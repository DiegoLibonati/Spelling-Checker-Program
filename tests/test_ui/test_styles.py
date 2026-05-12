from tkinter import CENTER

import pytest

from src.ui.styles import Styles


@pytest.mark.unit
class TestStyles:
    def test_primary_color_is_hex_string(self) -> None:
        assert Styles.PRIMARY_COLOR.startswith("#")
        assert len(Styles.PRIMARY_COLOR) == 7

    def test_secondary_color_is_hex_string(self) -> None:
        assert Styles.SECONDARY_COLOR.startswith("#")
        assert len(Styles.SECONDARY_COLOR) == 7

    def test_white_color_is_hex_string(self) -> None:
        assert Styles.WHITE_COLOR.startswith("#")
        assert len(Styles.WHITE_COLOR) == 7

    def test_black_color_is_hex_string(self) -> None:
        assert Styles.BLACK_COLOR.startswith("#")
        assert len(Styles.BLACK_COLOR) == 7

    def test_font_roboto_contains_roboto(self) -> None:
        assert "Roboto" in Styles.FONT_ROBOTO

    def test_font_roboto_12_contains_size(self) -> None:
        assert "12" in Styles.FONT_ROBOTO_12

    def test_font_roboto_13_contains_size(self) -> None:
        assert "13" in Styles.FONT_ROBOTO_13

    def test_font_roboto_15_contains_size(self) -> None:
        assert "15" in Styles.FONT_ROBOTO_15

    def test_font_roboto_20_contains_size(self) -> None:
        assert "20" in Styles.FONT_ROBOTO_20

    def test_anchor_center_equals_tkinter_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER
