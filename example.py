from kivy.app import App  # Импортирует главный класс для запуска формы
from kivy.uix.label import Label  # Импортирует поле вывода текста(Label)
from kivy.uix.button import Button  # Импортирует кнопку
"""
Импортирует окно, в которое можно поместить несколько виджетов. Также можно менять расположение виджетов внутри него.
То есть добавлять отступы, менять ориентацию и т.д.
Называть будем родительским окном. Виджеты внутри - дочерние
"""
from kivy.uix.boxlayout import BoxLayout


class MyFirstApp(App):  # Создает форму для приложения

    # Запускает приложения и методы(функции в форме)
    def build(self):
        root = BoxLayout()
        return root


# Запускаем приложение
MyFirstApp().run()
