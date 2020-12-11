from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

choise = 1
krest = 0
nolik = 0

class GameApp(App):
    def tic_tac(self, input_button):
        global choise, krest, nolik
        if choise % 2 == 1:
            input_button.text = "X"
        else:
            input_button.text = "O"
        input_button.disabled = True
        choise = choise + 1

        vectora = (
            [self.button[x].text for x in (0,1,2)],
            [self.button[x].text for x in (3,4,5)],
            [self.button[x].text for x in (6,7,8)],

            [self.button[y].text for y in (0,3,6)],
            [self.button[y].text for y in (1,4,7)],
            [self.button[y].text for y in (2,5,8)],

            [self.button[d].text for d in (0,4,8)],
            [self.button[d].text for d in (2,4,6)]
        )

        for i in range(8):
            if vectora[i].count("X")==3:
                krest = krest + 1
                for i in range(9):
                    self.button[i].disabled = True
                self.label1.text = " Счет:" + str(krest) + ":" + str(nolik)
            elif vectora[i].count("O")==3:
                for i in range(9):
                    self.button[i].disabled = True
                nolik = nolik + 1
                self.label1.text = " Счет:" + str(krest) + ":" + str(nolik)
        print(nolik, krest)

    def restart(self, input_button):
        for i in range(9):
            self.button[i].disabled = False
            self.button[i].text = ""

    def build(self):
        box = BoxLayout(orientation="vertical")
        self.label1 = Label(text=" Счет: 0:0", size_hint=[1, .1])
        button1 = Button(text="Сыграть еще раз", size_hint=[1, .1], on_press=self.restart)
        bit = GridLayout(cols=3)
        self.button = [0 for i in range(9)]
        for i in range(9):
            self.button[i] = Button(on_press=self.tic_tac, font_size=36)
            bit.add_widget(self.button[i])
        box.add_widget(self.label1)
        box.add_widget(bit)
        box.add_widget(button1)
        return box


GameApp().run()
