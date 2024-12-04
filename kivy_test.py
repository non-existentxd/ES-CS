from kivy.app import App
from kivy.lang import Builder

class HelloWorldApp(App):
    def build(self):
        return Builder.load_file('main.kv')
    

HelloWorldApp().run()

#   Image:
#        source: ''
#        allow stretch: True
#        keep_ration: True