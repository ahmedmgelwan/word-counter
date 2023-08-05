from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self._bgcolor = '#37474F'
        self._color = '#ECEFF1'
        self._font = 'Courier'
        self.Gui()

    def Gui(self):
        self.title('Word Counter')
        # self.iconbitmap('/home/ahmed/Desktop/word_counter/icon.ico')
        self.config(bg=self._bgcolor, padx=15)
        APP_WIDTH = 400
        APP_HEIGHT = 700
        SCREEN_WIDTH, SCREEN_HEIGHT = self.winfo_screenwidth(), self.winfo_screenheight()
        x = int((SCREEN_WIDTH/2) - (APP_WIDTH/2))
        y = int((SCREEN_HEIGHT/2) - (APP_HEIGHT/2))
        self.geometry(
            f'{APP_WIDTH}x{APP_HEIGHT}+{x}+{y}'
        )
        title_label = Label(self, text='Word Counter App',
                            bg=self._bgcolor, fg=self._color, font=(self._font, '20', 'bold'))
        title_label.pack(pady=5)

        frame = Frame(self, bg=self._bgcolor, width=100, height=1)
        frame.config(highlightbackground=self._color, highlightthickness=1)
        frame.pack()

        input_box = Text(frame,  bg=self._bgcolor,
                         height=20, font=(self._font, '12'), fg=self._color, padx=10, pady=10)
        input_box.pack()

        count_btn = Button(self, pady=8, text='Count', bg=self._bgcolor,
                           command=lambda: self.print_all(input_box.get('1.0', 'end')))
        count_btn.pack(pady=10)
        self.char_var = StringVar()
        self.char_var.set('0')
        self.word_var = StringVar()
        self.word_var.set('0')
        self.upper_var = StringVar()
        self.upper_var.set('0')
        self.num_var = StringVar()
        self.num_var.set('0')

        self.label_creator('Chars', self.char_var)
        self.label_creator('Words', self.word_var)
        self.label_creator('Upper', self.upper_var)
        self.label_creator('Numbers', self.num_var)

    def label_creator(self, text, var):

        char_label = Label(bg=self._bgcolor, fg=self._color,
                           font=f'{self._font} 10 bold', text=f'{text}: ')
        char_label.pack(pady=10)

        chars = Label(bg=self._bgcolor, fg=self._color,
                      font=f'{self._font} 10 bold', textvariable=var)
        chars.pack()

    def print_all(self, text):
        all_counts = self.count(text)
        self.char_var.set(all_counts[0])
        self.word_var.set(all_counts[1])
        self.upper_var.set(all_counts[2])
        self.num_var.set(all_counts[3])

    def count(self, text):
        return (
            self.count_chars(text),
            self.count_words(text),
            self.count_upper(text),
            self.count_numeric(text)
        )

    def count_chars(self, text: str) -> int: return len(text)

    def count_words(self, text: str) -> int: return len(text.split())

    def count_upper(self, text: str):
        counter = 0
        for char in text:
            if char.isupper():
                counter += 1

        return counter

    def count_numeric(self, text: str):
        counter = 0
        for char in text:
            if char.isnumeric():
                counter += 1

        return counter


def main():
    app = App()
    app.title('Word Counter')
    app.mainloop()


if __name__ == '__main__':
    main()
