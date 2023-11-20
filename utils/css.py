from pathlib import Path

DEFAULT_STYLES_PATH = Path("styles")
COMPONENT_CSS_FOLDER = DEFAULT_STYLES_PATH / "components"
SCREENS_CSS_FOLDER = DEFAULT_STYLES_PATH / "screens"


def get_component_css(component: str, extension="tcss") -> str:
    return (COMPONENT_CSS_FOLDER / f"{component}.{extension}").read_text()


def get_screen_css(screen: str, extension="tcss"):
    return (SCREENS_CSS_FOLDER / f"{screen}.{extension}").read_text()
