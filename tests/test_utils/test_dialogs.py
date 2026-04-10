from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP, MESSAGE_NOT_FOUND_DIALOG_TYPE
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BaseDialogNotification,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message_overrides_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message="custom error")
        assert dialog.message == "custom error"

    def test_none_message_keeps_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)
        assert dialog.message == MESSAGE_ERROR_APP

    def test_title_for_error(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.title == "Error"

    def test_title_for_unknown_type_falls_back_to_error(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = "UNKNOWN"
        assert dialog.title == "Error"

    def test_to_dict_contains_dialog_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result = dialog.to_dict()
        assert result["dialog_type"] == BaseDialog.ERROR

    def test_to_dict_contains_title(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result = dialog.to_dict()
        assert result["title"] == "Error"

    def test_to_dict_contains_message(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result = dialog.to_dict()
        assert result["message"] == MESSAGE_ERROR_APP

    def test_to_dict_custom_message(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")
        result = dialog.to_dict()
        assert result["message"] == "test msg"

    def test_open_calls_showerror(self) -> None:
        dialog: BaseDialog = BaseDialog()
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()
            mock_handler.assert_called_once_with("Error", MESSAGE_ERROR_APP)

    def test_open_warning_calls_showwarning(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.WARNING
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            dialog.open()
            mock_handler.assert_called_once()

    def test_open_info_calls_showinfo(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = BaseDialog.INFO
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            dialog.open()
            mock_handler.assert_called_once()

    def test_open_unknown_type_calls_showerror(self) -> None:
        dialog: BaseDialog = BaseDialog()
        dialog.dialog_type = "UNKNOWN"
        with patch("src.utils.dialogs.messagebox.showerror") as mock_showerror:
            dialog.open()
            mock_showerror.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


class TestBaseDialogError:
    def test_is_exception(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, Exception)

    def test_is_base_dialog(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert error.dialog_type == BaseDialog.ERROR

    def test_can_be_raised(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError()


class TestValidationDialogError:
    def test_default_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError()
        assert error.message == "Validation error"

    def test_custom_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="fields required")
        assert error.message == "fields required"

    def test_is_base_dialog_error(self) -> None:
        assert issubclass(ValidationDialogError, BaseDialogError)

    def test_can_be_raised(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError()


class TestAuthenticationDialogError:
    def test_default_message(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError()
        assert error.message == "Authentication error"

    def test_is_base_dialog_error(self) -> None:
        assert issubclass(AuthenticationDialogError, BaseDialogError)


class TestNotFoundDialogError:
    def test_default_message(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError()
        assert error.message == "Resource not found"

    def test_is_base_dialog_error(self) -> None:
        assert issubclass(NotFoundDialogError, BaseDialogError)


class TestConflictDialogError:
    def test_default_message(self) -> None:
        error: ConflictDialogError = ConflictDialogError()
        assert error.message == "Conflict error"

    def test_is_base_dialog_error(self) -> None:
        assert issubclass(ConflictDialogError, BaseDialogError)


class TestBusinessDialogError:
    def test_default_message(self) -> None:
        error: BusinessDialogError = BusinessDialogError()
        assert error.message == "Business rule violated"

    def test_is_base_dialog_error(self) -> None:
        assert issubclass(BusinessDialogError, BaseDialogError)


class TestInternalDialogError:
    def test_default_message(self) -> None:
        error: InternalDialogError = InternalDialogError()
        assert error.message == "Internal error"

    def test_is_base_dialog_error(self) -> None:
        assert issubclass(InternalDialogError, BaseDialogError)


class TestDeprecatedDialogWarning:
    def test_dialog_type_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.message == "This feature is deprecated"

    def test_is_base_dialog_notification(self) -> None:
        assert issubclass(DeprecatedDialogWarning, BaseDialogNotification)


class TestSuccessDialogInformation:
    def test_dialog_type_is_info(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.message == "Operation completed successfully"

    def test_is_base_dialog_notification(self) -> None:
        assert issubclass(SuccessDialogInformation, BaseDialogNotification)
