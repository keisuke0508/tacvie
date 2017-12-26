import tkinter as tk
import tkinter.ttk as ttk
import constant


class TacvieAppBase:
    def make_app_base(self):
        self.root = tk.Tk()
        self.root.geometry(constant.WINDOW_SIZE)
        self.root.title(constant.APP_TITLE)
        self.make_app()
        self.root.mainloop()

    def make_app(self):
        self.set_title()
        self.set_movie_list()
        self.set_button()

    def set_title(self):
        title = constant.APP_TITLE
        font = constant.FONT
        size = constant.TITLE_FONT_SIZE
        title_label = tk.Label(text=title, font=(font, size))
        title_label.pack()

    def set_movie_list(self):
        self.movie = tk.StringVar()
        movie_list = ttk.Combobox(self.root, state='readonly',
                                  textvariable=self.movie)
        movie_list['values'] = constant.MOVIE_LIST
        movie_list.current(0)
        movie_list.bind('<<ComboboxSelected>>', self.select_movie)
        movie_list.place(x=30, y=200)

    def set_button(self):
        start_btn = tk.Button(text='start')
        end_btn = tk.Button(text='end')
        start_btn.bind('<Button-1>', self.start_btn_func)
        end_btn.bind('<Button-1>', self.end_btn_func)
        start_btn.place(x=30, y=250)
        end_btn.place(x=30, y=300)

    def select_movie(self, e):
        movie_title = self.movie.get()
        if movie_title == 'Not Select':
            pass
        elif movie_title == 'haptic.mov':
            pass
        elif movie_title == 'bicycle.mov':
            pass
        else:
            pass

    def start_btn_func(self, e):
        pass

    def end_btn_func(self, e):
        pass


class TacvieApp(TacvieAppBase):
    def tacvie_app(self):
        self.make_app_base()
