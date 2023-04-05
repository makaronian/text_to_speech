import os
import tkinter as tk
from tkinter import filedialog
import pyttsx3
from langdetect import detect

class TextToSpeechApp:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')

        # Создание главного окна
        self.root = tk.Tk()
        self.root.title("Text to Speech")

        # Создание виджетов
        self.text_label = tk.Label(self.root, text="Введите текст, который нужно озвучить:")
        self.text_entry = tk.Entry(self.root, width=50)
        self.lang_label = tk.Label(self.root, text="")
        self.play_button = tk.Button(self.root, text="Озвучить", command=self.play_text)
        self.download_button = tk.Button(self.root, text="Загрузить .txt для воспроизведения", command=self.choose_file)

        # Размещение виджетов на главном окне
        self.text_label.pack()
        self.text_entry.pack()
        self.lang_label.pack()
        self.play_button.pack()
        self.download_button.pack()

    def run(self):
        self.root.mainloop()

    def play_text(self, text=''):
        text = self.text_entry.get()
        language = detect(text)
        self.lang_label.config(text=f"Язык текста: {language}")
        if language == 'ru':
            self.engine.setProperty('voice', self.voices[0].id)         # Русская Ирина
            self.engine.setProperty('rate', 150)                        # Настройка скорости воспроизведения
        elif language == 'en':
            self.engine.setProperty('voice', self.voices[2].id)         # Муриканский Давид
            self.engine.setProperty('rate', 150)
        else:
            self.engine.setProperty('voice', self.voices[1].id)         # Муриканская почему-то Зира
            self.engine.setProperty('rate', 150)
        self.engine.say(text)                                           # Озвучивание текста
        self.engine.runAndWait()                                        # Воспроизведение звука


    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if not os.path.exists(file_path):
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_text = f.read()
                language = detect(file_text)
                if language == 'ru':
                    self.engine.setProperty('voice', self.voices[0].id)  # Русская Ирина
                    self.engine.setProperty('rate', 150)  # Настройка скорости воспроизведения
                elif language == 'en':
                    self.engine.setProperty('voice', self.voices[2].id)  # Муриканский Давид
                    self.engine.setProperty('rate', 150)
                else:
                    self.engine.setProperty('voice', self.voices[1].id)  # Муриканская почему-то Зира
                    self.engine.setProperty('rate', 150)
                self.engine.say(file_text)
                self.engine.runAndWait()
        except OSError:
            print('Error with opening!')




if __name__ == "__main__":
    app = TextToSpeechApp()
    app.run()
