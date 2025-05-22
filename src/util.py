"""
Utility functions
"""

import os
import sys
import winreg
from pathlib import PurePath


def prompt_yn(prompt: str) -> bool:
    """Ask the user for permission to proceed. If the user inputs 'y' or 'Y', True is returned, False otherwise."""
    return input(prompt.strip()+" [y/n] ").lower() == "y"


def is_directory_string(path: str) -> bool:
    """Returns True if `path` describes a directory. Note that this does not work perfectly."""
    return path.endswith((os.sep, "/")) or PurePath(path).suffix == ""


def is_env_file(path: str) -> bool:
    """Returns True if `path` refers to an existing .env file"""
    return os.path.isfile(path) and path.endswith(".env")


# Functions used to validate specific types of values
# region evaluation_functions

def evaluate_directory(path: str) -> bool:
    """Evaluate whether path refers to an existing directory or not. If not, print feedback and return False."""
    if os.path.isdir(path):
        return True
    
    print(f"""Path "{path}" does not refer to an existing directory.""")
    return os.path.isdir(path)


def evaluate_file(path: str) -> bool:
    """Evaluate whether path refers to an existing file or not. If not, print feedback and return False."""
    if os.path.isfile(path):
        return True
    
    print(f"""Path "{path}" does not refer to an existing file.""")
    return False


def evaluate_path(path: str) -> bool:
    """Function that determines which function to use, then returns the function call with this value"""
    return (evaluate_directory if is_directory_string(path) else evaluate_file)(path)


# endregion

#region environmental variable registration functions
def _set_env_var_windows(name: str, value: str):
    
    reg = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Environment",
        0,
        winreg.KEY_SET_VALUE
    )
    
    winreg.SetValueEx(reg, name, 0, winreg.REG_EXPAND_SZ, value)
    winreg.CloseKey(reg)
    
    import ctypes
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x001A
    SMTO_ABORTIFHUNG = 0x0002
    ctypes.windll.user32.SendMessageTimeoutW(
        HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment", SMTO_ABORTIFHUNG, 5000, None)


def _set_env_var_linux(name: str, value: str):
    raise NotImplementedError


def _set_env_var_macos(name: str, value: str):
    raise NotImplementedError


def set_env_var(name: str, value: str):
    """Registers a specific environmental variable for the users' OS with `key` as key and `value` as value."""
    if sys.platform == "win32":
        return _set_env_var_windows(name, value)
    if sys.platform == "darwin":
        return _set_env_var_macos(name, value)
    if sys.platform.startswith("linux"):
        return _set_env_var_linux(name, value)


#endregion


