from unittest.mock import MagicMock, patch

from src.utils.dialogs import BaseDialogError, ValidationDialogError
from src.utils.error_handler import error_handler


class TestErrorHandler:
    def test_base_dialog_subclass_calls_open(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="test error")
        with patch.object(error, "open") as mock_open:
            error_handler(type(error), error, None)
            mock_open.assert_called_once()

    def test_base_dialog_error_calls_open(self) -> None:
        error: BaseDialogError = BaseDialogError(message="base error")
        with patch.object(error, "open") as mock_open:
            error_handler(type(error), error, None)
            mock_open.assert_called_once()

    def test_non_dialog_exception_creates_internal_error(self) -> None:
        exc: ValueError = ValueError("something went wrong")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
            mock_internal.assert_called_once_with(message="something went wrong")

    def test_non_dialog_exception_opens_internal_error(self) -> None:
        exc: RuntimeError = RuntimeError("runtime failure")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
            mock_instance.open.assert_called_once()
