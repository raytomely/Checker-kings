import sys
from cx_Freeze import setup, Executable

setup(
    name ='checker_kings',
    author='rdn',
    version = '1.0',
    options={'build_exe':{'include_files':['checker_resources/checker_icon.png','checker_resources/checker_title2.png','checker_resources/board3.png',
    'checker_resources/green_light.png','checker_resources/red_light.png','checker_resources/circle_pieces.png','checker_resources/chess_pieces.png','checker_resources/ghost.png',
    'checker_resources/sphere.png','checker_resources/smiley.png']}},
    executables = [Executable('checker_kings_gui.py', base = 'Win32GUI',icon = 'checker_icon.ico')])



#in command line(cmd)  change to current directory(cd) and write: "setup.py build" or "setup.py build_exe"
