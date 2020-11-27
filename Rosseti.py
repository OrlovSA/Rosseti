from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')
Window.size = (480, 853)

Builder.load_string('''
#Надстройки верстки Киви

<MyButton@Button>:
    font_name: 'PF Din Text Comp Pro Medium Regular.ttf'
    font_size: '25sp'
    background_color: [.0, .34, .58, 1]
    background_normal: ''

<MyLabel@Label>:
    font_name: 'PF Din Text Comp Pro Medium Regular.ttf'
    font_size: '30sp'
    markup: True

<MyTextInput@MDTextField>:
    font_name: 'PF Din Text Comp Pro Medium Regular.ttf'
    font_size: '45sp'
    markup: True
    haling: 'left'
    valing: 'middle'
    ext_size: self.size
    multiline: False

<MyGridLayout@GridLayout>:
    canvas:
        Color:
            rgba:(1,1,1,1)
        Rectangle:
            pos:self.pos
            size:self.size
    padding: [30, 30, 30, 30]

# первая страница 
<OneScreen>:
    MyGridLayout:
        text_login: text_login
        text_pass: text_pass
        rows: 3
        
        Image:
            source: '1.png'

        MyLabel:
            text: f'[color=#135794]Рационализаторский портал[/color]'

        BoxLayout:
            orientation: 'vertical'
            spacing: 10
            
            MyTextInput:
                id: text_login
                hint_text: 'Логин'

            MyTextInput:
                id: text_pass
                hint_text: 'Пароль'
                
            MyButton:
                text: 'Войти'
                on_press:root.manager.current = 'check'
                    
            BoxLayout:
                spacing: 10
               
                MyButton:
                    text: 'Регистрация'
                    on_press:root.manager.current = 'check'
                MyButton:
                    text: 'Забыл пароль?'
                    on_press:root.manager.current = 'check'
    

<CheckScreen>:
    MyGridLayout:
        text_login: text_login
        text_pass: text_pass
        rows: 3

        Image:
            source: '1.png'

        MyLabel:
            text: f'[color=#135794]Рационализаторский портал[/color]'

        BoxLayout:
            orientation: 'vertical'
            spacing: 10

            MyTextInput:
                id: text_login
                hint_text: 'логин'

            MyTextInput:
                id: text_pass
                hint_text: 'пароль'

            MyButton:
                text: 'Войти'
                on_press:root.manager.current = 'one'
''')


class OneScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CheckScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def previous_button(self):
        self.manager.current = 'one'


class RossetiApp(MDApp):
    title = "Россети Идея"

    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(OneScreen(name='one'))
        sm.add_widget(CheckScreen(name='check'))
        return sm


if __name__ == "__main__":
    RossetiApp().run()