from typing import Optional

from mkdocs.config.base import MkDocsConfig, Config
from mkdocs.plugins import BasePlugin


class ArtwallPlugin(BasePlugin):
    def on_config(self, config: MkDocsConfig) -> Optional[Config]:
        config.theme.dirs.append(".overrides")
        return config
