from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.widget import Widget

KV = '''
MDScreen:
    md_bg_color: [35/255, 59/255, 54/255, 1]
    
    MDCard:
        size_hint: None, None
        size: 320, 400
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 15
        md_bg_color: [35/255, 49/255, 48/255, 1]
        padding: 20
        spacing: 30
        orientation: "vertical"

        MDLabel:
            text: 'LOGIN'
            font_style: 'Button'
            font_size: 45
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        MDTextField:
            mode: 'round'
            hint_text: "username"
            icon_right: "account"
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
            color_active: [1, 1, 1, 1]

        MDTextField:
            mode: 'round'
            hint_text: "password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
            color_active: [1, 1, 1, 1]
            password: True

        MDRoundFlatButton:
            text: 'SIGN-UP'
            pos_hint: {"center_x": 0.5}
            font_size: 15

        Widget:
            size_hint_y: None
            height: 30
'''

class LoginApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    LoginApp().run()
