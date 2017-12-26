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
        movie_list = ttk.Combobox(self.root, state=constant.STATE,
                                  textvariable=self.movie)
        movie_list['values'] = constant.MOVIE_LIST
        movie_list.current(constant.OPENING_MOVIE_SETTING)
        movie_list.place(x=constant.MOVIE_LIST_X, y=constant.MOVIE_LIST_Y)

    def set_button(self):
        start_btn = tk.Button(text=constant.START_BTN_TEXT)
        end_btn = tk.Button(text=constant.END_BTN_TEXT)
        start_btn.bind(constant.BTN_EVENT, self.start_btn_func)
        end_btn.bind(constant.BTN_EVENT, self.end_btn_func)
        start_btn.place(x=constant.BTN_X, y=constant.START_BTN_Y)
        end_btn.place(x=constant.BTN_X, y=constant.END_BTN_Y)

    def start_btn_func(self, e):
        print self.movie.get()

    def end_btn_func(self, e):
        pass


class TacvieApp(TacvieAppBase):
    def tacvie_app(self):
        self.make_app_base()
