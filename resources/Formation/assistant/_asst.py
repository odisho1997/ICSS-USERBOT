#  ICSS - USERBOT
#  TELE - @NIIIN2
#  OWNER - KIMO

import time
from datetime import datetime
from userbot.Config import Config
from userbot.plugins import mention

# Kimo
K = "https://t.me/rruuurr"
D = "** ⌔∮ مطور بوت اكسس**"

OWNER_ID = Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME if Config.ALIVE_NAME else "@rruuurr"

# for OWNER_ID
OId = Config.OWNER_ID

# for time
StartTime = time.time()

# start-other disabled
startotherdis = f"**⌔∮ اهلا بك انا مساعد {mention} سعيد برؤيتك هنا**"

# start-other enabled
if Config.TOSH_START is None:
    MSSG = f"**⌔∮ اهلا بك انا مساعد {mention} تستطيع التواصل معه من خلالي**"
else:
    MSSG = Config.TOSH_START
startotherena = MSSG

# start-owner
startowner = f"** ⌔∮ اهلا بك مجدداً {ALIVE_NAME}. اختر احد الخيارات الاتيه:**"

# for ping
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
# Ping Message
Ping = "**⌔∮ سرعة الاستجابه** `{}`\n**⌔∮ مدة التشغيل** `{}`"


# Boys name1 - اسماء الشباب الاولى
Boysna1 = (
    "-𓆩 𝗔𝗠𝗔𝗔𝗥.𖤐𓆪\n"
    "-𓆩 𝗠𝗔𝗟𝗘𝗞.𖤐𓆪\n"
    "-𓆩 𝗔𝗬𝗔𝗗.𖤐𓆪\n"
    "-𓆩 𝗥𝗔𝗙𝗜𝗗.𖤐𓆪\n"
    "-𓆩 𝗦𝗕𝗔𝗛.𖤐𓆪\n"
    "-𓆩 𝗔𝗕𝗔𝗦.𖤐𓆪\n"
    "-𓆩 𝗛𝗔𝗕𝗜𝗕.𖤐𓆪\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "⌯『𝐀𝐋𝐈』𖤍᭄𓄹\n"
    "⌯『𝐋𝐁𝐍𝐀 』𖤍᭄𓄹\n"
    "⌯『𝐀𝐒𝐄𝐄𝐋』𖤍᭄𓄹\n"
    "⌯『𝐒𝐇𝐄𝐑𝐄𝐍』𖤍᭄𓄹\n"
    "⌯『𝐌𝐔𝐒𝐓𝐀𝐅𝐀』𖤍᭄𓄹𓆩\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "𓆩 𝒌𝒉𝒂𝒍𝒆𝒅 𓆪 🖤.\n"
    "𓆩 𝑶𝒎𝒂𝒓 𓆪 🖤.\n"
    "𓆩 𝑯𝒂𝒛𝒂𝒎 𓆪 🖤.\n"
    "𓆩 𝑯𝒂𝒕𝒂𝒎 𓆪 🖤.\n"
    "𓆩 𝑶𝒔𝒂𝒎𝒂 𓆪 🖤.\n"
    "𓆩 𝑯𝒂𝒅𝒐 𓆪 🖤.\n"
    "𓆩 𝑯𝒂𝒊𝒅𝒂𝒓 𓆪 🖤.\n"
    "𓆩 𝑮𝒉𝒂𝒍𝒆𝒃 𓆪 🖤.\n"
    "𓆩 𝑨𝒌𝒓𝒂𝒎 𓆪 🖤.\n"
    "𓆩 𝑯𝒂𝒔𝒐𝒏𝒆 𓆪 🖤.\n"
    "𓆩 𝑯𝒂𝒎𝒐𝒅𝒊 𓆪 🖤.\n"
    "𓆩 𝒗𝒊𝒓𝒐𝒔 𓆪 🖤.\n"
    "𓆩 𝑶𝒓𝒂𝒔 𓆪 🖤.\n"
    "𓆩 𝑺𝒂𝒍𝒊𝒉 𓆪 🖤.\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "「𝘔𝘦𝘳𝘰 𐃣.\n"
    "「𝘋𝘢𝘦𝘷 𐃣.\n"
    "「𝘌𝘷𝘢 𐃣.\n"
    "「𝘋𝘮𝘢𝘳 𐃣.\n"
    "「𝘑𝘮𝘳𝘢 𐃣."
)

