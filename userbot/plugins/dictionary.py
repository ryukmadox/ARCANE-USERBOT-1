# FIX BY TEAM DYNAMIC AMAN PANDEY
"""Urban Dictionary
Syntax: .ud Query"""
import asyncurban
from PyDictionary import PyDictionary

from userbot import CMD_HELP
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="ud (.*)"))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    urban = asyncurban.UrbanDictionary()
    try:
        mean = await urban.get_word(word)
        await edit_or_reply(
            event,
            "Text: **{}**\n\nMeaning: **{}**\n\nExample: __{}__".format(
                mean.word, mean.definition, mean.example
            ),
        )
    except asyncurban.WordNotFoundError:
        await edit_or_reply(event, "No result found for **" + word + "**")


@bot.on(admin_cmd(pattern="meaning (.*)"))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    dictionary = PyDictionary()
    hell = dictionary.meaning(word)
    output = f"**Word :** __{word}__\n\n"
    try:
        for a, b in hell.items():
            output += f"**{a}**\n"
            for i in b:
                output += f"☞__{i}__\n"
        await edit_or_reply(event, output)
    except Exception:
        await edit_or_reply(event, f"Couldn't fetch meaning of {word}")


CMD_HELP.update(
    {
        "dictionary": "**Plugin :** `dictionary`\
    \n\n**Syntax :** `.ud query`\
    \n**Usage : **fetches meaning from Urban dictionary\
    \n\n**Syntax : **`.meaning query`\
    \n**Usage : **Fetches meaning of the given word\
    "
    }
)
