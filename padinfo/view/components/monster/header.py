from typing import TYPE_CHECKING

from discordmenu.embed.text import LinkedText, Text

from padinfo.common.padx import monster_url

if TYPE_CHECKING:
    from dadguide.models.monster_model import MonsterModel


class MonsterHeader:
    @staticmethod
    def ja_suffix(m: "MonsterModel", subname_on_override=True):
        suffix = ""
        if m.roma_subname and (subname_on_override or m.name_en_override is None):
            suffix += ' [{}]'.format(m.roma_subname)
        if not m.on_na:
            suffix += ' (JP only)'
        return suffix

    @staticmethod
    def short(m: "MonsterModel", link=False):
        type_emojis = ''
        msg = '[{}] {}{}'.format(m.monster_no_na, type_emojis, m.name_en)
        return '[{}]({})'.format(msg, monster_url(m)) if link else msg

    @staticmethod
    def long(m: "MonsterModel", link=False):
        msg = MonsterHeader.short(m) + MonsterHeader.ja_suffix(m)
        return '[{}]({})'.format(msg, monster_url(m)) if link else msg

    @staticmethod
    def name(m: "MonsterModel", link=False, show_jp=False):
        msg = '[{}] {}{}'.format(
            m.monster_no_na,
            m.name_en,
            MonsterHeader.ja_suffix(m) if show_jp else '')
        return LinkedText(msg, monster_url(m)) if link else Text(msg)

    @staticmethod
    def long_v2(m: "MonsterModel", link=False):
        msg = '[{}] {}{}'.format(m.monster_no_na, m.name_en, MonsterHeader.ja_suffix(m))
        return LinkedText(msg, monster_url(m)) if link else Text(msg)
