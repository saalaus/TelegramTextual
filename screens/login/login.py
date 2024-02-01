from rich.console import RenderableType
from telethon import TelegramClient
from textual import on, work
from textual.app import ComposeResult
from textual.screen import ModalScreen, Screen
from textual.widgets import Input, Static

from widgets import Button

api_id = 29118466
api_hash = "3a03ee89d41c60ad26d82457f1add090"

client = TelegramClient("anon", api_id, api_hash)


class GetCodeModal(ModalScreen):
    def __init__(self, title: RenderableType) -> None:
        super().__init__()

        self.title: RenderableType = title

    def compose(self) -> ComposeResult:
        yield Static(self.title)
        yield Input(placeholder="Your code", id="text")
        yield Button("Submit", id="submit_code")

    @on(Button.Pressed, "#submit_code")
    def send_code(self) -> None:
        value = self.query_one("#text").value
        self.dismiss(value)

    def key_escape(self):
        self.dismiss(result=False)


class Login(Screen):
    CSS_PATH = "login.tcss"

    def __init__(
        self,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
    ) -> None:
        super().__init__(name, id, classes)

        self.app.install_screen(
            GetCodeModal("Enter the code you just received:"),
            name="code_modal",
        )
        self.app.install_screen(
            GetCodeModal(
                "Two step verification is enabled."
                "Please enter your password:",
            ),
            name="password_modal",
        )

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Phone Number")
        yield Button("login", style="blue", id="login")

    @on(Button.Pressed, "#login")
    def login_button(self, event: Button.Pressed) -> None:
        print(event)
        self.app.push_screen("password_modal", self.get_code)
        # self.login()

    def get_code(self, code: str | bool):
        print(code)

    @work
    async def login(self):
        print(await client.connect())
        print(await client.sign_in("89995620938"))
        # print(await client.get_me())
