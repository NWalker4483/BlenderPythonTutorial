import logging
import os

from .menu import register as register
from .menu import unregister as unregister

# print("Cat")
# logging.info("Cat")

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


if __name__ == "__main__":
    setup_logging()
    register()
