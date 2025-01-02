import os
import logging
import yaml

from telethon import TelegramClient
from telethon.sessions import StringSession


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
API_ID = int(os.getenv('API_ID', CONFIG['22118129']))
API_HASH = os.getenv('API_HASH', CONFIG['43c66e3314921552d9330a4b05b18800'])
DUMP_ID = os.getenv('DUMP_ID', CONFIG['-1002399310545'])
STRING_SESSION = os.getenv('STRING_SESSION', CONFIG['1BVtsOLYBu2X3PDA-KbYg0iLlsiZpCYUG6RWdVRDcELho-hcQul4MGPLmWoh7X9nP5l_FvTw8BYDe1j7ESy6p_p36M1X8kDTQdTeFKS9ooHjJmutSbJDgnlk_iDxDyz-9h11NeIcbtS-5VQ4LoDJ2Eur6_5qRrhu_5u54-fx115ykWAaUBXQu8vhK4Jqimw41y-OgExyK1zvhG6RxGRVij0CChrj6cellzTVQO5ZNffexVJuGBsWqF9Phyr6c2ecCb7ifqBK7WCFCoFyhV2XwDAAP0va3FclJOoURncUbfSvt5Wnto3TKqHfwsJS9ipQBHQ2LapE-w2dX-4e-I64c17Il7F1SABw='])

Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')
