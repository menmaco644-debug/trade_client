import os
import subprocess
import threading
import time
from datetime import datetime

from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

MINECRAFT_VERSION = "1.1.5"

KV = f'''
MDScreen:
    md_bg_color: 0.02, 0.02, 0.04, 1

    MDBoxLayout:
        orientation: "vertical"
        padding: "12dp"
        spacing: "8dp"

        MDTopAppBar:
            title: "BREADIX CLIENT"
            subtitle: f"Minecraft {MINECRAFT_VERSION} | Mod Menu"
            elevation: 8
            md_bg_color: 0.06, 0.06, 0.10, 1
            specific_text_color: 0.9, 0.7, 0.2, 1

        ScrollView:
            do_scroll_x: False

            MDBoxLayout:
                orientation: "vertical"
                spacing: "8dp"
                adaptive_height: True
                padding: "4dp"

                MDCard:
                    orientation: "vertical"
                    padding: "12dp"
                    spacing: "6dp"
                    size_hint_y: None
                    height: "130dp"
                    md_bg_color: 0.08, 0.08, 0.12, 1
                    radius: [16, 16, 16, 16]

                    MDLabel:
                        text: "СТАТУС"
                        font_style: "H6"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.7, 0.2, 1

                    MDLabel:
                        id: status_label
                        text: f"Проверка Minecraft {MINECRAFT_VERSION}..."
                        font_style: "Body1"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1

                    MDLabel:
                        id: version_label
                        text: f"Требуемая версия: {MINECRAFT_VERSION}"
                        font_style: "Body1"
                        theme_text_color: "Custom"
                        text_color: 0.5, 0.7, 1, 1

                MDCard:
                    orientation: "vertical"
                    padding: "12dp"
                    spacing: "6dp"
                    size_hint_y: None
                    height: "80dp"
                    md_bg_color: 0.08, 0.08, 0.12, 1
                    radius: [16, 16, 16, 16]

                    MDRaisedButton:
                        id: launch_btn
                        text: "🚀 ЗАПУСТИТЬ MINECRAFT 1.1.5"
                        md_bg_color: 0.2, 0.6, 0.3, 1
                        size_hint_y: None
                        height: "48dp"
                        font_size: "16sp"
                        on_release: app.launch_minecraft()

                MDCard:
                    orientation: "vertical"
                    padding: "12dp"
                    spacing: "6dp"
                    size_hint_y: None
                    height: "150dp"
                    md_bg_color: 0.08, 0.08, 0.12, 1
                    radius: [16, 16, 16, 16]

                    MDLabel:
                        text: "📊 HUD"
                        font_style: "H6"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.7, 0.2, 1

                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: "4dp"

                        MDLabel:
                            text: "❤️ HP: --"
                            font_style: "Body1"
                            theme_text_color: "Custom"
                            text_color: 1, 0.3, 0.3, 1

                        MDLabel:
                            text: "🛡️ Armor: --"
                            font_style: "Body1"
                            theme_text_color: "Custom"
                            text_color: 0.3, 0.6, 1, 1

                        MDLabel:
                            text: "🧪 FX: --"
                            font_style: "Body1"
                            theme_text_color: "Custom"
                            text_color: 0.6, 0.4, 1, 1

                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: "4dp"

                        MDLabel:
                            text: "⚡ Combo: 0"
                            font_style: "Body1"
                            theme_text_color: "Custom"
                            text_color: 1, 0.8, 0.2, 1

                        MDLabel:
                            text: "🖱️ CPS: 0.0"
                            font_style: "Body1"
                            theme_text_color: "Custom"
                            text_color: 0.3, 1, 0.5, 1

                MDCard:
                    orientation: "vertical"
                    padding: "12dp"
                    spacing: "6dp"
                    size_hint_y: None
                    height: "120dp"
                    md_bg_color: 0.08, 0.08, 0.12, 1
                    radius: [16, 16, 16, 16]

                    MDLabel:
                        text: "⌨️ KEYSTROKES"
                        font_style: "H6"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.7, 0.2, 1

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "4dp"
                        pos_hint: {{"center_x": 0.5}}

                        MDBoxLayout:
                            orientation: "horizontal"
                            spacing: "4dp"
                            pos_hint: {{"center_x": 0.5}}

                            MDLabel:
                                text: ""
                                size_hint_x: None
                                width: "44dp"

                            MDLabel:
                                id: key_w
                                text: "W"
                                font_style: "H5"
                                theme_text_color: "Custom"
                                text_color: 0.5, 0.5, 0.5, 1
                                size_hint_x: None
                                width: "44dp"
                                halign: "center"

                            MDLabel:
                                text: ""
                                size_hint_x: None
                                width: "44dp"

                        MDBoxLayout:
                            orientation: "horizontal"
                            spacing: "4dp"
                            pos_hint: {{"center_x": 0.5}}

                            MDLabel:
                                id: key_a
                                text: "A"
                                font_style: "H5"
                                theme_text_color: "Custom"
                                text_color: 0.5, 0.5, 0.5, 1
                                size_hint_x: None
                                width: "44dp"
                                halign: "center"

                            MDLabel:
                                id: key_s
                                text: "S"
                                font_style: "H5"
                                theme_text_color: "Custom"
                                text_color: 0.5, 0.5, 0.5, 1
                                size_hint_x: None
                                width: "44dp"
                                halign: "center"

                            MDLabel:
                                id: key_d
                                text: "D"
                                font_style: "H5"
                                theme_text_color: "Custom"
                                text_color: 0.5, 0.5, 0.5, 1
                                size_hint_x: None
                                width: "44dp"
                                halign: "center"

                MDCard:
                    orientation: "vertical"
                    padding: "12dp"
                    spacing: "6dp"
                    size_hint_y: None
                    height: "200dp"
                    md_bg_color: 0.08, 0.08, 0.12, 1
                    radius: [16, 16, 16, 16]

                    MDLabel:
                        text: "⚙️ МОДУЛИ"
                        font_style: "H6"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.7, 0.2, 1

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "4dp"

                        MDSwitch:
                            id: autosprint_switch
                            text: "🏃 AutoSprint"
                            active: True
                            theme_text_color: "Custom"
                            text_color: 0.8, 0.8, 0.8, 1

                        MDSwitch:
                            id: nohurtcam_switch
                            text: "📷 NoHurtcam"
                            active: True
                            theme_text_color: "Custom"
                            text_color: 0.8, 0.8, 0.8, 1

                        MDSwitch:
                            id: fullbright_switch
                            text: "💡 Fullbright"
                            active: True
                            theme_text_color: "Custom"
                            text_color: 0.8, 0.8, 0.8, 1

                        MDSwitch:
                            id: lowfire_switch
                            text: "🔥 LowFire"
                            active: True
                            theme_text_color: "Custom"
                            text_color: 0.8, 0.8, 0.8, 1

                        MDSwitch:
                            id: lowbob_switch
                            text: "🎥 LowBob"
                            active: True
                            theme_text_color: "Custom"
                            text_color: 0.8, 0.8, 0.8, 1

                MDCard:
                    orientation: "vertical"
                    padding: "12dp"
                    spacing: "6dp"
                    size_hint_y: None
                    height: "180dp"
                    md_bg_color: 0.06, 0.06, 0.10, 1
                    radius: [16, 16, 16, 16]

                    MDLabel:
                        text: "📋 ЛОГ"
                        font_style: "H6"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.7, 0.2, 1

                    ScrollView:
                        do_scroll_x: False
                        size_hint_y: 1

                        MDBoxLayout:
                            id: log_box
                            orientation: "vertical"
                            adaptive_height: True
                            spacing: "2dp"
'''