# Boys name2 - اسماء الشباب الثانيه
Boysna2 = (
    "𓆩 𝑨𝒃𝒐𝒅𝒆 𓆪 🖤.\n"
    "𓆩 𝑴𝒖𝒔𝒕𝒂𝒇𝒂 𓆪 🖤.\n"
    "𓆩 𝑴𝒂𝒉𝒅𝒊 𓆪 🖤.\n"
    "𓆩 𝑸𝒂𝒔𝒂𝒎 𓆪 🖤.\n"
    "𓆩 𝑹𝒂𝒔𝒉𝒂𝒅 𓆪 🖤.\n"
    "𓆩 𝑨𝒅𝒏𝒂𝒏 𓆪 🖤.\n"
    "𓆩 𝑺𝒂𝒓𝒎𝒂𝒅 𓆪 🖤.\n"
    "𓆩 𝑯𝒂𝒔𝒂𝒏 𓆪 🖤.\n"
    "𓆩 𝑵𝒂𝒛𝒂𝒓 𓆪 🖤.\n"
    "𓆩 𝑴𝒐𝒉𝒂𝒎𝒆𝒅 𓆪 🖤.\n"
    "𓆩 𝑲𝒂𝒓𝒂𝒓 𓆪 🖤.\n"
    "𓆩 𝑨𝒉𝒎𝒆𝒅 𓆪 🖤.\n"
    "𓆩 𝑨𝒅𝒂𝒎 𓆪 🖤.\n"
    "𓆩 𝑯𝒖𝒔𝒔𝒊𝒆𝒏 𓆪 🖤.\n"
    "𓆩 𝑨𝒍𝒐𝒔𝒉 𓆪 🖤.\n"
    "𓆩 𝑹𝒂𝒔𝒐𝒖𝒍 𓆪 🖤.\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "𓆩 𝚁𝙾𝙽𝙴 𓆪  🇺🇸.\n"
    "𓆩 𝙴𝚅𝙰𝙽 𓆪  🇺🇸.\n"
    "𓆩 𝙹𝙰𝙺 𓆪  🇺🇸.\n"
    "𓆩 𝚃𝙾𝙼 𓆪  🇺🇸.\n"
    "𓆩 𝙹𝙾𝙽 𓆪  🇺🇸.\n"
    "𓆩 𝙰𝙷𝙼𝙸𝙳 𓆪🎗️ ꙰\n"
    "𓆩 𝙰𝙻𝙾𝚂𝙷 𓆪🎗️ ꙰\n"
    "𓆩 𝚂𝙰𝙹𝙰𝙳 𓆪🎗️ ꙰\n"
    "𓆩 𝚂𝙱𝙰𝙰𝙷 𓆪🎗️ ꙰\n"
    "𓆩 𝙷𝙰𝙸𝚃𝙷𝙼 𓆪🎗️ ꙰\n"
    "𓆩 𝙷𝚄𝚂𝚂𝙴𝙸𝙽 𓆪🎗️ ꙰\n"
    "𓆩 𝙼𝚄𝙷𝙰𝙼𝙼𝙰𝙳 𓆪🎗️ ꙰\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "- 𝙎 𝘼 𝙄 𝙆 𝙊 : 🇺🇸Ꮠ\n"
    "- 𝙈 𝘼 𝙍 𝘾 𝙊 : 🇺🇸Ꮠ\n"
    "- 𝙎 𝘼 𝙉 𝙔 : 🇺🇸Ꮠ\n"
    "- 𝙆 𝙄 𝙈 𝙊 : 🇺🇸Ꮠ\n"
    "- 𝙏 𝙃 𝘼 𝙈 𝙀 𝙍 : 🇺🇸Ꮠ\n"
    "- 𝘽 𝘼 𝙉 : 🇺🇸Ꮠ\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "𓂐 𝙄𝘾𝙎𝙎 𖠛 .\n"
    "𓂐 𝘼𝙈𝙀𝙍 𖠛 .\n"
    "𓂐 𝙆𝘼𝙈𝙀𝙇 𖠛.\n"
    "𓂐 𝙃𝙈𝙊 𖠛 .\n"
    "𓂐 𝙅𝙊𝙅 𖠛 ."
)

