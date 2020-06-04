from flask import Flask, render_template, url_for, Markup, redirect, request
from bs4 import BeautifulSoup
import requests as req

app = Flask(__name__, static_url_path='/static')
app.config['SECRETKEY'] = 'secretkey'


@app.route('/')
def index():
    response = req.get('https://chat.chatra.io/#hostId=qX33LcTDsgDLYJpiE&amp;mode=widget&amp;clientId=EBhRX-T6djPFsu_cMbc-WOCJXGVAk0w2sz8RoAUk&amp;lang=en&amp;currentPage=https%3A%2F%2Fgoflix.se%2Fthe-bellmen&amp;currentPageTitle=Watch%20The%20Bellmen%20online%20for%20free&amp;prevPage=https%3A%2F%2Fgoflix.se%2F%3Ffbclid%3DIwAR0jymro9VCHhVoCyfut5tJFTm4Pq2avnYJp-yK-2D97Vr7Mpe7p_WNJ8F0&amp;referrer=https%3A%2F%2Fl.facebook.com%2F')
    data = Markup(response.text)
    movie_soup = BeautifulSoup(response.text, 'html.parser')
    # print(movie_soup.findAll('div', attrs = {'class': 'w3l-movie-gride-agile'}))
    movie_list = movie_soup.findAll('div', attrs = {'class' : 'w3l-movies-grade-agile'})
    for list in movie_list:
        print(list.find('img'))
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run('localhost', 9000, debug = True)
# <iframe src="../../svop4/srv2?search=dwm-chernobyl-s01e01" id="toChange" scrolling="no" frameborder="0" width="700" height="430" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" __idm_frm__="2295" __idm_id__="391558145"></iframe>
# https://topeuropix.site/svop4/srv2?search=dwm-chernobyl-s01e01
# <iframe width="640" height="365" src="//ok.ru/videoembed/2687159372470" frameborder="0" allow="autoplay" allowfullscreen=""></iframe>