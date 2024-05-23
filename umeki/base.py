import dearpygui.dearpygui as dpg


class Window:
    def __init__(self):
        with dpg.stage() as self._stage:
            with dpg.window() as self.id:
                self._setup_window()

    def _setup_window(self):
        pass

    def start(self):
        dpg.unstage(self._stage)
