import random

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class MyRoot(BoxLayout):
    random_label = ObjectProperty(None)

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 2000))


class RandomNumber(App):
    def build(self):
        return MyRoot()


if __name__ == "__main__":
    RandomNumber().run()