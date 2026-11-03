from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty 
from functions import ruffier_index
from meow import *
import json

## GLOBAL

name, age = '', 7
pulse_1 = 0
pulse_2 = 0
pulse_3 = 0
language = "es"

with open("test_ruffier/language.json", "r", encoding="utf-8") as archivo:
    languages = json.load(archivo)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.language = ""
        language_select = Label(text="Please select your language")
        self.english_button = Button(text="en", color=(1, 1, 1, 0), background_down="en_flag.jpg", background_normal="en_flag.jpg", size_hint_max_x="250sp")
        self.spanish_button = Button(text="es", color=(1, 1, 1, 0), background_down="es_flag.jpg", background_normal="es_flag.jpg", size_hint_max_x="250sp")
        self.japanese_button = Button(text="jp", color=(1, 1, 1, 0), background_down="jp_flag.jpg", background_normal="jp_flag.jpg",size_hint_max_x="250sp")

        self.english_button.bind(on_press=self.get_language)
        self.spanish_button.bind(on_press=self.get_language)
        self.japanese_button.bind(on_press=self.get_language)

        self.next_button = Button(text="Continue", size_hint_max_x="250sp", size_hint=(0.4, 0.2))
        self.next_button.on_press = self.next

        main_layout = BoxLayout(orientation="vertical", spacing=25)
        main_layout.add_widget(language_select)

        buttons_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=(1, '250sp'))
        buttons_layout.add_widget(self.english_button)
        buttons_layout.add_widget(self.spanish_button)
        buttons_layout.add_widget(self.japanese_button)

        main_layout.add_widget(buttons_layout)
        main_layout.add_widget(self.next_button)

        self.add_widget(main_layout)

    def get_language(self, instance):
        global language
        language = instance.text

    def next(self):
            app = App.get_running_app()
            app.root.current = "start"
            app.root.transition.direction = "left"

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global languages, language

        welcome_text = Label(text=languages[language]["welcome"])
        name_text = Label(text=languages[language]["insert_name"])
        age_text = Label(text="ingrese su edad")
        self.name_warning = Label(text="Por favor, inserte su nombre para continuar", color=(1, 0, 0, 0), bold=True, size_hint_y=None)

        self.input_name = TextInput(multiline=False)
        self.input_age = TextInput(multiline=False, text="7")

        self.button = Button(text="Comenzar el test", size_hint=(0.4, 0.2), pos_hint={'center_x':0.5})
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation="vertical")
        input_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=(1, '80sp'))
        input_2_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=(1, '80sp'))

        main_layout.add_widget(welcome_text)
        main_layout.add_widget(self.name_warning)

        input_layout.add_widget(name_text)
        input_layout.add_widget(self.input_name)

        input_2_layout.add_widget(age_text)
        input_2_layout.add_widget(self.input_age)

        main_layout.add_widget(input_layout)
        main_layout.add_widget(input_2_layout)

        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        global age, name
        name = self.input_name.text
        age = int(self.input_age.text)

        if name != "":
            app = App.get_running_app()
            app.root.current = "firstStep"
            app.root.transition.direction = "left"
        else:
            self.name_warning.color = (1, 0, 0, 1)

                 
class PulseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instructions_text = Label(text=txt_test1)

        pulse_text = Label(text="ingrese su pulso")

        self.input_pulse = TextInput(multiline=False)

        self.button = Button(text="Siguiente", size_hint=(0.4, 0.2), pos_hint={'center_x':0.5})

        main_layout = BoxLayout(orientation="vertical")
        input_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=('120sp', '80sp'))

        main_layout.add_widget(instructions_text)

        input_layout.add_widget(pulse_text)
        input_layout.add_widget(self.input_pulse)

        main_layout.add_widget(input_layout)

        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        pulse_1 = int(self.input_pulse.text)
        print(pulse_1)

        app = App.get_running_app()
        app.root.current = "secondStep"

class WorkoutScreen(Screen):
    def __init__(self, **kwargs):
        pass

class Pulse2Screen(Screen):
    def __init__(self, **kwargs):
        pass

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        pass

class RuffierApp(App):
    def build(self):
        manager = ScreenManager()

        manager.add_widget(WelcomeScreen(name="main"))
        manager.add_widget(StartScreen(name="start"))
        manager.add_widget(PulseScreen(name="firstStep"))
        manager.add_widget(WorkoutScreen(name="secondStep"))
        #manager.add_widget(Pulse2Screen(name="lastStep"))
        #manager.add_widget(ResultScreen(name="results"))

        return manager

if __name__ == '__main__':
    App = RuffierApp()
    App.run()