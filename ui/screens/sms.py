from actions.classify import group_messages
from actions.inbox import fetch_all_sms, fetch_new_sms, get_latest_sms_timestamp

from kivymd.uix.list import MDListItem, MDListItemHeadlineText, MDListItemLeadingIcon, MDListItemSupportingText, MDListItemTertiaryText
from kivy.properties import StringProperty, ObjectProperty


def fetch_all_messages():
    all_messages = fetch_all_sms()
    grouped_messages = group_messages(all_messages)
    return grouped_messages

def refresh_messages(source: str | None = None):
    new_messages = fetch_new_sms(get_latest_sms_timestamp())
    grouped_messages = group_messages(new_messages)
    return grouped_messages[source.upper()]


class SMSRow(MDListItem):
    sender = StringProperty("")
    msg = StringProperty("")
    time = StringProperty("")
    show_profile = ObjectProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.radius = (20,)

        #self.on_release = lambda: self.show_profile()

        self.sender_label = MDListItemHeadlineText(theme_text_color = "Custom", text_color = "blue", shorten=True, shorten_from = "right")
        self.msg_label = MDListItemSupportingText(theme_text_color = "Custom", text_color = "blue", shorten=True, shorten_from = "right")
        self.time_label = MDListItemTertiaryText(theme_text_color = "Custom", text_color = "blue", shorten=True, shorten_from = "right")
        
        self.add_widget(MDListItemLeadingIcon(icon="message", theme_icon_color = "Custom", icon_color = "blue"))
        self.add_widget(self.sender_label)
        self.add_widget(self.msg_label)
        self.add_widget(self.time_label)
        
        self.bind(sender=lambda inst, val: setattr(self.sender_label, 'text', val))
        self.bind(msg=lambda inst, val: setattr(self.msg_label, 'text', val))
        self.bind(time=lambda inst, val: setattr(self.time_label, 'text', val))
