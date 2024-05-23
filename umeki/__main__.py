import dearpygui.dearpygui as dpg

from umeki.data.base import BaseData
from .umeki import Umeki

if __name__ == '__main__':
    dpg.create_context()

    umeki = Umeki()
    umeki.start()
    dpg.show_item_registry()

    test = BaseData("testdata")
    test.start()

    umeki.setup_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
