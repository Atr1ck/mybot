from nonebot.plugin import PluginMetadata

from .config import Config
from . import pjsk as __main__

__plugin_meta__ = PluginMetadata(
    name="pjsk-helper",
    description="",
    usage="",

    type="application",

    homepage="https://github.com/Atr1ck/nonebot-plugin-pjsk-helper",
    
    config=Config,
)


