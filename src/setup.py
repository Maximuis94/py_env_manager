"""
Setup module for registering the root directory as environmental variable
"""
import os
from typing import Literal

from src.util import evaluate_directory, is_directory_string, prompt_yn, set_env_var


def setup_environmental_variable(key: str, path: str = None) -> Literal[0, 1]:
    """Register the .env root directory as environmental variable with ENV_VAR_KEY as key. If the given value refers to
    a non-existent root directory, ask to create it.
    If the variable is already registered, notify user and overwrite it instead.
    On completion, exit() is called for the registration to take effect.
    
    Returns
    -------
    Literal[0]
        Failed to register the root directory as environmental variable.
    Literal[1]
        Successfully registered the root directory as environmental variable.

    Raises
    ------
    RuntimeError
        If the environment variable does not exist and the user does not wish to install it.
    """
    print("Setting up environmental variable...")
    if os.environ.get(key, False):
        prompt_yn(f"{key} already has a value registered to it.\n"
              f"Would you like to overwrite the current value of '{os.environ[key]}' registered as "
              f"environmental variable with key={key}?")
    
    while path is None or not evaluate_directory(path):
        try:
            path = input(f"Which value would you like to set for key={key}? "
                          f"Alternatively, press enter immediately to use clipboard contents instead or press CTRL+C "
                          f"(cli) to abort.")
        except KeyboardInterrupt:
            print("\nAborting...")
            return 0
        
        if path == "":
            import pyperclip
            path = pyperclip.paste()
            if not prompt_yn(f"Register '{path}' as root directory for .env files used by the manager?"):
                path = None
        
        if is_directory_string(path) and not os.path.exists(path):
            if (not os.path.exists(path) and
                    prompt_yn(f'Path "{path}" does not refer to an existing directory.'
                              f'\n\tWould you like to create it?')):
                os.makedirs(path)
    
    set_env_var(key, path)
    print(f"Successfully registered '{key}' as environmental variable with value '{path}'.")
    return 1
