from rich.text import TextType
from textual.widgets import Button as DefaultButton
from textual.reactive import reactive
from typing import Literal
from utils.css import get_component_css

ButtonVariant = Literal["default", "red", "blue", "yellow", "green"]


class Button(DefaultButton):
    DEFAULT_CSS = get_component_css("button")

    style = reactive("default")

    def __init__(
        self,
        label: TextType | None = None,
        style: ButtonVariant = "default",
        *,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
    ):
        super().__init__(label, name=name, id=id, classes=classes, disabled=disabled)
        self.style = style

    def watch_style(self, old_style: str, style: str):
        self.remove_class(f"-{old_style}")
        self.add_class(f"-{style}")
