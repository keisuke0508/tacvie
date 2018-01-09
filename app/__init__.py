import tkinter as tk
import tkinter.ttk as ttk
import sys
from datetime import datetime
import constant
from process import AppHapticProcesser, AppBicycleProcesser


class TacvieAppBase:
    def __init__(self):
        self.is_operated = False

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
        self.set_menu_bar()

    def set_title(self):
        title = constant.APP_TITLE
        font = constant.FONT
        size = constant.TITLE_FONT_SIZE
        title_label = tk.Label(text=title, font=(font, size))
        title_label.place(x=constant.TITLE_X, y=constant.TITLE_Y)

    def set_movie_list(self):
        self.movie = tk.StringVar()
        self.movie_list = ttk.Combobox(self.root, state=constant.STATE,
                                       textvariable=self.movie)
        self.movie_list['values'] = constant.MOVIE_LIST
        self.movie_list.current(constant.OPENING_MOVIE_SETTING)
        self.movie_list.place(x=constant.MOVIE_LIST_X, y=constant.MOVIE_LIST_Y)

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

    def set_menu_bar(self):
        menu_bar = tk.Menu(self.root)
        menu_tacvie = tk.Menu(menu_bar)
        self.root.configure(menu=menu_bar)
        menu_bar.add_cascade(label='Tacvie', menu=menu_tacvie)
        menu_tacvie.add_command(label='help', command=self.display_help)
        menu_tacvie.add_command(label='exit', command=self.exit_app)

    def start_btn_func(self, e):
        movie = self.movie.get()
        if movie == constant.NOT_SELECT:
            err_log = constant.LOG_NOT_SELECTED
            self.write_log(err_log)
        elif movie == constant.HAPTIC_MOVIE:
            try:
                self.is_operated = True
                processer = AppHapticProcesser()
            except Exception:
                err_log = constant.LOG_DISCONNECTED
                self.write_log(err_log)
            while self.is_operated:
                processer.process()
            processer.close()
        elif movie == constant.BICYCLE_MOVIE:
            try:
                self.is_operated = True
                processer = AppBicycleProcesser()
            except Exception:
                err_log = constant.LOG_DISCONNECTED
                self.write_log(err_log)
            while self.is_operated:
                processer.process()
            processer.close()
        else:
            err_log = constant.LOG_INVALID
            self.write_log(err_log)

    def end_btn_func(self, e):
        self.b = False

    def write_log(self, log=None):
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

    def display_help(self):
        log = 'help have not written.'
        self.write_log(log)

    def exit_app(self):
        sys.exit()


class TacvieApp(TacvieAppBase):
    def tacvie_app(self):
        self.make_app_base()
