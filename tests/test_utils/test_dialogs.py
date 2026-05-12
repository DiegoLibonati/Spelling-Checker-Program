from typing import Any
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


@pytest.mark.unit
class TestBaseDialog:
    def test_error_constant(self) -> None:
        assert BaseDialog.ERROR == "Error"

    def test_warning_constant(self) -> None:
        assert BaseDialog.WARNING == "Warning"

    def test_info_constant(self) -> None:
        assert BaseDialog.INFO == "Info"

    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.dialog_type == BaseDialog.ERROR

    def test_title_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.title == "Error"

    def test_title_for_warning_type(self) -> None:
        class WarningDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING

        dialog: WarningDialog = WarningDialog()

        assert dialog.title == "Warning"

    def test_title_for_info_type(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO

        dialog: InfoDialog = InfoDialog()

        assert dialog.title == "Information"

    def test_title_for_unknown_type_falls_back_to_error(self) -> None:
        class UnknownDialog(BaseDialog):
            dialog_type = "UNKNOWN"

        dialog: UnknownDialog = UnknownDialog()

        assert dialog.title == "Error"

    def test_init_overrides_message_when_provided(self) -> None:
        dialog: BaseDialog = BaseDialog(message="custom message")

        assert dialog.message == "custom message"

    def test_init_keeps_class_message_when_none(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.message == MESSAGE_ERROR_APP

    def test_to_dict_contains_required_keys(self) -> None:
        dialog: BaseDialog = BaseDialog()

        result: dict[str, Any] = dialog.to_dict()

        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_to_dict_values_match_attributes(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")

        result: dict[str, Any] = dialog.to_dict()

        assert result["dialog_type"] == dialog.dialog_type
        assert result["title"] == dialog.title
        assert result["message"] == "test msg"

    def test_open_calls_correct_handler_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog(message="error msg")
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Error", "error msg")

    def test_open_calls_correct_handler_for_warning_type(self) -> None:
        class WarningDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING

        dialog: WarningDialog = WarningDialog(message="warn msg")
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Warning", "warn msg")

    def test_open_calls_correct_handler_for_info_type(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO

        dialog: InfoDialog = InfoDialog(message="info msg")
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Information", "info msg")

    def test_open_with_invalid_type_shows_error_with_not_found_message(self) -> None:
        class BrokenDialog(BaseDialog):
            dialog_type = "INVALID"

        dialog: BrokenDialog = BrokenDialog()

        with patch("src.utils.dialogs.messagebox.showerror") as mock_showerror:
            dialog.open()

        mock_showerror.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


@pytest.mark.unit
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

    def test_can_be_raised_and_caught_as_base_dialog_error(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError(message="raised")

    def test_can_be_caught_as_generic_exception(self) -> None:
        with pytest.raises(Exception):
            raise BaseDialogError(message="raised")


@pytest.mark.unit
class TestValidationDialogError:
    def test_inherits_base_dialog_error(self) -> None:
        error: ValidationDialogError = ValidationDialogError()

        assert isinstance(error, BaseDialogError)

    def test_default_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError()

        assert error.message == "Validation error"

    def test_custom_message_overrides_default(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="field required")

        assert error.message == "field required"


@pytest.mark.unit
class TestInternalDialogError:
    def test_inherits_base_dialog_error(self) -> None:
        error: InternalDialogError = InternalDialogError()

        assert isinstance(error, BaseDialogError)

    def test_default_message(self) -> None:
        error: InternalDialogError = InternalDialogError()

        assert error.message == "Internal error"

    def test_custom_message_overrides_default(self) -> None:
        error: InternalDialogError = InternalDialogError(message="db connection failed")

        assert error.message == "db connection failed"


@pytest.mark.unit
class TestOtherDialogErrors:
    def test_authentication_dialog_error_inherits_base_dialog_error(self) -> None:
        assert isinstance(AuthenticationDialogError(), BaseDialogError)

    def test_not_found_dialog_error_inherits_base_dialog_error(self) -> None:
        assert isinstance(NotFoundDialogError(), BaseDialogError)

    def test_conflict_dialog_error_inherits_base_dialog_error(self) -> None:
        assert isinstance(ConflictDialogError(), BaseDialogError)

    def test_business_dialog_error_inherits_base_dialog_error(self) -> None:
        assert isinstance(BusinessDialogError(), BaseDialogError)


@pytest.mark.unit
class TestDeprecatedDialogWarning:
    def test_inherits_base_dialog_notification(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert isinstance(warning, BaseDialogNotification)

    def test_dialog_type_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert warning.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert warning.message == "This feature is deprecated"


@pytest.mark.unit
class TestSuccessDialogInformation:
    def test_inherits_base_dialog_notification(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()

        assert isinstance(info, BaseDialogNotification)

    def test_dialog_type_is_info(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()

        assert info.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()

        assert info.message == "Operation completed successfully"
