import logging
import os
from pathlib import Path
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir_path = Path(__file__).parent.parent.parent / "logs"

log_dir_path.mkdir(parents=True, exist_ok=True)

LOG_FILE_PATH = log_dir_path / LOG_FILE

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    logging.info("This is a test log")