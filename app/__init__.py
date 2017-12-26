import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
import constant
from connector import TacvieMain


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
        self.set_log_area()

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
        start_btn.place(x=constant.START_BTN_X, y=constant.START_BTN_Y)
        end_btn.place(x=constant.END_BTN_X, y=constant.END_BTN_Y)

    def set_log_area(self):
        self.logs = []
        font = constant.FONT
        size = constant.LOG_FONT_SIZE
        log_area = tk.Label(text=None, font=(font, size))
        log_area.place(x=constant.LOG_AREA_X, y=constant.LOG_AREA_Y)

    def start_btn_func(self, e):
        movie = self.movie.get()
        if movie == constant.NOT_SELECT:
            err_log = constant.LOG_NOT_SELECTED
            self.write_log(err_log)
        elif movie == constant.HAPTIC_MOVIE:
            TacvieMain().haptic_senbay_ver()
        elif movie == constant.BICYCLE_MOVIE:
            TacvieMain().bicycle_senbay_speed_ver()
        else:
            err_log = constant.LOG_INVALID
            self.write_log(err_log)

    def end_btn_func(self, e):
        pass

    def write_log(self, log):
        log = self.get_log(log)
        self.update_log(log)
        font = constant.FONT
        size = constant.LOG_FONT_SIZE
        logs = str()
        for l in self.logs:
            logs = logs + '\n' + l
        log_area = tk.Label(text=logs, font=(font, size))
        log_area.place(x=constant.LOG_AREA_X, y=constant.LOG_AREA_Y)

    def get_log(self, log):
        current_time = self.get_current_time()
        return current_time + ':\n' + log

    def update_log(self, log):
        self.logs.append(log)
        if(len(self.logs) > constant.LOG_LIMIT):
            self.logs.pop(constant.LOG_POP_NUM)

    def get_current_time(self):
        return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


class TacvieApp(TacvieAppBase):
    def tacvie_app(self):
        self.make_app_base()
