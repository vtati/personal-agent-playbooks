"""Unit tests for Scanner scoring + Time Machine gate/sizing.
Run: python3 tests/run_tests.py  (from the tools/ folder)
Pure-function tests only — no network, no broker calls.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from time_machine import classify_path, analog_stats, monte_carlo, gate_verdict, size_position
from scanner import score_candidate


# ---------- Time Machine: first passage ----------
def test_classify_target_hit_first():
    # entry 100, stop 95, target 110 — path rises to target before dipping to stop
    outcome, exit_price, days = classify_path([100, 103, 108, 111, 90], stop=95, target=110, horizon=5)
    assert outcome == "target" and exit_price == 110 and days == 3

def test_classify_stop_hit_first():
    outcome, exit_price, days = classify_path([100, 97, 94, 120], stop=95, target=110, horizon=5)
    assert outcome == "stop" and exit_price == 95 and days == 2

def test_classify_timeout_at_close():
    outcome, exit_price, days = classify_path([100, 101, 99, 102], stop=95, target=110, horizon=3)
    assert outcome == "timeout" and exit_price == 102 and days == 3

def test_classify_same_bar_stop_wins():
    # a single bar that crosses BOTH stop and target resolves to stop (conservative)
    outcome, _, _ = classify_path([100, 100], stop=95, target=110, horizon=1) if False else classify_path([100, 115], stop=95, target=110, horizon=1, lows=[100, 90], highs=[100, 116])
    assert outcome == "stop"

# ---------- Time Machine: analog stats ----------
def test_analog_stats_uptrend_positive_expectancy():
    closes = [100 + i * 0.5 for i in range(120)]  # steady uptrend
    stats = analog_stats(closes, stop_pct=0.05, target_pct=0.10, horizon=40)
    assert stats["n"] > 50
    assert stats["p_target"] > 0.8
    assert stats["expectancy_r"] > 0

def test_analog_stats_downtrend_negative_expectancy():
    closes = [200 - i * 0.5 for i in range(120)]  # steady downtrend
    stats = analog_stats(closes, stop_pct=0.05, target_pct=0.10, horizon=40)
    assert stats["p_stop"] > 0.8
    assert stats["expectancy_r"] < 0

# ---------- Time Machine: Monte Carlo ----------
def test_monte_carlo_deterministic_and_bounded():
    import random
    rng = random.Random(7)
    returns = [rng.gauss(0.001, 0.01) for _ in range(500)]
    a = monte_carlo(returns, start=100, stop=95, target=110, horizon=20, n_paths=2000, seed=42)
    b = monte_carlo(returns, start=100, stop=95, target=110, horizon=20, n_paths=2000, seed=42)
    assert a == b  # same seed = same result
    total = a["p_target"] + a["p_stop"] + a["p_timeout"]
    assert abs(total - 1.0) < 1e-9

def test_monte_carlo_strong_drift_mostly_target():
    import random
    rng = random.Random(3)
    returns = [rng.gauss(0.01, 0.005) for _ in range(500)]  # +1%/day drift
    stats = monte_carlo(returns, start=100, stop=95, target=110, horizon=20, n_paths=2000, seed=1)
    assert stats["p_target"] > 0.7

# ---------- Time Machine: the R18 gate ----------
def test_gate_pass():
    assert gate_verdict(expectancy_r=0.35, p_stop=0.30, earnings_in_horizon=False) == "PASS"

def test_gate_veto_on_negative_expectancy():
    assert gate_verdict(expectancy_r=-0.05, p_stop=0.30, earnings_in_horizon=False) == "VETO"

def test_gate_veto_on_high_stop_prob_even_if_positive():
    assert gate_verdict(expectancy_r=0.30, p_stop=0.60, earnings_in_horizon=False) == "VETO"

def test_gate_earnings_caps_at_watch():
    assert gate_verdict(expectancy_r=0.50, p_stop=0.20, earnings_in_horizon=True) == "WATCH"

def test_gate_watch_band():
    assert gate_verdict(expectancy_r=0.10, p_stop=0.30, earnings_in_horizon=False) == "WATCH"

# ---------- Time Machine: R10/R16 sizing ----------
def test_sizing_risk_budget_1pct():
    # synthetic fixture: pilot 10,000 units, entry 100, stop 95 -> risk/share 5, budget 100 -> 20 sh = 2,000 position
    # but the R16 single-name cap (10% of pilot = 1,000) -> capped at 10 shares, risk 50
    s = size_position(pilot_value=10000, entry=100, stop=95)
    assert s["position_dollars"] == 1000 and s["shares"] == 10 and s["risk_dollars"] == 50

def test_sizing_uncapped_case():
    # entry 100, stop 90 -> risk/share $10, budget $100 -> 10 sh = $1,000 = cap exactly
    s = size_position(pilot_value=10000, entry=100, stop=90)
    assert s["shares"] == 10 and s["risk_dollars"] == 100

def test_sizing_tight_stop_hits_cap():
    # entry 100, stop 99 -> budget would buy 100 sh (10,000) -> cap binds to 10 sh
    s = size_position(pilot_value=10000, entry=100, stop=99)
    assert s["position_dollars"] == 1000 and s["risk_dollars"] == 10

def test_sizing_zero_when_stop_equals_entry():
    s = size_position(pilot_value=10000, entry=100, stop=100)
    assert s["shares"] == 0 and s["position_dollars"] == 0

# ---------- Scanner scoring ----------
STRONG = dict(forward_pe=15.0, net_margin=25.0, roe=30.0, revenue_growth_pct=18.0,
              income_growth_pct=22.0, buy=50, hold=5, sell=0, price=120.0, sma50=110.0, rsi=55.0)
WEAK = dict(forward_pe=34.0, net_margin=2.0, roe=3.0, revenue_growth_pct=-8.0,
            income_growth_pct=-15.0, buy=2, hold=20, sell=8, price=90.0, sma50=110.0, rsi=78.0)

def test_scanner_strong_beats_weak():
    s_strong = score_candidate(**STRONG)
    s_weak = score_candidate(**WEAK)
    assert s_strong["total"] > s_weak["total"]
    assert s_strong["total"] >= 70
    assert s_weak["total"] <= 40

def test_scanner_missing_data_scores_zero_and_is_named():
    s = score_candidate(forward_pe=None, net_margin=None, roe=None, revenue_growth_pct=None,
                        income_growth_pct=None, buy=None, hold=None, sell=None,
                        price=None, sma50=None, rsi=None)
    assert s["total"] == 0
    assert len(s["missing"]) >= 5  # every missing leg is named, never silently passed

def test_scanner_overbought_rsi_gets_no_trend_points():
    base = dict(STRONG); base["rsi"] = 85.0
    s = score_candidate(**base)
    assert s["legs"]["trend"] < score_candidate(**STRONG)["legs"]["trend"]
