import datetime
import os

class Logger:
    """
    A simple logger class to log messages to a file or console.
    """

    LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def __init__(self, log_file=None, log_level="INFO"):
        """
        Initialize the logger.

        :param log_file: Path to the log file (optional).
        :param log_level: Minimum log level to log messages.
        """
        self.log_file = log_file
        self.log_level = log_level.upper()
        if self.log_level not in self.LOG_LEVELS:
            raise ValueError(f"Invalid log level: {self.log_level}")

    def _log(self, level, message):
        """
        Internal method to log a message.

        :param level: Log level of the message.
        :param message: The message to log.
        """
        if self.LOG_LEVELS.index(level) >= self.LOG_LEVELS.index(self.log_level):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] [{level}] {message}"
            if self.log_file:
                with open(self.log_file, "a") as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)

    def debug(self, message):
        """Log a debug message."""
        self._log("DEBUG", message)

    def info(self, message):
        """Log an info message."""
        self._log("INFO", message)

    def warning(self, message):
        """Log a warning message."""
        self._log("WARNING", message)

    def error(self, message):
        """Log an error message."""
        self._log("ERROR", message)

    def critical(self, message):
        """Log a critical message."""
        self._log("CRITICAL", message)


# Example usage:
if __name__ == "__main__":
    logger = Logger(log_file="app.log", log_level="DEBUG")
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")