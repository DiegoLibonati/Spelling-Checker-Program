from tkinter import CENTER

import pytest

from src.ui.styles import Styles


class TestStyles:
    @pytest.mark.parametrize(
        "color_attr",
        [
            "PRIMARY_COLOR",
            "SECONDARY_COLOR",
            "WHITE_COLOR",
            "BLACK_COLOR",
        ],
    )
    def test_color_is_valid_hex(self, color_attr: str) -> None:
        color: str = getattr(Styles, color_attr)

        assert color.startswith("#")
        assert len(color) == 7

    def test_font_roboto_name(self) -> None:
        assert Styles.FONT_ROBOTO == "Roboto"

    @pytest.mark.parametrize(
        "font_attr,size",
        [
            ("FONT_ROBOTO_12", "12"),
            ("FONT_ROBOTO_13", "13"),
            ("FONT_ROBOTO_15", "15"),
            ("FONT_ROBOTO_20", "20"),
        ],
    )
    def test_font_contains_size(self, font_attr: str, size: str) -> None:
        assert size in getattr(Styles, font_attr)

    def test_anchor_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER
