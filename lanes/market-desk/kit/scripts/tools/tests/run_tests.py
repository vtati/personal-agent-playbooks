"""Tiny test runner (pytest is not installed on this VM). Runs every test_* in test_tools.py."""
import sys, pathlib, traceback
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import test_tools

names = [n for n in dir(test_tools) if n.startswith("test_")]
passed, failed = 0, []
for n in sorted(names):
    try:
        getattr(test_tools, n)()
        passed += 1
        print(f"PASS {n}")
    except Exception:
        failed.append(n)
        print(f"FAIL {n}")
        traceback.print_exc(limit=2)
print(f"\n{passed} passed, {len(failed)} failed, {passed+len(failed)} total")
sys.exit(1 if failed else 0)