class BreadixClient(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.keys_pressed = {"W": False, "A": False, "S": False, "D": False}
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)
        Clock.schedule_once(lambda dt: self.check_minecraft())
        return Builder.load_string(KV)

    def check_minecraft(self):
        Clock.schedule_once(lambda dt: self._check_minecraft())

    def _check_minecraft(self):
        mc_found = False
        possible_paths = [
            "/sdcard/games/com.mojang/minecraftpe",
            "/sdcard/Android/data/com.mojang.minecraftpe",
            "/sdcard/games/com.mojang",
            "/storage/emulated/0/Android/data/com.mojang.minecraftpe",
            "/storage/emulated/0/games/com.mojang",
            "/data/data/com.mojang.minecraftpe",
        ]
        for path in possible_paths:
            if os.path.exists(path):
                mc_found = True
                break

        if mc_found:
            self.root.ids.status_label.text = f"✅ Minecraft {MINECRAFT_VERSION} найден"
            self.root.ids.status_label.text_color = (0.3, 1, 0.5, 1)
            self.log("SYSTEM", f"Minecraft {MINECRAFT_VERSION} найден")
            self.root.ids.launch_btn.disabled = False
            self.root.ids.launch_btn.md_bg_color = (0.2, 0.6, 0.3, 1)
        else:
            self.root.ids.status_label.text = f"❌ Minecraft {MINECRAFT_VERSION} НЕ найден"
            self.root.ids.status_label.text_color = (1, 0.3, 0.3, 1)
            self.log("ERROR", f"Minecraft {MINECRAFT_VERSION} не установлен")
            self.root.ids.launch_btn.disabled = True
            self.root.ids.launch_btn.md_bg_color = (0.4, 0.4, 0.4, 1)
            dialog = MDDialog(
                title=f"Minecraft {MINECRAFT_VERSION} не найден",
                text=f"Для работы клиента необходима версия {MINECRAFT_VERSION}.\n\nДругие версии не поддерживаются.",
                buttons=[MDFlatButton(text="ОК", on_release=lambda x: dialog.dismiss())]
            )
            dialog.open()

    def launch_minecraft(self):
        self.log("SYSTEM", f"Запуск Minecraft {MINECRAFT_VERSION}...")
        self.root.ids.status_label.text = f"⏳ Запуск Minecraft {MINECRAFT_VERSION}..."
        self.root.ids.status_label.text_color = (1, 0.8, 0.2, 1)
        try:
            subprocess.Popen([
                "am", "start",
                "-a", "android.intent.action.MAIN",
                "-c", "android.intent.category.LAUNCHER",
                "-n", "com.mojang.minecraftpe/.MainActivity"
            ])
            self.log("SUCCESS", "Minecraft запущен")
            self.root.ids.status_label.text = f"✅ Minecraft {MINECRAFT_VERSION} запущен"
            self.root.ids.status_label.text_color = (0.3, 1, 0.5, 1)
        except Exception as e:
            self.log("ERROR", f"Ошибка запуска: {e}")
            self.root.ids.status_label.text = f"❌ Ошибка запуска: {e}"
            self.root.ids.status_label.text_color = (1, 0.3, 0.3, 1)

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        key_map = {"w": "W", "W": "W", "a": "A", "A": "A", "s": "S", "S": "S", "d": "D", "D": "D"}
        if codepoint in key_map:
            k = key_map[codepoint]
            self.keys_pressed[k] = True
            self.update_keystrokes_ui()
        return False

    def on_key_up(self, window, key, scancode, codepoint, modifier):
        key_map = {"w": "W", "W": "W", "a": "A", "A": "A", "s": "S", "S": "S", "d": "D", "D": "D"}
        if codepoint in key_map:
            k = key_map[codepoint]
            self.keys_pressed[k] = False
            self.update_keystrokes_ui()
        return False

    def update_keystrokes_ui(self):
        for key_name, key_id in [("W", "key_w"), ("A", "key_a"), ("S", "key_s"), ("D", "key_d")]:
            if hasattr(self, 'root') and key_id in self.root.ids:
                label = self.root.ids[key_id]
                if self.keys_pressed.get(key_name, False):
                    label.text_color = (0.3, 1, 0.5, 1)
                else:
                    label.text_color = (0.5, 0.5, 0.5, 1)

    def log(self, tag, text):
        timestamp = datetime.now().strftime("%H:%M:%S")
        line = f"[{timestamp}] [{tag}] {text}"
        Clock.schedule_once(lambda dt: self._add_log(line))

    def _add_log(self, line):
        if hasattr(self, 'root') and 'log_box' in self.root.ids:
            self.root.ids.log_box.add_widget(
                OneLineListItem(text=line, theme_text_color="Custom", text_color=(1, 1, 1, 1))
            )

if __name__ == "__main__":
    BreadixClient().run()
