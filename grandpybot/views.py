#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, url_for
from .methods import ParseMode, Gmaps, Wiki

app = Flask(__name__)

@app.route('/_add_datas')
def add_datas():
    """
    XXX
    """

    request_user = request.args.get('place', type=str)
    place = ParseMode(request_user)
    
    if request_user == "":
        place.emptyInput()
        wiki = None

    else:
        place.cleanInput()
        place = Gmaps(place.user_input_cleaned)
        place.geocodingPlace()
        
        wiki = Wiki(place.lat, place.lng)
        wiki.title()
        wiki.content()
        wiki = wiki.content_wiki

    return jsonify(address=place.address,
                   lat=place.lat,
                   lng=place.lng,
                   wiki=wiki)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__ == "__main__":
    app.run()