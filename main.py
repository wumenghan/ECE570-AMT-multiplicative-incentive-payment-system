import os
import sys
import json
import socket
import sqlite3
from flask import Flask, request, jsonify, render_template


ROOTPATH = os.path.dirname(sys.path[0])
PORT = 8025
server = True if socket.gethostname() == "hci.ecn.purdue.edu" else False
DEBUG = True

_URL_PREFIX = "/%02d"%(PORT%100) if server else "/"

# create application
app = Flask(__name__, static_path=os.path.join(_URL_PREFIX, "static"))
app.config.from_object(__name__)
app.config.from_envvar("FLASKER_SETTINGS", silent=True)


@app.route( _URL_PREFIX + "flags", methods=["GET", "POST"])
def flags():
	mode = str(request.args.get("mode"))
	turkSubmitTo = request.args.get("turkSubmitTo")
	assignmentId = request.args.get("assignmentId")
	return render_template("flags.html", mode=mode, turkSubmitTo=turkSubmitTo, assignmentId=assignmentId)


if server:
    import flask_hci_server, flask_helpers
    flask_hci_server.adapt_for_crowd_server(app)

if __name__ == "__main__":
    if server:
        flask_helpers.main(app, port=PORT, host='127.0.0.1', debug=DEBUG)
    else:
        app.run(port=PORT, host='127.0.0.1', debug=DEBUG)
