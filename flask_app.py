from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from Tester.runner import run
from storage import list_runs
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)

@app.get("/")
def consignes():
     return render_template('consignes.html')

@app.route("/dashboard")
def dashboard():

    runs = list_runs()

    latencies = [r[2] for r in runs]
    ids = [r[0] for r in runs]

    return render_template(
        "dashboard.html",
        runs=runs,
        latencies=latencies,
        ids=ids
    )

@app.route("/run")
def run_test():

    run()

    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    # utile en local uniquement
    app.run(host="0.0.0.0", port=5000, debug=True)
