# Installed Command Line Options
Below are the python installer supported command line options since 2.7.6.1:

  * /S - silent installation
  * /FULL - Install/update all of the available plugins
  * /INSTDIR="path"- XY install root
  * /MINGWPATH="path" - mingw install root
  * /SWIGPATH="path" - swig install root
  * /PYTHONPATH="path" - Python Interpreter Install Root
  * /AllUsers - Install for all users (default)
  * ~~/CurrentUser - Install for current user~~ (untested).

# Example:
```
Python(x,y)-2.7.6.1.exe /INSTDIR="c:\xy" /MINGWPATH=c:\mingw32 /SWIGPATH=c:\swig /PYTHONPATH=c:\py27 /FULL /S
```