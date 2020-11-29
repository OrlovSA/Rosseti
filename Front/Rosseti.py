from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
import json
import requests
from kivy.properties import ObjectProperty
from sys import getdefaultencoding


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
    padding: 50
        
# первая страница 

<OneScreen>:
    text_login: text_login
    text_pass: text_pass
    
    MyGridLayout:
        rows: 4
        
        GridLayout:
            padding: [20, 20, 20, 20]
            rows: 2
            
            MyLabel:
                pos_hint: {'x': .9, 'y': .9}
                text: f'[color=#135794]Рационализаторский портал[/color]'
    
            Image:
                source: '1.png'

        BoxLayout:  
            orientation: 'vertical'
            spacing: 20
            
            MyTextInput:
                id: text_login
                hint_text: 'Логин'
                required: False
                helper_text_mode: "on_focus"
                helper_text: "Электронная почта или номер тефлефона"            

            MyTextInput:
                id: text_pass
                hint_text: 'Пароль'
                required: False
                helper_text_mode: "on_error"
                helper_text: "Не верный логин или пароль"
                
            FloatLayout:                
                MyButton:
                    pos_hint: {'x': .15, 'y': .5}
                    size_hint: .7, .3
                    text: 'Войти'
                    on_press:root.check_input()
                
                MDTextButton:
                    pos_hint: {'x': .35, 'y': .35}
                    markup: True
                    text: f'[color=#135794]Забыл пароль?[/color]'
                    on_press:root.manager.current = 'Protocol418'
    

<HelloScreen>:
    text_Label: text_Label

    MyGridLayout:
        rows: 2
        
        FloatLayout:
            Image:
                pos_hint: {'x': .25, 'y': .8}
                size_hint: .5, .3
                source: '1.png'
                
            MyLabel:
                pos_hint: {'x': .01, 'y': .13}
                text: f'[color=#135794]Добро пожаловать[/color]'
            
            MyLabel:
                id: text_Label
                pos_hint: {'x': .01, 'y': .01}
                text: f'[color=#135794]Петров Пётр Петрович[/color]'
                
        Image:
            source: 'hello.png'

<HomeScreen>:
    text_search: text_search
    
    MyGridLayout:
        rows: 2
        
        FloatLayout:
            Image:
                pos_hint: {'x': .25, 'y': .85}
                size_hint: .5, .3
                source: '1.png' 
          
        
        MyTextInput:
            pos_hint: {'x': .50, 'y': .80}
            id: text_search
            hint_text: 'Поиск'
    
    
    BoxLayout:
        padding: [40, 0, 40, 0]
        spacing: 27
        
        MDIconButton:
            icon: 'home-06.png'
            on_press:
                self.icon = 'home-01.png'
            on_release:
                self.icon = 'home-06.png'
                
                
        MDIconButton:
            icon: 'ideas-03.png'
            on_press:
                self.icon = 'ideas-08.png'
            on_release:
            
            
        MDIconButton:
            user_font_size: "70sp"
            icon: 'new_idea-05.png'
            on_release:


        MDIconButton:
            icon: 'message-04.png'
            on_press:
                self.icon = 'message-09.png'
            on_release:
            
            
        MDIconButton:
            icon: 'profile-02.png'
            on_press:
                self.icon = 'profile-07.png'
            on_release:    
        
            
                
<Protocol418Screen>:
    GridLayout:
        padding: [20, 20, 20, 20]
        rows: 4

        Image:
            source: '1.png'
        
        MyLabel:
            font_size: '100sp'
            text: f'[color=#135794]418[/color]'
            
        MDTextButton:
            markup: True
            text: f'[color=#135794]Назад?[/color]'
            on_press:root.manager.current = 'one' 

        Image:
            source: 'hello.png'
            
            
''')
class User_data():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class OneScreen(Screen, User_data):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def check_input(self):
        login = self.text_login.text.lower()
        pas = self.text_pass.text

        while True:
            url = f'https://secure-harbor-01729.herokuapp.com/api/v1/check_user/?format=' \
                  f'json&user_login={login}&user_password={pas}'
            response = requests.get(url)
            if response.status_code == 200:
                self.user_data = response.json()
                if self.user_data.get('status') == 'ok':
                    self.text_login.required = False
                    self.text_pass.required = False
                    self.manager.current = 'home'
                    break
                else:
                    self.text_login.required = True
                    self.text_pass.required = True
                    break


class CheckScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class HelloScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Protocol418Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RossetiApp(MDApp):
    title = "Россети Идея"


    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(OneScreen(name='one'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(Protocol418Screen(name='Protocol418'))
        sm.add_widget(HelloScreen(name='hello'))
        return sm


if __name__ == "__main__":
    RossetiApp().run()