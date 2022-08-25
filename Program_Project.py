#chat app
from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import DataBase

view = Blueprint("views", __name__)

#GLOBAL CONSTANTS
NAME_KEY = 'name'
MSG_LIMIT = 20

#VIEWS

@view.route("/login", methods=["POST","GET"])
def login():
    """
    displays main login page and handles saving name in session
    :exception POST 
    :return:None"""

    if request.method == "POST": #if user input a name
        name = request.form["inputName"]
        if len(name) >= 2:
            session[NAME_KEY] = name