# Girls name1 - اسماء البنات الاولى
Girlan1 = (
    "- 𝑎𝑠𝑜 𐇲.\n"
    "- 𝑎𝑛𝑜 𐇲.\n"
    "- 𝑡𝑏𝑜 𐇲.\n"
    "- 𝑡𝑛𝑜 𐇲.\n"
    "- 𝒛𝒉𝒐 𐇲.\n"
    "- 𝒛𝒏𝒐 𐇲.\n"
    "- 𝒉𝒅𝒐 𐇲.\n"
    "- 𝒉𝒃𝒐 𐇲.\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "𖥻 𓆩 𝙍𝙚𝙚𝙢 𓆪،𖤍\n"
    "𖥻 𓆩 𝙕𝙖𝙮𝙣𝙖𝙗 𓆪،𖤍\n"
    "𖥻 𓆩 𝙁𝙖𝙩𝙚𝙢𝙖 𓆪،𖤍\n"
    "𖥻 𓆩 𝙍𝙖𝙤𝙖𝙣 𓆪،𖤍\n"
    "𖥻 𓆩 𝙅𝙖𝙣𝙖𝙩 𓆪،𖤍\n"
    "𖥻 𓆩 𝙕𝙖𝙝𝙧𝙖 𓆪،𖤍\n"
    "𖥻 𓆩 𝙉𝙤𝙨𝙖 𓆪،𖤍\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "- 𝙎 𝘼 𝙉 𝘿 𝙍 𝙄 𝙇 𝘼 : 🇺🇸Ꮠ\n"
    "- 𝙍 𝘽 𝘼 𝙉 𝙕 𝙇 : 🇺🇸Ꮠ\n"
    "- 𝙎 𝘼 𝙇 𝙇 𝙔 : 🇺🇸Ꮠ\n"
    "- 𝙆 𝘼 𝘿 𝙄 𝘼 : 🇺🇸Ꮠ\n"
    "- 𝙏 𝙊 𝙏 𝘼 : 🇺🇸Ꮠ\n"
    "- 𝘽 𝘼 𝙉 𝙀 𝙉 : 🇺🇸Ꮠ\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "𓄼 𝘚 𝘖 𝘚 ༆ 𓄹.\n"
    "𓄼 𝘛 𝘖 𝘛 ༆ 𓄹.\n"
    "𓄼 𝘕 𝘖 𝘕 ༆ 𓄹.\n"
    "𓄼 𝘍 𝘖 𝘍 ༆ 𓄹.\n"
    "𓄼 𝘑 𝘖 𝘑  ༆ 𓄹.\n"
    "𓄼 𝘒 𝘖 𝘒 ༆ 𓄹.\n"
    "𓄼 𝘛 𝘕 𝘖 ༆ 𓄹.\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "⌯ ˹ʀɴᴏѕʜ˼❀ .\n"
    "⌯ ˹ᴍᴇᴍᴏ˼❀ .\n"
    "⌯ ˹ʜᴏʀᴇ˼ ❀ .\n"
    "⌯ ˹ѕᴀʀᴀ˼ ❀ .\n"
    "⌯ ˹ѕᴏѕ˼  ❀ .\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "𓂐 𝙀𝙇𝙄𝙕𝘼𝘽𝙀𝙏𝙃 𖠛.\n"
    "𓂐 𝘼𝙈𝘼𝙉𝘿𝘼 𖠛 .\n"
    "𓂐 𝘼𝙉𝘿𝙍𝙀𝘼 𖠛 .\n"
    "𓂐 𝙀𝙈𝙀𝙇𝙔 𖠛 .\n"
    "𓂐 𝙀𝙍𝙄𝙆𝘼 𖠛 .\n"
    "𓂐 𝙀𝙑𝘼 𖠛 .\n"
    "𓂐 𝘼𝙈𝙔  𖠛 ."
)

