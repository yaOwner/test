from kivy.app import App   

from kivy.uix.widget import Widget  
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image, AsyncImage

from kivy.config import Config

from kivy.animation import Animation

import random

from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button

from collections import deque # главное

Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '700');
Config.set('graphics', 'height', '390');

Builder.load_string("""
<Gex>:
	Label:
		id: fer
		text:"..."
		pos: 305, 325

""")
class Gex(Widget):
	def __init__(self, **kwargs):
		super(Gex, self).__init__(**kwargs)
		self.name_one = TextInput(multiline = False,pos = (275, 325),size = (200, 60))
		self.add_widget(self.name_one)

		self.name_two = TextInput(multiline = False,pos = (275, 265),size = (200, 60))
		self.add_widget(self.name_two)

		self.name_three = TextInput(multiline = False,pos = (275, 205),size = (200, 60))
		self.add_widget(self.name_three)

		self.name_four = TextInput(multiline = False,pos = (275, 145),size = (200, 60))
		self.add_widget(self.name_four)

		self.wid = Widget()
		self.wid.add_widget(Button(text = 'Играть', size = (140, 40), pos = (305, 0), on_press = self.play))
		self.add_widget(self.wid)


	def play(self,instance):
		anim = Animation(x = 275, y = 800, duration = 0)
		anim.start(self.name_one)

		anim_two = Animation(x = 275, y = 800, duration = 0.2)
		anim_two.start(self.name_two)

		anim_three = Animation(x = 275, y = 800, duration = 0.2)
		anim_three.start(self.name_three)

		anim_four = Animation(x = 275, y = 800, duration = 0.2)
		anim_four.start(self.name_four)

		anim_five = Animation(x = 305, y = 800, size = (140, 60), duration = 0.2)
		anim_five.start(instance)

		instance.add_widget(Button(text = 'Правда или Действие?', pos = (260, 235), size = (200, 60), on_press = self.upd))


		self.text_scrolls = []
		self.q = deque()
		while True:
			self.q.append(self.name_one.text)
			self.q.append(self.name_two.text)
			self.q.append(self.name_three.text)
			self.q.append(self.name_four.text)

	def upd(self, instance):
		self.ids['fer'].text = str(self.q.popleft())

		play = ['Правда', 'Действие']
		start = random.choice(play)
		instance.text = start

		if (start == 'Действие'):
			for i in range(1):
				self.wid = Button(
					text = 'Вопросы для действия',
					pos = (160, 180),
					size = (400, 55),
					on_press = self.questionAction,
					font_size = 13)
				self.add_widget(self.wid)

		if (start == 'Правда'):
			for i in range(1):
				self.wid = Button(
					text = 'Вопросы для правды',
					pos = (160, 180),
					size = (400, 55),
					on_press = self.questionTruth,
					font_size = 13)
				self.add_widget(self.wid)

	def questionAction(self, instance):
		pass

	def questionTruth(self, instance):
		pass

class FakeApp(App):
	def build(self):
		return Gex()

if __name__ == '__main__':
	FakeApp().run()