from typing import Union

import dearpygui.dearpygui as dpg

from umeki.base import Window


class BaseData(Window):
    def __init__(self, name: str):
        self.name = name
        self.plot: Union[int, str, None] = None
        self.menubar: Union[int, str, None] = None
        super().__init__()

    def _setup_window(self):
        dpg.set_item_label(self.id, f"Data: {self.name}")
        with dpg.plot(width=-1) as self.plot: pass
        with dpg.menu_bar() as self.menubar: pass
