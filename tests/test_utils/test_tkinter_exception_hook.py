from unittest.mock import MagicMock, patch

import pytest

from src.utils.dialogs import ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


@pytest.mark.unit
class TestTkinterExceptionHook:
    def test_calls_open_when_exception_is_base_dialog(self) -> None:
        exc: ValidationDialogError = ValidationDialogError(message="test error")
        exc.open = MagicMock()

        with patch("src.utils.tkinter_exception_hook.logger"):
            tkinter_exception_hook(type(exc), exc, None)

        exc.open.assert_called_once()

    def test_wraps_non_dialog_exception_in_internal_dialog_error(self) -> None:
        exc: ValueError = ValueError("unexpected error")
        mock_instance: MagicMock = MagicMock()

        with patch("src.utils.tkinter_exception_hook.logger"):
            with patch(
                "src.utils.tkinter_exception_hook.InternalDialogError", return_value=mock_instance
            ) as mock_cls:
                tkinter_exception_hook(type(exc), exc, None)

        mock_cls.assert_called_once_with(message=str(exc))
        mock_instance.open.assert_called_once()

    # def test_logs_error_for_non_dialog_exception(self) -> None:
    #     exc: RuntimeError = RuntimeError("log this")

    #     with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
    #         with patch(
    #             "src.utils.tkinter_exception_hook.InternalDialogError", return_value=MagicMock()
    #         ):
    #             tkinter_exception_hook(type(exc), exc, None)

    #     mock_logger.error.assert_called_once()

    # def test_logs_error_for_base_dialog_exception(self) -> None:
    #     exc: ValidationDialogError = ValidationDialogError(message="dialog error")
    #     exc.open = MagicMock()

    #     with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
    #         tkinter_exception_hook(type(exc), exc, None)

    #     mock_logger.error.assert_called_once()
