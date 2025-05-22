# py_env_manager
Manager for setting up and accessing environmental variables per project

## Setup
Setup is initiated automatically if during usage `PY_ENV_ROOT` is not registered as environment variable.
A directory is registered as environmental variable under `PY_ENV_ROOT` during setup. If the directory does not exist, 
it is created. 
At some point during setup, you will be asked to provide a path. It is also possible to copy the path to the
clipboard and press enter to extract clipboard contents instead.

## Command-Line Interface (CLI)
The CLI is used for setup and registering external .env files.

The setup protocol can be initiated via
```bash
python -m py_env_manager
```
or
```bash
python -m py_env_manager <path> [--force-register-key]
```

---

### Positional Argument

| Argument | Description                                                                                                                 |
| :------: |:----------------------------------------------------------------------------------------------------------------------------|
|  `path`  | The filesystem path to the directory you want to register as `PY_ENV_ROOT`. If undefined, it will be prompted during setup. |

---

### Optional Flags

| Flag                   | Type                      | Default | Description                                                                                                              |
| ---------------------- | ------------------------- | :-----: |:-------------------------------------------------------------------------------------------------------------------------|
| `--force-register-key` | `0`, `1`, `False`, `True` |   `0`   | If set to `1` or `True`, forces the setup script to run even if `PY_ENV_ROOT` already exists as an environment variable. |

---

### Environment Variable

* **`PY_ENV_ROOT`**
  The key under which your root `.env` directory will be registered in the user’s environment. This variable name is hard-coded.


---

### Behavior

1. Parses the `path` argument and validates it exists.
2. Checks whether `PY_ENV_ROOT` is set in the user’s environment:
   * If **not set**, or if `--force-register-key` is true, the setup protocol is executed in which a root directory is registered as environmental variable to write the new value (to shell‐profile or registry, depending on OS).
   * Otherwise, reports the current setting and exits.
3. Prints a success or failure message to `stdout`.

---


## Files
### Root directory
The registered root directory is used as default root directory for all files used by the manager. All .env files 
located in this directory are registered automatically.

### Key, path value pairs
Additionally, .env files located elsewhere can be added to the environmental_variable_files.json file and accessed using
the associated key. Paths registered this way should be absolute paths.

## EnvManager
The EnvManager is the class that is used to interact with registered .env files.

### Loading .env files
`EnvManager.load(...)` can be used to load an .env file into os.environ. Alternatively, one or more keys may be passed 
when initializing EnvManager. These keys will then be loaded during initialization.

### Registering .env files
.env files in the registered root are automatically accessible via the EnvManager. External .env files can be registered
via `EnvManager.register_external_env()`. Files in the external .env JSON file are not required to have the .env 
extension

### Accessing environment values
The EnvManager can also be used to get environment variable values. The value will be returned when calling `EnvManager.get(key)`
or `EnvManager[key]`. This, ofcourse, is also possible via os.environ.