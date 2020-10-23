#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, url_for
from .methods import ParseMode

app = Flask(__name__)

@app.route('/_add_datas')
def add_datas():
    """
    XXX
    """

    input_user = request.args.get('place', type=str)
    place = ParseMode(input_user)

    if input_user == "":
        place.emptyInput()


    else:
        place.cleanInput()
        place.geocodingPlace()
        place.wikipediaSearch()

    print(place.address, place.lat, place.lng, place.wiki)
    return jsonify(address=place.address,
                   lat=place.lat,
                   lng=place.lng,
                   wiki=place.wiki)


# @app.route('/_add_datas')
# def add_datas():
#
#     input_user = request.args.get("place", type=str)
#     place = ParseMode(input_user)
#
#     placeJson = jsonify(adress = place.user_input)
#     return placeJson


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