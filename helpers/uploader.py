from youtube_upload.auth import GoogleAuth
from youtube_upload.youtube import Youtube

from config import Config

from translations import Messages as tr

import os
import time
import traceback

class Uploader:

    def __init__(self, file, title=None):
        
        self.file = file
        
        self.title = title


    async def start(self, progress=None, *args):
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message


    async def _upload(self):
        try:

            auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
            
            if not os.path.isfile(Config.CRED_FILE):
                self.status = False
                
                self.message = "Uzur Avtarizatsiyadan o'ting /help"
                
                return

            auth.LoadCredentialsFile(Config.CRED_FILE)

            google = auth.authorize()

            properties = dict(
                title = self.title if self.title else os.path.basename(self.file),
                description = "✅ Ijtimoiy Tarmoqlarim
➥ Telegram: https://t.me/UniversalVlog
➥ Instagram: https://www.instagram.com/OTASH_Arts
➥ Instagram: https://www.instagram.com/UzHakkerTv
==========================================
👍Layk tugmasini bosishni unutmang !
🔥Ajoyib kommentlaringizni qoldiring...
==========================================
▶️ Youtube kanalingizga sifatli banner, avatar, oblojka va yana turli xildagi dizaynlar kerakmi ? 
✉️ Unda men bilan bog'laning: 
https://t.me/OTASH_Arts
==========================================


GTA, GamePlay, Pubg, Stars War, Pubg lite, Pubg Mobile, FreeFire, Cod Mobile, Call of Duty, Clash of clans, Forza Horizon, Fall Guys, Marvel, Iron man, No copyright GamePlay, Jump Force, BattleField, Tekken, Mortal Combat, Counter Strike, CS GO and Others.",
                category = 27,
                privacyStatus = 'Private'
            )

            youtube = Youtube(google)

            self.start_time = time.time()
            self.last_time = self.start_time

            r = await youtube.upload_video(video = self.file, properties = properties)

            self.status = True
            self.message = f"Yuklandi. https://youtu. be/{r['id']}"
        except Exception as e:
            traceback.print_exc()
            self.status = False
            self.message = f"Yuklash Jarayonida Xatolik.\nXatolik haqida: {e}"
        return

