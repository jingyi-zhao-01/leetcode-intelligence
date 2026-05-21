import logging
import sys


def setup_logging():
    """Set up the root logger to log to both console and a file."""
    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Remove existing handlers to avoid duplication
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # Console handler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(log_formatter)
    root_logger.addHandler(stream_handler)

    # File handler
    file_handler = logging.FileHandler("app.log", mode="w")
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    # Silence noisy loggers
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("prisma").setLevel(logging.WARNING)
