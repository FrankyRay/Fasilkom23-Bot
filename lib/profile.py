from linebot.models import SourceGroup

def get_profile(bot, event):
    return bot.get_group_member_profile(event.source.group_id, event.source.user_id) \
        if isinstance(event.source, SourceGroup) \
        else bot.get_profile(event.source.user_id)