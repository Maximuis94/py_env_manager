"""
CLI implementation for environmental variable manager
"""
import argparse
import os
from py_env_manager.src.setup import setup_environmental_variable

_ENV_VAR_KEY = "PY_ENV_ROOT"

parser = argparse.ArgumentParser(
    description=f'Register a value for {_ENV_VAR_KEY} in environmental variables'
)
parser.add_argument(
    'path',
    help='The root directory to register as value for the environmental variable.',
    default=None
)
parser.add_argument(
    '--force-register-key',
    help='If True/1, execute setup regardless of whether the key exists or not',
    choices=[0, False, 1, True],
    default=0
)
args = parser.parse_args()
if not os.environ.get(_ENV_VAR_KEY, not args.force_register_key):
    if setup_environmental_variable(key=_ENV_VAR_KEY, value=args.path):
        print(f"Successfully updated the {_ENV_VAR_KEY} environment variable")
    else:
        print(f"Did not update the {_ENV_VAR_KEY} environment variable")
else:
    print(f"{_ENV_VAR_KEY} is already registered as an environment variable with value {os.environ[_ENV_VAR_KEY]}")