# Girls name2 - اسماء البنات الثانيه
Girlan2 = (
    "『𓆩 𝚃𝙱𝙾 𓆪』𐂂𓄹\n"
    "『𓆩 𝙷𝙽𝙾 𓆪』 𐂂𓄹\n"
    "『𓆩 𝙰𝙽𝙾 𓆪』𐂂𓄹\n"
    "『𓆩 𝙰𝚉𝙾 𓆪』𐂂𓄹\n"
    "『𓆩 𝙳𝙷𝙾 𓆪』𐂂𓄹\n"
    "『𓆩 𝙰𝚂𝙾 𓆪』𐂂𓄹\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "•˹𝙻𝚈𝙽𝙽˼⛈💞.\n"
    "•˹𝙽𝙾𝙾𝚁˼⛈💞.\n"
    "•˹𝚂𝙰𝙼𝙰𝚁˼⛈💞.\n"
    "•˹𝙽𝙾𝚁𝙷𝙰𝙽˼⛈💞.\n"
    "•˹𝙺𝙰𝚆𝚃𝙷𝙴𝚁˼⛈💞.\n"
    "•˹𝚃𝙰𝙱𝙰𝚁𝙰𝚀˼⛈💞.\n"
    "•˹𝚂𝙰𝙱𝚁𝙴𝙴𝙽˼⛈💞.\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "•𝙼𝙰𝚁𝚈𝙰𝙼⋆  🧚🏻‍♀♥️ .\n"
    "•𝙱𝙰𝚃𝙾𝙻⋆ 🧚🏻‍♀♥️ .\n"
    "•𝙰𝙼𝙾𝙽⋆  🧚🏻‍♀♥️ .\n"
    "•𝚉𝙰𝙽𝙾𝚂𝙷𝙰⋆ 🧚🏻‍♀♥️ .\n"
    "•𝚉𝙰𝙷𝚁𝙰𝙰⋆  🧚🏻‍♀♥️ .\n"
    "•𝙱𝙰𝙽𝙴𝙽⋆ 🧚🏻‍♀♥️ .\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "• мαяɪαм🚴🏽‍♀️💞..\n"
    "• zαyиαв🚴🏽‍♀️💞..\n"
    "• sαяαн🚴🏽‍♀️💞..\n"
    "• zαняα🚴🏽‍♀️💞..\n"
    "• sнαɪмαα🚴🏽‍♀️💞..\n"
    "┉ ┉ ┉ ┉ ┉\n"
    "𝄇 𝗦𝗢𝗦𝗢𝆹𝅥𝅮 𝄆💘\n"
    "𝄇 𝗡𝗢𝗡𝗔𝆹𝅥𝅮 𝄆💘\n"
    "𝄇 𝗝𝗢𝗝𝗔 𝆹𝅥𝅮  𝄆💘\n"
    "𝄇 𝗠𝗘𝗠𝗔𝆹𝅥𝅮𝄆💘\n"
    "𝄇 𝗞𝗢𝗞𝗔𝆹𝅥𝅮 𝄆💘"
)

# Pio1 - البايو 1
ICSPIO1 = (
    "𓋜┊𓆩 ➝  ˛⁽🇮🇶₎⇣ 𓆪\n"
    "𓋜┊𓆩  𓆪\n"
    "𓋜┊𓆩  𓆪\n"
    "𓋜┊𓆩  𓆪\n"
    "𓋜┊𓆩 ﭑميرۿ ـلآ يُليق بها ﭑلانحنا🍂 𓆪\n"
    "⁞ ωєℓ¢σмє тo му ρяσƒιℓє ⁞"
)

# Pio2 - البايو 2
ICSPIO2 = (
    "🜟 ↬ ᑎᗩᗰE ، • •😌❤️\n"
    "🜟 ↬ ᖴᖇOᗰ ، IRΔQ 🇮🇶\n"
    "🜟 ↬ ᗩGE ، y.o ♥️.\n\n"
    "🧿🍃  .....  🧿🍃."
)

# Pio3 - البايو 3
ICSPIO3 = "☁️ : 🕊\n" "☁️ :   ✨\n" "☁️ :   🤍\n\n" "بريئۃ ۿي، بصورۿ لطيفۃ ڪالاطفال🎀"

# Pio4 - بايو4
ICSPIO4 = "☘️ 💕\n" "☘️ 💕\n" "☘️ 💕\n" "☘️ دمت لي شيئاً جميلاً لا ينتهي💕"

# Pio5 - بايو 5
ICSPIO5 = "𓂅| •\n" "𓂅| •\n" "𓂅| •🖤☁️ .\n" "• 𝙸 𝙻𝙸𝙺𝙴 𝙼𝙾𝚄𝙽𝚃𝙰𝙸𝙼𝚂 𝙽𝙾𝚃 𝙵𝙰𝙻𝙻 ."

# Months - الاشهر
ICSMONT = (
    "-𝒋𝒂𝒏𝒖𝒂𝒓𝒚.💞\n"
    "-𝒇𝒆𝒃𝒓𝒖𝒂𝒓𝒚.💞\n"
    "-𝒎𝒂𝒓𝒄𝒉.💞\n"
    "𝒂𝒑𝒓𝒊𝒍.💞\n"
    "-𝒎𝒂𝒚.💞\n"
    "-𝒋𝒖𝒏𝒆.💞\n"
    "-𝒋𝒖𝒍𝒚.💞\n"
    "-𝒂𝒖𝒈𝒖𝒔𝒕 .💞\n"
    "-𝒔𝒆𝒑𝒕𝒆𝒎𝒃𝒆𝒓 .💞\n"
    "-𝒐𝒄𝒕𝒐𝒃𝒆𝒓.💞\n"
    "-𝒏𝒐𝒗𝒆𝒎𝒃𝒆𝒓.💞\\n"
    "-𝒅𝒆𝒄𝒆𝒎𝒃𝒆𝒓.💞\n"
    "------\n"
    "-𝐒𝐔𝐍𝐃𝐀𝐘.♡\n"
    "-𝐌𝐎𝐍𝐃𝐀𝐘.♡\n"
    "-𝐓𝐔𝐄𝐒𝐃𝐀𝐘.♡\n"
    "-𝐖𝐄𝐃𝐍𝐄𝐒𝐃𝐀𝐘.♡\n"
    "-𝐓𝐇𝐔𝐑𝐒𝐃𝐀𝐘.♡\n"
    "-𝐅𝐑𝐈𝐃𝐀𝐘.♡\n"
    "-𝐒𝐀𝐓𝐔𝐑𝐃𝐀𝐘.♡"
)

