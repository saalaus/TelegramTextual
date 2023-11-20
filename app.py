from textual.app import App
from screens import Login


class TelegramApp(App):
    BINDINGS = [
        ("q", "quit", "Quit app"),
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def on_mount(self) -> None:
        self.install_screen(Login(), name="login")
        self.push_screen("login")



if __name__ == "__main__":
    app = TelegramApp()
    app.run()
