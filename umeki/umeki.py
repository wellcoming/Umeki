import dearpygui.dearpygui as dpg

from umeki.base import Window


class Umeki(Window):
    def __init__(self):
        with dpg.font_registry():
            dpg.bind_font(dpg.add_font("umeki/resources/fonts/JetBrainsMono-Regular.ttf", 20))

        super().__init__()
        dpg.set_primary_window(self.id, True)

    def setup_viewport(self):
        dpg.create_viewport(
            title=self.__class__.__name__,
            width=800,
            height=600
        )
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def _setup_window(self):
        dpg.set_item_label(self.id, self.__class__.__name__)
        with dpg.menu_bar():
            dpg.add_menu_item(label="Open")
