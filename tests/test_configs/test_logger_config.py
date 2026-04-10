import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger(self) -> None:
        logger: logging.Logger = setup_logger()
        assert isinstance(logger, logging.Logger)

    def test_default_name(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "tkinter-app"

    def test_custom_name(self) -> None:
        logger: logging.Logger = setup_logger("custom-logger")
        assert logger.name == "custom-logger"

    def test_has_handler(self) -> None:
        logger: logging.Logger = setup_logger("test-handler-logger")
        assert len(logger.handlers) > 0

    def test_no_duplicate_handlers(self) -> None:
        logger: logging.Logger = setup_logger("test-no-dup")
        handler_count: int = len(logger.handlers)
        setup_logger("test-no-dup")
        assert len(logger.handlers) == handler_count

    def test_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("test-level-logger")
        assert logger.level == logging.DEBUG

    def test_handler_has_formatter(self) -> None:
        logger: logging.Logger = setup_logger("test-formatter-logger")
        assert logger.handlers[0].formatter is not None
