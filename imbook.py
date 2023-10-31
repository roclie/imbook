from textual import events
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Markdown, Label, Input, Select, DataTable

from globalvar import generalVar
from adddata import ADDDATA


class ImbookApp(App):
    def compose(self) -> ComposeResult:
        yield Label("报销记录", id="Title")
        yield Markdown(generalVar.TITLE_MARKDOWN)
        yield Horizontal(
            Button(name="Add", label="添加发票"),
            Button(name="Change", label="修改发票状态"),
            Button(name="Search", label="查找发票"),
            Button(name="Exit", label="退出"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.name == "Add":
            self.push_screen(ADDDATA())
        if event.button.name == "Exit":
            self.exit()


if __name__ == "__main__":
    app = ImbookApp(css_path="imbook.tcss")
    app.run()
