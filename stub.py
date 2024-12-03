import sys
import os
import glob
import importlib
import logging
import debugpy
import bl_ui

# Configuration
PACKAGE_NAME = "btest"
VENV_PATH = '/home/walkenz1/.cache/pypoetry/virtualenvs/btest-UeLnX-4F-py3.12/'
DEBUG_HOST = "0.0.0.0"
DEBUG_PORT = 5678

def setup_logging():
    """Configure logging to write to a file in the script's directory."""
    log_file = os.path.join(os.path.dirname(__file__), "log.txt")
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info("Logging initialized")

def reload_blender_ui():
    """Reload Blender's UI to prevent addon UI elements from duplicating."""
    bl_ui.unregister()
    importlib.reload(bl_ui)
    bl_ui.register()
    logging.debug("Blender UI reloaded")

def setup_python_paths():
    """Configure Python path to include virtualenv site-packages and project directory."""
    # Find Python lib directory
    lib_pattern = os.path.join(VENV_PATH, 'lib', 'python3.*')
    python_libs = glob.glob(lib_pattern)
    
    if not python_libs:
        raise RuntimeError(f"No Python lib directory found in {VENV_PATH}")
    
    # Setup paths
    site_packages_dir = os.path.join(python_libs[0], 'site-packages')
    project_dir = os.path.dirname(__file__)
    
    # Add to Python path if not already present
    for path in [site_packages_dir, project_dir]:
        if path not in sys.path:
            sys.path.append(path)
            logging.debug(f"Added to Python path: {path}")

def reload_package_modules():
    """Reload all submodules of the specified package."""
    for module_name in list(sys.modules.keys()):
        if module_name.startswith(PACKAGE_NAME):
            try:
                importlib.reload(sys.modules[module_name])
                logging.debug(f"Reloaded module: {module_name}")
            except ModuleNotFoundError:
                logging.warning(f"Module not found during reload: {module_name}")

def setup_debugger():
    """Configure remote debugging with debugpy."""
    if not debugpy.is_client_connected():
        debugpy.listen((DEBUG_HOST, DEBUG_PORT))
        logging.info(f"Debugpy listening on {DEBUG_HOST}:{DEBUG_PORT}")
        debugpy.wait_for_client()
        logging.info("Debugger client connected")

def main():
    """Initialize all debug components and start the main application."""
    setup_logging()
    reload_blender_ui()
    setup_python_paths()
    reload_package_modules()
    setup_debugger()
    
    # Import and run main application
    from btest.main import main as run 
    run()

if __name__ == "__main__":
    main()
