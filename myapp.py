from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import datetime
import calendar

##class MojGumb(Button):
##	def __init__(self, datum, **kwargs):
##		super().__init__(**kwargs)
##		self.datum = datum
##
####class MyApp(App):
####	def build(self):
####		layout = GridLayout(cols=7)
####		datum = datetime.datetime.now()
####		gumb = MojGumb(datum, text="{0}.{1}.{2}".format(datum.day, datum.month, datum.year))
####		layout.add_widget(gumb)
####		return layout
##
##class MyApp(App):
##        def build(self):
##                layout = GridLayout(cols=7)
##                mesec = calendar.month(datetime.datetime.now().year, datetime.datetime.now().month)
##                mesec = mesec.strip().split()
##                vrsta = 1
##                stolpec = 1
##                for dan in mesec[9:]:
##                        if stolpec > 7:
##                                stolpec = 1
##                        vrsta += 1
##                gumb = MojGumb(layout, text="{0}".format(dan))
##                layout.add_widget(gumb)
##                stolpec += 1
##		
##if __name__ == "__main__":
##	MyApp().run()




