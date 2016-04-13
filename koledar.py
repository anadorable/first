import datetime
import calendar

mesec = calendar.month(datetime.datetime.now().year, datetime.datetime.now().month)
print(mesec.strip().split())

class MojGumb(Button):
	def __init__(self, dan, **kwargs):
		super().__init__(**kwargs)
		self.dan = dan

class App():
    def build(self):
        layout = GridLayout(cols=7)
        for dan in mesec[2:]:
            gumb = MojGumb(dan, text="{0}".format(dan))
		layout.add_widget(gumb)
		return layout

if __name__ == "__main__":
    App().run()
