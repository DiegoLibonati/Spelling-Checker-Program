import logging
from unittest.mock import MagicMock, patch

import pytest

from src.utils.dialogs import BaseDialogError, ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


class TestTkinterExceptionHook:
    def test_base_dialog_subclass_calls_open(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="test error")
        mock_open: MagicMock = MagicMock()

        with patch.object(error, "open", mock_open):
            tkinter_exception_hook(type(error), error, None)

        mock_open.assert_called_once()

    def test_base_dialog_error_calls_open(self) -> None:
        error: BaseDialogError = BaseDialogError(message="base error")
        mock_open: MagicMock = MagicMock()

        with patch.object(error, "open", mock_open):
            tkinter_exception_hook(type(error), error, None)

        mock_open.assert_called_once()

    def test_non_dialog_exception_creates_internal_error(self) -> None:
        exc: ValueError = ValueError("something went wrong")
        mock_instance: MagicMock = MagicMock()

        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
            mock_internal.return_value = mock_instance
            tkinter_exception_hook(type(exc), exc, None)

        mock_internal.assert_called_once_with(message="something went wrong")

    def test_non_dialog_exception_opens_internal_error(self) -> None:
        exc: RuntimeError = RuntimeError("runtime failure")
        mock_instance: MagicMock = MagicMock()

        with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
            mock_internal.return_value = mock_instance
            tkinter_exception_hook(type(exc), exc, None)

        mock_instance.open.assert_called_once()

    def test_logs_error_on_exception(self, caplog: pytest.LogCaptureFixture) -> None:
        exc: RuntimeError = RuntimeError("log this")

        with caplog.at_level(logging.ERROR):
            with patch("src.utils.tkinter_exception_hook.InternalDialogError"):
                tkinter_exception_hook(type(exc), exc, None)

        assert "Unhandled exception" in caplog.text
