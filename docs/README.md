# docs
early documentation for this repository


## virtual environment
+ Download [`requirements.txt`](requirements.txt) to `V:\`
+ Open cmd
  ```
  V:\>
  ```
+ Create virtual enviroment
  ```
  V:\>py -m venv randp
  ```
+ Activate virtual enviroment
  ```
  V:\>randp/Script/activate
  ```
+ Install all packages
  ```
  (randp) V:\>pip install -r requirements.txt
  ```
+ Deactivate virtual environment
  ```
  (randp) V:\>deactivate
  ```
+ Close cmd
  ```
  V:\>exit
  ```
+ See [`venv.md`](venv.md) for more details, if necessary


## clone repository
+ Use GitBash or [install it first](https://medium.com/p/8d4c29799185).
  ```
  viridi@ryzen7 MINGW64 /m
  $ git clone https://github.com/dudung/random-problem
  Cloning into 'random-problem'...
  remote: Enumerating objects: 5, done.
  remote: Counting objects: 100% (5/5), done.
  remote: Compressing objects: 100% (5/5), done.
  remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
  Receiving objects: 100% (5/5), done.
  ```
+ Change directory
  ```
  viridi@ryzen7 MINGW64 /m
  $ cd random-problem
  ```
+ List all files
  ```
  viridi@ryzen7 MINGW64 /m
  $ ls -l
  total 168
  -rw-r--r-- 1 Sparisoma Viridi 197121   1094 May 25 08:48 LICENSE
  -rw-r--r-- 1 Sparisoma Viridi 197121   1656 May 25 10:48 README.md
  -rwxr-xr-x 1 Sparisoma Viridi 197121   1172 May 25 10:39 cmd.lnk*
  -rw-r--r-- 1 Sparisoma Viridi 197121   2148 May 25 10:18 requirements.txt
  -rw-r--r-- 1 Sparisoma Viridi 197121 153213 May 25 10:25 venv.md
  ```
+ Close GitBash
  ```
  viridi@ryzen7 MINGW64 /m
  $ exit
  ```

## jupyter notebook
+ Open `random-problem folder` on `M:\`
+ Open cmd
  ```
  M:\random-problem>
  ```
+ Activate virtual enviroment
  ```
  M:\random-problem>v:\randp\Scripts\activate
  ```
+ Run Jupyter Notebook
  ```
  (randp) M:\random-problem>jupyter notebook
  ```
+ Work on Jupyter opened Notebook window
  ![](jupyter_notebook.png)
+ Terminate Jupyter Notebook with CTRL+C on the cmd
  ```
  (randp) M:\random-problem>
  ```
+ Deactivate virtual environment
  ```
  (randp) M:\random-problem>deactivate
  ```
+ Close cmd
  ```
  M:\random-problem>exit
  ```
