from textual import events
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label, Input, Select, DataTable

from globalvar import generalVar


class ADDDATA(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Label("输入发票数据", id="Title")
        yield Horizontal(
            Vertical(
                Label("接收时间"),
                Label("发票代码"),
                Label("类别"),
                Label("公司"),
                Label("状态"),
                Label("发票号"),
                Label("金额"),
                Label("来源"),
                classes="label",
            ),
            Vertical(
                Label(generalVar.DATENOW),
                Input(placeholder="发票代码"),
                Input(placeholder="类别"),
                Input(placeholder="公司"),
                Select(generalVar.STATEOP, value="未预约"),
                Input(placeholder="发票号"),
                Input(placeholder="金额"),
                Input(placeholder="来源"),
                classes="input",
            ),
        )
        yield DataTable()
        yield Button(name="Append", label="添加")

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("时间", "发票代码", "类别", "公司", "状态", "发票号", "金额", "来源")

    def on_button_press(self, event: Button.Pressed) -> None:
        if event.button.name == "Append":
            newInvoice = []
            newInvoice.append(generalVar.DATENOW)
