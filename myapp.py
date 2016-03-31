from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import datetime

class MojGumb(Button):
	def __init__(self, datum, **kwargs):
		super().__init__(**kwargs)
		self.datum = datum

class MyApp(App):
	def build(self):
		layout = GridLayout(cols=7)
		datum = datetime.datetime.now()
		gumb = MojGumb(datum, text="{0}.{1}.{2}".format(datum.day, datum.month, datum.year))
		layout.add_widget(gumb)
		return layout

if __name__ == "__main__":
	MyApp().run()