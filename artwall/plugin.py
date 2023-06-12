from typing import Optional

from dict_deep import deep_get, deep_set
from mkdocs.config.base import Config
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from path import Path

icon_dir = Path(__file__).parent / ".overrides" / ".icons"


class ArtwallPlugin(BasePlugin):
    def on_config(self, config: MkDocsConfig) -> Optional[Config]:
        config.theme.dirs.insert(1, icon_dir.parent)

        key = "mdx_configs|pymdownx.emoji|options|custom_icons"
        custom_icons = (deep_get(config, key, sep="|") or []) + [str(icon_dir)]
        deep_set(config, key, custom_icons, sep="|")

        return config
