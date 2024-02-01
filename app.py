from textual.app import App, ComposeResult
from screens import Login
from textual.widgets import Static


class TelegramApp(App):
    BINDINGS = [
        ("q", "quit", "Quit app"),
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        yield Static("Loading...")

    def on_mount(self) -> None:
        self.install_screen(Login(), name="login")
        # self.install_screen(BaseLoginModal("You code"), name="code_modal")
        self.push_screen("login", self.login_screen)

    def login_screen(self, phone):
        print(phone)


if __name__ == "__main__":
    app = TelegramApp()
    app.run()
