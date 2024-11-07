"""Logging configuration."""

import logging
import os
import time


class Log:
    """Setup logging."""

    LOG_LEVEL = os.getenv("LOG_LEVEL").upper() if os.getenv("LOG_LEVEL") else "ERROR"
    """Set log level."""

    @classmethod
    def logger(cls, desc="app") -> logging.getLogger:
        """Configure logger object."""
        logging.basicConfig(
            level=getattr(logging, cls.LOG_LEVEL),
            format="%(levelname)s - %(asctime)s UTC - %(name)s - %(message)s",
        )
        logging.Formatter.converter = time.gmtime

        return logging.getLogger(desc)
