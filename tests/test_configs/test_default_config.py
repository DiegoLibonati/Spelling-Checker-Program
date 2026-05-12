import os
from unittest.mock import patch

import pytest

from src.configs.default_config import DefaultConfig


@pytest.mark.unit
class TestDefaultConfig:
    def test_debug_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert config.DEBUG is False

    def test_testing_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert config.TESTING is False

    def test_tz_uses_env_variable_when_set(self) -> None:
        with patch.dict(os.environ, {"TZ": "UTC"}):
            config: DefaultConfig = DefaultConfig()

        assert config.TZ == "UTC"

    def test_tz_uses_default_when_env_not_set(self) -> None:
        filtered_env: dict[str, str] = {k: v for k, v in os.environ.items() if k != "TZ"}
        with patch.dict(os.environ, filtered_env, clear=True):
            config: DefaultConfig = DefaultConfig()

        assert config.TZ == "America/Argentina/Buenos_Aires"

    def test_env_name_uses_env_variable_when_set(self) -> None:
        with patch.dict(os.environ, {"ENV_NAME": "my-app"}):
            config: DefaultConfig = DefaultConfig()

        assert config.ENV_NAME == "my-app"

    def test_env_name_uses_default_when_env_not_set(self) -> None:
        filtered_env: dict[str, str] = {k: v for k, v in os.environ.items() if k != "ENV_NAME"}
        with patch.dict(os.environ, filtered_env, clear=True):
            config: DefaultConfig = DefaultConfig()

        assert config.ENV_NAME == "template tkinter python"
