from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def create_button(self):
        return Button(text = "кнопка")

if __name__ == "__main__":
    MyApp().run()