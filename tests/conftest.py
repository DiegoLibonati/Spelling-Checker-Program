import tkinter as tk
from collections.abc import Generator

import pytest


@pytest.fixture(scope="session")
def root() -> Generator[tk.Tk, None, None]:
    instance: tk.Tk = tk.Tk()
    instance.withdraw()
    yield instance
    instance.destroy()
