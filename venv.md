# venv
virtual environment


## info
+ OS Windows 11 (version 10.0.22631.3593)
+ Windows Terminal (version 1.19.11213.0)
+ Drive V
+ Python 3 (version 3.12.3)
+ pip 24.0


## create
```
V:\>py -m venv randp

V:\>
```

## activate
Activate virtual environment
```
V:\>randp\Scripts\activate

(randp) V:\>
```

## deactivate
Deactivate virtual environment
```
(randp) V:\>deactivate
V:\>
```

## pip
List installed package
```
(randp) V:\>pip list
Package Version
------- -------
pip     24.0

(randp) V:\>
```

## sympy
Install sympy
```
(randp) V:\>pip install sympy
Collecting sympy
  Downloading sympy-1.12-py3-none-any.whl.metadata (12 kB)
Collecting mpmath>=0.19 (from sympy)
  Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Downloading sympy-1.12-py3-none-any.whl (5.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.7/5.7 MB 960.5 kB/s eta 0:00:00
Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 1.9 MB/s eta 0:00:00
Installing collected packages: mpmath, sympy
Successfully installed mpmath-1.3.0 sympy-1.12

(randp) V:\>
```

List installed packages
```
(randp) V:\>pip list
Package Version
------- -------
mpmath  1.3.0
pip     24.0
sympy   1.12
(randp) V:\>
```

Show particular package(s)
```
(randp) V:\>pip show sympy
Name: sympy
Version: 1.12
Summary: Computer algebra system (CAS) in Python
Home-page: https://sympy.org
Author: SymPy development team
Author-email: sympy@googlegroups.com
License: BSD
Location: V:\randp\Lib\site-packages
Requires: mpmath
Required-by:
```
