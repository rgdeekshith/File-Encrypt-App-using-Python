import sys, os
from cx_Freeze import setup, Executable

os.environ["TCL_LIBRARY"] = "C:\Program Files\Python37/tcl/tcl8.6"
os.environ["TK_LIBRARY"] = "C:\Program Files\Python37/tcl/tk8.6"

base = None
include_files = [
    "./assets",
    "C:\Program Files\Python37/DLLs/tcl86t.dll",
    "C:\Program Files\Python37/DLLs/tk86t.dll"
]

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="KrypApp",
    version="1.0",
    description="File Encryption App",
    options={
        "build_exe": {
            "include_files": include_files
            }
    },
    executables=[
        Executable(
            "KrypApp.py",
            base=base,
            targetName="KrypApp.exe",
            icon="./assets/icon.ico"
        )
    ]
)
