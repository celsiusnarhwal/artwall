from typing import Optional

from mkdocs.config.base import Config
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin


class ArtwallPlugin(BasePlugin):
    def on_config(self, config: MkDocsConfig) -> Optional[Config]:
        config.theme.dirs.append(".overrides")
        return config
