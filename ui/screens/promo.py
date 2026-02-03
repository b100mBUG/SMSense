from kivy.lang import Builder
from kivy.metrics import sp, dp


from kivymd.uix.screen import MDScreen

from ui.screens.sms import fetch_all_messages, SMSRow
from config import resource_path

Builder.load_file(resource_path("ui/screens/promo.kv"))


class PromoScreen(MDScreen):
    def __init(self, **kwargs):
        super().__init__(**kwargs)
        self.messages = None
    
    def load_messages(self):
        self.messages = fetch_all_messages("promotion")

    

    def display_items(self, prev_class, items, mapper):
        prev = self.ids.rec_view
        self.ids.rec_box.default_size = (None, dp(300))
        prev.viewclass = prev_class

        data = [mapper(i) for i in items]
        prev.data = data
    
    def sms_mapper(self, sms: dict | None):
        sms = sms or {}
        return {
            'sender': sms.get("sender"),
            'msg': sms.get("body").strip(),
            'time': f"{sms.get('timestamp')}"
        }
    
    def show_messages(self):
        self.ids.rec_box.clear_widgets()
        if not self.messages:
            return
        
        self.display_items("SMSRow", self.messages, self.sms_mapper)
    
    def on_enter(self):
        self.load_messages