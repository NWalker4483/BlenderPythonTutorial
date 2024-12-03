# Add these lines at the top of your script
import sys
import os
import glob

PACKAGE_NAME = "btest"
VENV_PATH = '/home/walkenz1/.cache/pypoetry/virtualenvs/btest-UeLnX-4F-py3.12/'

###########region Jank (Shouldn't need to modify)
# Find the Python lib directory dynamically
lib_pattern = os.path.join(VENV_PATH, 'lib','python3.*')
python_libs = glob.glob(lib_pattern)

if python_libs:
    # Use the first matching Python lib directory found
    SITE_PACKAGES_DIR = os.path.join(python_libs[0], 'site-packages')
    PROJECT_DIR = os.path.dirname(__file__)
    # Add to Python path if not already there
    if SITE_PACKAGES_DIR not in sys.path:
        sys.path.append(SITE_PACKAGES_DIR)
    if PROJECT_DIR not in sys.path:
        sys.path.append(PROJECT_DIR)

else:
    raise(RuntimeError(f"No Python lib directory found in {VENV_PATH}"))

import importlib
# Reload all modules that start with 'btest'
for module_name in list(sys.modules.keys()):
    if module_name.startswith(PACKAGE_NAME):
        try:
            importlib.reload(sys.modules[module_name])
        except ModuleNotFoundError: # Old Submodule no longer exists
            pass

import debugpy
if not debugpy.is_client_connected:
    # Allow other computers to attach to debugpy at this IP address and port.
    debugpy.listen(("0.0.0.0", 5678))
    # Pause the script until a remote debugger is attached
    debugpy.wait_for_client()

import logging
logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), "log.txt"), 
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
logging.getLogger().setLevel(logging.DEBUG) # Set the level of the root logger
###############################################

from btest.main import main
main()