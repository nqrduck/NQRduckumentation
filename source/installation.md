# Installation

## Requirements

- Python 3.10+
- pip
- virtualenv
- About 600MB of free storage space

## Steps (Linux)

1. Install the specified requirements.

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    . venv/bin/activate
    ```

3. You can now install the NQRduck core program:

    ```bash
    pip install nqrduck
    ```

4. Run the program with `nqrduck`. This should open up a window with the NQRduck install wizard.

5. The install wizard for different modules should open up. Install the modules you would like to use. Some  modules have dependencies on other modules, but the install wizard will automatically install them for you.

6. You now need to restart the program.

7. You can switch between different modules with the toolbar. You can customize the appearance of the program in `Settings -> Preferences`. Settings are saved and restored on the next start.
Some settings need a restart to take effect - so it's recommended to restart the program after changing settings.

## Uninstall

To uninstall the NQRduck, you can simply delete the virtual environment. If you additionally want the nqrduck package to remove any other files, you can run:

```bash
nqrduck --uninstall
```

This removes the desktop file and the icon from the system.