# years - المواليد
ICSYEAR = (
    "-₁₉₉₀\n"
    "-₁₉₉₁\n"
    "-₁₉₉₂\n"
    "-₁₉₉₃\n"
    "-₁₉₉₄\n"
    "-₁₉₉₅\n"
    "-₁₉₉₆\n"
    "-₁₉₉₇\n"
    "-₁₉₉₈\n"
    "-₁₉₉₉\n"
    "-₂₀₀₀\n"
    "-₂₀₀₁\n"
    "-₂₀₀₂\n"
    "-₂₀₀₃\n"
    "-₂₀₀₄\n"
    "-₂₀₀₅-\n"
    "-₂₀₀₆\n"
    "-₂₀₀₇"
)

# Channels name - اسماء القنوات
CHANLAN = (
    "𝙁𝙍𝘼𝙉𝘾𝙊𝙄𝙎 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝙆𝙀𝙑𝙄𝙉 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝘼𝙉𝙇𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝘾𝙃𝙄𝙏𝙏𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝙎𝘼𝙑𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝘾𝙃𝙄𝘾𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝘾𝙃𝙄𝘾𝘼𝙂𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝙀𝘾𝙃𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝙔𝘼𝙔𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝙈𝘼𝙍𝘾𝙀𝙑𝙊 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "𝙔𝙄𝙎𝙆𝘼 𝟐𝟎𝟐𝟏 🎄꙳.\n"
    "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
    "𝐌𝐈𝐋𝐀𝐍 🌵\n"
    "𝐀𝐍𝐈𝐒𝐀𝐔 🌵\n"
    "𝐅𝐑𝐀𝐍𝐂𝐈𝐒𝐎 🌵\n"
     "𝐀𝐏𝐑𝐈𝐋  🌵\n"
     "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
     "𝙛𝙞𝙘𝙤 🎄\n"
     "𝙞𝙨𝙝𝙤 🎄\n"
     "𝙖𝙗𝙧𝙖𝙨 🎄\n"
     "𝙣𝙞𝙣𝙤 🎄\n"
     "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
     "..⌠𝐒𝐞𝐥𝐯𝐚𝐧𝐚⌡𓊑.\n"
     "..⌠𝐓𝐨𝐛𝐚𝐤⌡𓊑.\n"
     "..⌠𝐄𝐥𝐤𝐚𝐫⌡𓊑.\n"
     "..⌠𝐌𝐚𝐲𝐚⌡𓊑.\n"
     "..⌠𝐓𝐞𝐨𝐨⌡𓊑.\n"
     "..⌠𝐌𝐞𝐚⌡𓊑.\n"
     "..⌠𝐋𝐞𝐥𝐞⌡𓊑.\n"
     "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
     "⌯ ˹𝙆𝙖𝙧𝙖˼ \n"
     "⌯ ˹𝙉𝙖𝙖𝙧˼ \n"
     "⌯ ˹𝙂𝙢𝙧˼ \n"
     "⌯ ˹𝘿𝙚𝙫˼\n"
     "⌯ ˹𝙀𝙫𝙖˼\n"
     "﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎\n"
     ":   ˹𝘾𝘼𝙍𝙊𝙇𝙄𝙉𝙀˼ 𓆪 .\n"
     ":   ˹𝘾𝙍𝙔𝙎𝙏𝘼𝙇˼ 𓆪 .\n"
     ":   ˹𝙇𝘼𝙐𝙍𝙀𝙉˼ 𓆪 .\n"
     ":   ˹𝙆𝘼𝙈𝙄𝙇𝘼˼ 𓆪 .\n"
     ":   ˹𝘿𝘼𝙉𝘼˼ 𓆪 .\n"
     ":   ˹𝙍𝙄𝙏𝘼˼ 𓆪 .\n"
     ": ..................."
)
