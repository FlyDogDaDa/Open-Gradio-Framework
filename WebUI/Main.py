import gradio as gr
import os
from importlib import import_module
import json


# 定義主頁面
class MainPage(gr.TabbedInterface):
    _pages: dict[str : gr.Blocks] = {}

    def __init__(self):
        self._load_pages()
        v = self._pages.values()
        super().__init__(v, self._pages.keys())

    def reload(self):
        """
        重新載入頁面
        """
        self._pages.clear()
        self._load_pages()
        self._render()

    def _load_pages(self):
        """
        載入分頁頁面
        """
        for filename in os.listdir("WebUI/gradio_pages"):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = import_module(f"gradio_pages.{module_name}")
                try:
                    blocks = getattr(module, module_name)
                except AttributeError as e:
                    raise SyntaxError(
                        f'{e}\n\nThere is no renderable object with the same file name.\nPossible Debug Methods:It can be fixed by with gr.Blocks(title="your page") as [your_module_nam]: method.'
                    )

                self._pages[module_name] = blocks

    def _render(self):
        """
        渲染主頁面
        """
        self.clear()
        # for name, page in self._pages.items():
        #     self.add(gr.Tab(name, page.render()))
        self.render()


if __name__ == "__main__":
    # 啟動應用程式
    with open("Launch_setting.json", "r") as file:
        launch_setting = json.load(file.read())
    MainPage().launch(*launch_setting)
