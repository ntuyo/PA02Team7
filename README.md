# PA02Team7
Team 7 PA2 - Tiffany's Branch
(base) PS C:\Users\tiffh\PA02Team7\pa02> pylint tracker.py
************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:94:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:119:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:146:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:162:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:44:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:64:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:62:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:62:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:125:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:142:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:147:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:149:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:150:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:152:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:153:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:37:0: W0611: Unused import sys (unused-import)
tracker.py:37:0: C0411: standard import "import sys" should be placed before "from category import Category" (wrong-import-order)

-----------------------------------
Your code has been rated at 7.62/10

(base) PS C:\Users\tiffh\PA02Team7\pa02> pytest -v -m tiffany
================================================= test session starts =================================================
platform win32 -- Python 3.9.5, pytest-7.1.1, pluggy-1.0.0 -- c:\users\tiffh\miniconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\tiffh\PA02Team7\pa02, configfile: pytest.ini
plugins: anyio-3.5.0
collected 7 items / 6 deselected / 1 selected

test_transaction.py::test_tiffanys_tests PASSED                                                                  [100%]

=========================================== 1 passed, 6 deselected in 0.47s ===========================================
