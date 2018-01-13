import flask as f
import connector.constant as constant
import connector.url as url
from connector import ActuationMain


app = f.Flask(__name__)


@app.route('/')
def get():
    title = get_title()
    movie_list = get_movie_list()
    selected_movie = None
    movie_url = url.INITIAL_URL
    return f.render_template(constant.MAIN_URL,
                             title=title,
                             movie_list=movie_list,
                             selected_movie=selected_movie,
                             movie_url=movie_url
                             )


@app.route('/post', methods=['POST'])
def post():
    title = get_title()
    movie_list = get_movie_list()
    err_log = None
    if "start" in f.request.form:
        selected_movie = f.request.form['movie']
        movie_url = get_movie_url(selected_movie)
        # err_log = actuation(selected_movie)
    elif "end" in f.request.form:
        selected_movie = None
        movie_url = url.INITIAL_URL
    return f.render_template(constant.MAIN_URL,
                             title=title,
                             movie_list=movie_list,
                             selected_movie=selected_movie,
                             movie_url=movie_url,
                             err_log=err_log
                             )


def get_title():
    return constant.SYSTEM_NAME


def get_movie_list():
    return constant.MOVIE_LIST


def get_movie_url(movie):
    if movie == 'haptic.mov':
        movie_url = url.HAPTIC_URL
    elif movie == 'bicycle.mov':
        movie_url = url.BICYCLE_URL
    return movie_url


def actuation(movie):
    try:
        if movie == 'haptic.mov':
            ActuationMain().haptic_senbay_ver()
        elif movie == 'bicycle.mov':
            ActuationMain().bicycle_senbay_speed_ver()
        return
    except Exception as err_log:
        return err_log


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
