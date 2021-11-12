from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


saveInput = ''

class CalculatorApp(App):
    def build(self):
        Window.size = (300, 300)
        root = BoxLayout(orientation='vertical', padding=5)

        self.result = TextInput(
            text = '', readonly = True, font_size = 25,
            size_hint = [1,.2], background_color = [1,1,1,.8]
        )
        root.add_widget(self.result)

        allButtons = GridLayout(cols=4)

        allButtons.add_widget(Button(text='('))
        allButtons.add_widget(Button(text=')'))
        allButtons.add_widget(Button(text='<'))
        allButtons.add_widget(Button(text='Clear'))
        
        allButtons.add_widget(Button(text='%'))
        allButtons.add_widget(Button(text='//'))
        allButtons.add_widget(Button(text='х²'))
        allButtons.add_widget(Button(text='√x'))

        allButtons.add_widget(Button(text='7'))
        allButtons.add_widget(Button(text='8'))
        allButtons.add_widget(Button(text='9'))
        allButtons.add_widget(Button(text='+'))
        
        allButtons.add_widget(Button(text='4'))
        allButtons.add_widget(Button(text='5'))
        allButtons.add_widget(Button(text='6'))
        allButtons.add_widget(Button(text='-'))
        
        allButtons.add_widget(Button(text='1'))
        allButtons.add_widget(Button(text='2'))
        allButtons.add_widget(Button(text='3'))
        allButtons.add_widget(Button(text='*'))
        
        allButtons.add_widget(Button(text='.'))
        allButtons.add_widget(Button(text='0'))
        allButtons.add_widget(Button(text='='))
        allButtons.add_widget(Button(text='÷'))

        root.add_widget(allButtons)
        return root

if __name__ == '__main__':
    CalculatorApp().run()