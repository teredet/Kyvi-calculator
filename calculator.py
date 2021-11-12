from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


saveInput = ''

class CalculatorApp(App):
    def calculate(self, symbol):
        global saveInput
        if symbol.text is 'Clear':
            saveInput = self.result.text = ''
        elif symbol.text is '<':
            saveInput = self.result.text = self.result.text[:-1]
        elif symbol.text is '÷':
            self.result.text += '/'
            saveInput += '/'
        elif symbol.text is 'х²':
            self.result.text += '**2'
            saveInput += '**2'
        elif symbol.text is '√x':
            self.result.text += '**(1/2)'
            saveInput += '**(1/2)'
        elif symbol.text is not '=':
            self.result.text += symbol.text
            saveInput += symbol.text
        else:
            try: 
                print(self.result.text)
                saveInput = self.result.text = str(eval(saveInput))
                print(eval(saveInput))
            except: saveInput = self.result.text = ""

    def build(self):
        Window.size = (300, 300)
        root = BoxLayout(orientation='vertical', padding=2)

        self.result = TextInput(
            text = '', readonly = False, font_size = 25, 
            size_hint = [1,.2], background_color = [1,1,1,.5],
            foreground_color = (1,1,1,1), cursor_color = (1,1,1,1)
        )
        root.add_widget(self.result)

        allButtons = GridLayout(cols=4)

        allButtons.add_widget(Button(text='(', on_press = self.calculate))
        allButtons.add_widget(Button(text=')', on_press = self.calculate))
        allButtons.add_widget(Button(text='<', on_press = self.calculate))
        allButtons.add_widget(Button(text='Clear', on_press = self.calculate))
        
        allButtons.add_widget(Button(text='%', on_press = self.calculate))
        allButtons.add_widget(Button(text='//', on_press = self.calculate))
        allButtons.add_widget(Button(text='х²', on_press = self.calculate))
        allButtons.add_widget(Button(text='√x', on_press = self.calculate))

        allButtons.add_widget(Button(text='7', on_press = self.calculate))
        allButtons.add_widget(Button(text='8', on_press = self.calculate))
        allButtons.add_widget(Button(text='9', on_press = self.calculate))
        allButtons.add_widget(Button(text='+', on_press = self.calculate))
        
        allButtons.add_widget(Button(text='4', on_press = self.calculate))
        allButtons.add_widget(Button(text='5', on_press = self.calculate))
        allButtons.add_widget(Button(text='6', on_press = self.calculate))
        allButtons.add_widget(Button(text='-', on_press = self.calculate))
        
        allButtons.add_widget(Button(text='1', on_press = self.calculate))
        allButtons.add_widget(Button(text='2', on_press = self.calculate))
        allButtons.add_widget(Button(text='3', on_press = self.calculate))
        allButtons.add_widget(Button(text='*', on_press = self.calculate))
        
        allButtons.add_widget(Button(text='.', on_press = self.calculate))
        allButtons.add_widget(Button(text='0', on_press = self.calculate))
        allButtons.add_widget(Button(text='=', on_press = self.calculate))
        allButtons.add_widget(Button(text='÷', on_press = self.calculate))

        root.add_widget(allButtons)
        return root

if __name__ == '__main__':
    CalculatorApp().run()