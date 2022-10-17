from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (255/255, 186/255, 3/255, 1)


class CalcApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        self.solution = TextInput(multiline=False, readonly=False, halign="right", font_size=55, input_filter="float")
        self.memory_one = TextInput()
        self.memory_two = TextInput()

        memory_buttons = [
            ["M1", "M2", "MC"],
        ]
        for row in memory_buttons:
            h_layout = BoxLayout()
            for label in row:
                memory_buttons = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                memory_buttons.font_size = 30
                memory_buttons.background_color = [123/255, 250/255, 45/255, 1]
                memory_buttons.bind(on_press=self.on_memory_button_press)
                h_layout.add_widget(memory_buttons)
            main_layout.add_widget(h_layout)

        main_layout.add_widget(self.solution)

        buttons = [
            ["e", "π", "(", ")"],
            ["√", "<-", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["C", "0", ".", "="],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.font_size = 30
                button.background_color = [123/255, 250/255, 45/255, 1]
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def on_memory_button_press(self, instance):
        if instance.text == "M1":
            if self.memory_one.text == "":
                self.memory_one.text = self.solution.text
            else:
                self.solution.text += self.memory_one.text
        if instance.text == "M2":
            if self.memory_two.text == "":
                self.memory_two.text = self.solution.text
            else:
                self.solution.text += self.memory_two.text
        if instance.text == "MC":
            self.memory_one.text = ""
            self.memory_two.text = ""

    def on_button_press(self, instance):
        if instance.text == "C":
            self.solution.text = ""

        elif instance.text == "=":
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = "Error"

        elif instance.text == "%":
            self.solution.text += "*0.01"

        elif instance.text == "π":
            self.solution.text += "3.1415"

        elif instance.text == "√":
            self.solution.text += "**(0.5)"

        elif instance.text == "(":
            self.solution.text += "("

        elif instance.text == ")":
            self.solution.text = ")"

        elif instance.text == "<-":
            length_string = len(str(self.solution.text))
            delete_last = str(self.solution.text[:length_string-1])
            self.solution.text = delete_last

        elif instance.text == "e":
            self.solution.text += "2.71828183"

        else:
            self.solution.text += instance.text


if __name__ == '__main__':
    CalcApp().run()
