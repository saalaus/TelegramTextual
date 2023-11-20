from textual.screen import Screen
from textual.widgets import Input
from widgets import Button
from textual.app import ComposeResult


class Login(Screen):
    CSS_PATH = "login.tcss"

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Login")
        yield Input(placeholder="Password", password=True)
        yield Button("login", style="blue")
