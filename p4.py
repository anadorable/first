import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from datetime import date, timedelta
from functools import partial

##class DolociDatum(BoxLayout):
##    def __init__(self, *args, **kwargs):
##        super(DolociDatum, self).__init__(**kwargs)
##        self.datum = date.today()
##        self.orientacija = "vertical"
##        self.meseci = ('January', 'February', 'March', 'April', 'May', 'June',
##                       'July', 'August', 'September', 'October', 'November',
##                       'December')
##        if "meseci" in kwargs:
##            self.meseci = kwargs["meseci"]
##
##
##
##            
##
##
####import calendar
####import pprint
####
####koledar = calendar.monthcalendar(2007, 7)
####print(koledar)

class MyApp(App):
    def build(self):
        okno = GridLayout(cols=3)
        gumb = Button()
        okno.add_widget(gumb)

if __name__ == "__main__":
    MyApp().run()
