from nonebot.plugin import PluginMetadata

from .config import Config
from . import pjsk as __main__

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="pjsk-helper",
    description="基于 Nonebot2 的 Project Sekai 助手",
    usage="使用命令 pjsk help 查看帮助",

    type="application",

    homepage="https://github.com/Atr1ck/nonebot-plugin-pjsk-helper",
    
    config=Config,
    extra={
        "version": __version__,
        "author": "Atr1ck <3126670240@qq.com"
    }
)
