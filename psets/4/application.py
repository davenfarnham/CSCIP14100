"""Implements a site via which users can look up stocks' prices."""

# import Flask, plus support for redirects, rendering templates, and accessing requests' parameters
from flask import Flask, redirect, render_template, request

# create an instance of Flask
app = Flask(__name__)

@app.route("/")
def index():
    """displays form"""
    return render_template("index.html")

@app.route("/quote")
def quote():
    """once implemented fully, gets stock quote from Yahoo! Finance"""
    return render_template("quote.html")

# http://cscip-14100-davenf.c9.io/
# if the script is executed directly from the Python interpreter and not used as an imported module
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
