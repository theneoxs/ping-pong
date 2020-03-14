from cx_Freeze import setup,Executable
import sys
 
base=None
if sys.platform=='win32':
    base='Win32GUI'
    
setup(name='Ping-Pong',
      version='1.0',
      executables=[Executable(script='game.py',base=base)])