import sys
import os
from cx_Freeze import setup, Executable

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI"
)

# List of files to include
files = []  # Add other files or folders as needed

# SETUP CX FREEZE
setup(
    name = "PlayBud",
    version = "1.0",
    description = "Game Recommendation App",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)