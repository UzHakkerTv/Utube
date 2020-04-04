
class Messages:

    START_MSG = "🙋Salom {}.\n\nMen Youtube-ning yuklovchisiman. ☺️Siz menga avtorizatsiyadan o'tgach, youtube-ga istalgan telegram-video yuklash uchun mendan foydalanishingiz mumkin.\nQanday Yuklash Haqida Malumot /help.\n\nRaxmat."

    HELP_MSG = [
        ".",
        "Salom.\n\nAvvalo birinchi narsa. Siz shuni bilishingiz kerakki, youtube har bir yuklangan har bir videoni qayta ishlaydi va uning AI, agar u boshqa kanaldan ko'chirib olingan kontent yuklanganidan xabar topsa va videoni nashr eta olmasangiz, u mualliflik huquqi uchun videoni yopiladi. Agarda 3 marta ogohlantirish olsangiz Kanalingiz yopiladi.\n\nQanday ishlashimni bilish uchun barcha sahifalarni o'qing.",

        "**Keling, qanday ishlashimni bilib olaylik.**\n\n**1-Qadam:** __Sizga youtube kanalingizga yuklashga ijozat berasiz. Bu haqida keyingi sahifalarda batafsilroq.__\n\n**2-qadam:** __Siz har qanday Telegram videosini menga yuborasiz.__\n\n**3-qadam:** __📍Yuborilgan vedioga Reply qilib /upload so'zini yozasiz.__\n\n**4-qadam:** __Faylni masofadan turib va Youtube kanalingizga yuklab berdik__\n\n**5-qadam:** __Kanalingizga yuklangan vedio manzilini yuboraman__",

        "**Youtube Kanal Yarating**\n\nAgar Youtube kanaliga ega bo'lmasangiz, meni ishlatishda hech qanday ma'no yo'q. Shunday qilib, uni yaratish uchun quyida keltirilgan amallarni bajaring.\n\n**1-qadam:** __Kompyuterga yoki mobil qurilmadan YouTube-ga kiring.__\n\n**2-qadam:** __Videoni yuklash, sharh yuborish yoki pleylist yaratish kabi kanallarni talab qiladigan barcha amallarni bajaring.__\n\n**3-qadam:** __Agar sizda hali kanal yo'q bo'lsa, siz kanal yaratish haqida ko'rsatma olasiz.__\n\n**4-qadam:** __Tafsilotlarni tekshiring va yangi kanalingizni yaratish uchun tasdiqlang.__",

        "**YouTube hisobingizni tasdiqlang**\n\nYoutube spam va suiiste'molni juda jiddiy qabul qiladi. Shuning uchun sizdan Youtube hisobingizni tasdiqlash so'raladi. Hisobingizni tasdiqlaganingizdan so'ng, siz 15 daqiqadan ko'proq vaqt davomida video yuklay olasiz. Agar siz hisobingizni tasdiqlamagan bo'lsangiz, 15 daqiqadan ko'proq vaqt yuklangan har bir video o'chiriladi.\n[Youtube hisobingizni bu erda tasdiqlang.](http://www.youtube.com/verify)",

        "**Endi avtorizatsiya qilish.**\n\nSizga Youtube-dagi hisob qaydnomangizga videolarni yuklash huquqini berishingiz kerak. Berilgan havolani ochib, kodni ko'chirib olish huquqini beradigan. Bu erga qaytib kelib, /authorise kopiyalangan kodni tering va yuboring.\n\n**Qo'rqma!**\nMen hech qanday xaker yoki odamlarning hayotiga aralashishni istamaydigan odam emasman. Men shaxsiy hayotimni hurmat qilaman. Men yordam so'rab kelganlarga yordam berish uchun keldim. Agar men hacker bo'lganimda, men bu erda Telegram Bots yozish uchun o'tirmayman."
    ]

    NOT_A_REPLY_MSG = "Iltimos, video faylga reply qilib yoizng."

    NOT_A_MEDIA_MSG = "Media fayl topilmadi. "+NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "Bu yaroqli media emas"

    PROCESSING = "Yuklanoqda....."

    NOT_AUTHENTICATED_MSG = "Siz biron bir qayd yozuviga video yuklash uchun meni tasdiqlamadingiz. autentifikatsiya qilish /help deb yozing."

    NO_AUTH_CODE_MSG = "Hech qanday kod yo'q. Iltimos, kodni ko'rsating"

    AUTH_SUCCESS_MSG = "Tabriklayman, siz muvaffaqiyatli Youtube-ga yuklash uchun tasdiqladingiz.\nMuvaffaqiyatli yuklash!"

    AUTH_FAILED_MSG = "Haqiqiylikni tekshirib bo'lmadi\nTafsilotlar:{}"
