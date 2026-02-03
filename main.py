# ------------------------
# HARD GUARD (must be first)
# ------------------------
import sys
import types

if "android" not in sys.modules:
    sys.modules["android"] = types.ModuleType("android")


# ------------------------
# Safe imports now
# ------------------------
import os
from kivy.utils import platform


# ------------------------
# Kivy / KivyMD
# ------------------------
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivymd.app import MDApp

from ui.screens.home import HomeScreen
from ui.screens.focused import FocusedScreen
from ui.screens.spam import SpamScreen
from ui.screens.promo import PromoScreen
from ui.screens.otp import OTPScreen
from ui.screens.unknown import UnknownScreen


# ------------------------
# Permissions (runtime-safe)
# ------------------------
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_SMS, Permission.RECEIVE_SMS])


class SMSense(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"

        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(FocusedScreen(name="focused"))
        sm.add_widget(SpamScreen(name="spam"))
        sm.add_widget(PromoScreen(name="promo"))
        sm.add_widget(OTPScreen(name="otp"))
        sm.add_widget(UnknownScreen(name="unknown"))

        sm.current = "home"
        return sm


if __name__ == "__main__":
    SMSense().run()
