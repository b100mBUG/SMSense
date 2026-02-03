from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.uix.screen import MDScreen

from config import resource_path

Builder.load_file(resource_path("ui/screens/home.kv"))


class HomeScreen(MDScreen):
    image_path = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_path = resource_path("assets")
        
    
    def on_enter(self):

        print("Image path: ", self.image_path)