import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

class RandomNumber(App):
  def build(self):
    return MyRoot()

randomApp = RandomNumber()
randomApp.run()