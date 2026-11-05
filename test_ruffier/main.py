from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock
from kivy.core.window import Window
from functions import ruffier_index, ruffier_results
import json
from time import sleep

## GLOBAL
name, age = '', 7
pulse_1, pulse_2, pulse_3 = 0, 0, 0
language = "es"
ruffier = 0.0
results = ""

with open("test_ruffier/language.json", "r", encoding="utf-8") as archivo:
    languages = json.load(archivo)

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.language = ""
        language_select = Label(text="Por favor seleccione su lenguaje", color=(0,0,0,1), font_size='20sp')
        self.english_button = Button(text="en", border = (30, 30, 30, 30), color=(1, 1, 1, 0), background_down="images/en_flag.jpg", background_normal="images/en_flag.jpg", size_hint_max_x="250sp", width="250sp")
        self.spanish_button = Button(text="es", border = (30, 30, 30, 30), color=(1, 1, 1, 0), background_down="images/es_flag.jpg", background_normal="images/es_flag.jpg", size_hint_max_x="250sp", width="250sp")
        self.japanese_button = Button(text="ca", border = (30, 30, 30, 30), color=(1, 1, 1, 0), background_down="images/ca_flag.jpg", background_normal="images/ca_flag.jpg",size_hint_max_x="250sp", width="250sp")

        self.english_button.bind(on_press=self.get_language)
        self.spanish_button.bind(on_press=self.get_language)
        self.japanese_button.bind(on_press=self.get_language)

        self.next_button = Button(text="Continue", border = (30, 30, 30, 30), color=(0.3, 0.3, 0.3, 1), background_down="images/down.png", background_normal="images/normal.png", size_hint_max_x="250sp", size_hint=(0.4, 0.2), pos_hint={'center_x':0.5})
        self.next_button.on_press = self.next

        main_layout = BoxLayout(orientation="vertical", spacing=25)
        main_layout.add_widget(language_select)

        central_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        buttons_layout = BoxLayout(orientation='horizontal', padding=60, spacing=30, size_hint_y=None, height='250sp', size_hint_x=0.7)
        buttons_layout.add_widget(self.english_button)
        buttons_layout.add_widget(self.spanish_button)
        buttons_layout.add_widget(self.japanese_button)

        central_layout.add_widget(buttons_layout)

        main_layout.add_widget(central_layout)
        main_layout.add_widget(self.next_button)

        self.add_widget(main_layout)

    def get_language(self, instance):
        global language
        language = instance.text

    def next(self):
            app = App.get_running_app()
            app.root.transition.direction = "left"
            app.root.current = "start"

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global languages, language

        self.welcome_text = Label(text='', color=(0, 0, 0, 1), font_size='20sp')
        self.name_text = Label(text='', color=(0, 0, 0, 1), font_size='20sp')
        self.age_text = Label(text='', color=(0, 0, 0, 1), font_size='20sp')
        self.name_warning = Label(text='', color=(1, 0, 0, 0), bold=True, size_hint_y=None, font_size='20sp')

        self.input_name = TextInput(multiline=False)
        self.input_age = TextInput(multiline=False, text="7")

        self.button = Button(text='', border = (30, 30, 30, 30), color=(0.3, 0.3, 0.3, 1), background_down="images/down.png", background_normal="images/normal.png", size_hint=(0.4, 0.2), pos_hint={'center_x':0.5})
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation="vertical")
        input_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=(1, '80sp'))
        input_2_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=(1, '80sp'))

        main_layout.add_widget(self.welcome_text)
        main_layout.add_widget(self.name_warning)

        input_layout.add_widget(self.name_text)
        input_layout.add_widget(self.input_name)

        input_2_layout.add_widget(self.age_text)
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

    def on_enter(self, *args):
        global languages, language
        self.welcome_text.text = languages[language]["welcome"]
        self.name_text.text = languages[language]["insert_name"]
        self.age_text.text = languages[language]["insert_age"]
        self.name_warning.text = languages[language]["error_name"]
        self.button.text = languages[language]["next"]
            
class PulseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.instructions_text = Label(text='', color=(0,0,0,1), font_size='20sp')

        self.pulse_text = Label(text='', color=(0,0,0,1), font_size='20sp')

        self.input_pulse = TextInput(multiline=False)

        self.button = Button(text='', border = (30, 30, 30, 30), color=(0.3, 0.3, 0.3, 1), background_down="images/down.png", background_normal="images/normal.png", size_hint=(0.4, 0.2), pos_hint={'center_x':0.5})
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation="vertical")
        input_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=('120sp', '80sp'))

        main_layout.add_widget(self.instructions_text)

        input_layout.add_widget(self.pulse_text)
        input_layout.add_widget(self.input_pulse)

        main_layout.add_widget(input_layout)

        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        global pulse_1
        pulse_1 = int(self.input_pulse.text)
        print(pulse_1)

        app = App.get_running_app()
        app.root.current = "secondStep"
        app.root.transition.direction = "left"

    def on_enter(self, *args):
        global languages, language
        self.instructions_text.text = languages[language]["first_step"]
        self.pulse_text.text = languages[language]["insert_pulse"]
        self.button.text = languages[language]["next"]

class WorkoutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instructions_text = Label(text='', color=(0, 0, 0, 1), font_size='20sp')
        self.counter = Label(text=f"00:45", color=(0, 0, 0, 1), font_size='40sp', size_hint_y=None)

        self.sits_text = Label(text='', color=(0, 0, 0, 1), font_size='20sp')

        self.temporizer_button = Button(text='', border = (30, 30, 30, 30), color=(0.3, 0.3, 0.3, 1), background_down="images/down.png", background_normal="images/normal.png")
        self.temporizer_button.bind(on_press=self.set_temporizer)
        self.next_button = Button(text='', color=(0.3, 0.3, 0.3, 1), border = (30, 30, 30, 30), background_down="images/down.png", background_normal="images/normal.png", size_hint=(0.4, 0.2), pos_hint={'center_x':0.5}, disabled=True)
        self.next_button.bind(on_press=self.next)

        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        main_layout.add_widget(self.instructions_text)
        main_layout.add_widget(self.counter)
        main_layout.add_widget(self.sits_text)
        main_layout.add_widget(self.temporizer_button)
        main_layout.add_widget(self.next_button)

        self.add_widget(main_layout)

    def set_temporizer(self, *args):
        print("temporizer has been started")
        self.sits_text.color = (0, 0, 0, 1)
        
        self.seconds_left = 45
        self.temporizer_button.disabled = True

        Clock.schedule_interval(self.update_timer, 1.0)

    def update_timer(self, dt):
        global languages, language
        self.seconds_left -= 1
        
        minutes = self.seconds_left // 60
        seconds = self.seconds_left % 60
        self.counter.text = f"{minutes:02}:{seconds:02}"

        if self.seconds_left <= 0:
            Clock.unschedule(self.update_timer)
            print("Finished")
            self.next_button.disabled = False
            self.temporizer_button.text = languages[language]["temporizer_restart"]
            self.temporizer_button.disabled = False
            return False

    def next(self, *args):
        app = App.get_running_app()
        app.root.current = "lastStep"
        app.root.transition.direction = "left"

    def on_enter(self, *args):
        global languages, language
        self.instructions_text.text = languages[language]["second_step"]
        self.sits_text.text = languages[language]["sits_step"]
        self.temporizer_button.text = languages[language]["temporizer_init"]
        self.next_button.text = languages[language]["next"]

class Pulse2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instructions_text = Label(text='', color=(0,0,0,1), font_size='20sp')
        first_pulse_text = Label(text='', color=(0,0,0,1), font_size='20sp')
        second_pulse_text = Label(text='', color=(0,0,0,1), font_size='20sp')

        self.input_pulse_1 = TextInput(multiline=False)
        self.input_pulse_2 = TextInput(multiline=False)

        self.button = Button(text='', color=(0.3, 0.3, 0.3, 1), border = (30, 30, 30, 30), background_down="images/down.png", background_normal="images/normal.png", size_hint=(0.4, 0.2), pos_hint={'center_x':0.5})
        self.button.on_press = self.next

        main_layout = BoxLayout(orientation="vertical")
        input_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=(1, '80sp'))
        input_2_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=(1, '80sp'))

        main_layout.add_widget(instructions_text)

        input_layout.add_widget(first_pulse_text)
        input_layout.add_widget(self.input_pulse_1)

        input_2_layout.add_widget(second_pulse_text)
        input_2_layout.add_widget(self.input_pulse_2)

        main_layout.add_widget(input_layout)
        main_layout.add_widget(input_2_layout)

        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        global pulse_1, pulse_2, pulse_3, age, ruffier, results
        pulse_2 = int(self.input_pulse_1.text)
        pulse_3 = int(self.input_pulse_2.text)

        ruffier = ruffier_index(pulse_1, pulse_2, pulse_3)
        results = ruffier_results(ruffier, age)

        print(ruffier)
        print(results)

        app = App.get_running_app()
        app.root.transition.direction = "left"
        app.root.current = "results"

    def on_enter(self, *args):
        global language
        self.instructions_text.text = languages[language]["last_step"]
        self.first_pulse_text.text = languages[language]["first_pulse"]
        self.second_pulse_text.text = languages[language]["first_pulse"]
        self.button.text = languages[language]["next"]

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.results = Label(text="", color=(0, 0, 0, 1), font_size='20sp')
        self.restart_button = Button(text='', color=(0.3, 0.3, 0.3, 1), border = (30, 30, 30, 30), background_down="images/down.png", background_normal="images/normal.png",   size_hint=(0.4, 0.2), pos_hint={'center_x':0.5})
        self.restart_button.on_press = self.restart
        self.dev = Label(text='', color=(0, 0, 0, 1), font_size='20sp')

        self.main_layout = BoxLayout(orientation="vertical")

        self.main_layout.add_widget(self.results)
        self.main_layout.add_widget(self.dev)
        self.main_layout.add_widget(self.restart_button)

        self.add_widget(self.main_layout)

    def restart(self, *args):
        app = App.get_running_app()
        app.root.transition.direction = "left"
        app.root.current = "start"

    def on_enter(self, *args):
        global languages, language, results, ruffier
        self.results.text= f'{languages[language]["results"]} {results} {ruffier}'
        self.restart_button.text = languages[language]["restart"]
        self.dev.text = languages[language]["dev_message"]

class RuffierApp(App):
    def build(self):
        global language
        Window.clearcolor = (0.7, 0.7, 0.7, 1)
        manager = ScreenManager()

        manager.add_widget(WelcomeScreen(name="main"))
        manager.add_widget(StartScreen(name="start"))
        manager.add_widget(PulseScreen(name="firstStep"))
        manager.add_widget(WorkoutScreen(name="secondStep"))
        manager.add_widget(Pulse2Screen(name="lastStep"))
        manager.add_widget(ResultScreen(name="results"))

        return manager

if __name__ == '__main__':
    App = RuffierApp()
    App.run()

## NO VUELVO A TOCAR KIVY EN MI VIDA QUE COSA MAS FEA.