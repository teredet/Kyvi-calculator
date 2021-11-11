from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


saveInput = ''

class CalculatorApp(App):
    def build(self):
        Window.size = (300, 100)
        root = BoxLayout(orientation='vertical', padding=5)

        self.result = TextInput(
            text = '', readonly = True, font_size = 25,
            size_hint = [1,.75], background_color = [1,1,1,.8]
        )

        root.add_widget(self.result)

        return root

if __name__ == '__main__':
    CalculatorApp().run()