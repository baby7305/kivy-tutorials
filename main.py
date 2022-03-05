import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RandomNumber(App):
  def build(self):
    return BoxLayout()

randomApp = RandomNumber()
randomApp.run()