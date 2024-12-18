from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Maishiy Texnika",callback_data="maishiy"),InlineKeyboardButton(text="Kiyimlar",callback_data="kiyim"),InlineKeyboardButton(text="Aloqa",callback_data="aloqa")],
        [InlineKeyboardButton(text='ortga',callback_data='ortga')]
    ]
)
maishiy1=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Konditsioner🗣",callback_data="kond🗣"),InlineKeyboardButton(text="Televizor",callback_data="tv")],
        [InlineKeyboardButton(text="Changgitgich🗣",callback_data="chang🗣"),InlineKeyboardButton(text="Mikravolnovka",callback_data="mikra")],
        [InlineKeyboardButton(text="Kirmoshina🗣",callback_data="kir🗣"),InlineKeyboardButton(text="Myasarubka",callback_data="myasa")],
    ]
)




kiyim=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Erkaklarga",callback_data="er"),InlineKeyboardButton(text="Ayolarga",callback_data="ay"),InlineKeyboardButton(text="Bolalarga",callback_data="miti")],
    ]
)



aloqa=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="+998999676861",callback_data="1"),InlineKeyboardButton(text="+998991511117",callback_data="4")],
        [InlineKeyboardButton(text="+998996554551",callback_data="2"),InlineKeyboardButton(text="+998996654555",callback_data="5")],
        [InlineKeyboardButton(text="+998995255142",callback_data="3"),InlineKeyboardButton(text="+998254545551",callback_data="6")]
    ]
)





#ISHLAMIN DURIBDI  . . .