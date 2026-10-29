from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from functions import ruffier_index
from meow import *

## GLOBAL

name, age = '', 7
pulse_1 = 0
pulse_2 = 0
pulse_3 = 0

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        welcome_text = Label(text=txt_instruction)
        name_text = Label(text="ingrese su nombre")
        age_text = Label(text="ingrese su edad")

        self.input_name = TextInput(multiline=False)
        self.input_age = TextInput(multiline=False, text="7")

        self.button = Button(text="Comenzar el test", size_hint=(0.4, 0.2), pos_hint={'center_x':0.5})
        self.button.on_press = self.next()

        main_layout = BoxLayout(orientation="vertical")
        input_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=(1, '80sp'))
        input_2_layout = BoxLayout(padding=20, spacing=10, size_hint_y=None, size=(1, '80sp'))

        main_layout.add_widget(welcome_text)

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

        print(name, age)

        self.manager.current= 'firstStep'

            
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
        manager.add_widget(PulseScreen(name="firstStep"))
        #manager.add_widget(WorkoutScreen(name="main"))
        #manager.add_widget(Pulse2Screen(name="main"))
        #manager.add_widget(ResultScreen(name="main"))

        return manager

if __name__ == '__main__':
    App = RuffierApp()
    App.run()