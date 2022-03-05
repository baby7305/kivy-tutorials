import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label

class RandomNumber(App):
  def build(self):
    return Label(text="Random Number Generator")

randomApp = RandomNumber()
randomApp.run()