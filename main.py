import os
import sys
import json
import socket
import sqlite3
from flask import Flask, request, jsonify, render_template


ROOTPATH = os.path.dirname(sys.path[0])
PORT = 8025
server = True if socket.gethostname() == "hci.ecn.purdue.edu" else False
DEBUG = False

_URL_PREFIX = "/%02d/"%(PORT%100) if server else "/"

# create application
app = Flask(__name__, static_path=os.path.join(_URL_PREFIX, "static"))
app.config.from_object(__name__)
app.config.from_envvar("FLASKER_SETTINGS", silent=True)



@app.route( _URL_PREFIX + "flags", methods=["GET", "POST"])
def flags():
	mode = str(request.args.get("mode"))
	turkSubmitTo = request.args.get("turkSubmitTo")
	assignmentId = request.args.get("assignmentId")

	worker = ["A1UCX2JQRCSMFY","A2O4RICIH4QZU9", "A1K55Z90VSYU9W", "A1X0E744MFI5WQ", "A02XWUYRP5WE", "AKZNAHPWN51F8", "A3GMU9ITNE99SG", "A1ZNFJQBU3PIX5", "A3VC4X4D5SL1YV", "A38QND5IC0NC00"]
	worker_id = request.args.get("workerId")
	if worker_id in worker:
		return "You have done this HIT before, please return the HIT"
	else:
		return render_template("flags.html", mode=mode, turkSubmitTo=turkSubmitTo, assignmentId=assignmentId)


@app.route( _URL_PREFIX + "updateWorkerRecord", methods=["GET", "POST"])
def updateWorker():
	conn = sqlite3.connect("data.db")
	db = conn.cursor()
	worker_id = request.form["worker_id"]
	if worker_id is not None:
		db.execute("insert into worker(worker_id) values(?)", (worker_id,))
	conn.commit()
	conn.close()
	return "success"


if server:
    import flask_hci_server, flask_helpers
    flask_hci_server.adapt_for_crowd_server(app)

if __name__ == "__main__":
    if server:
        flask_helpers.main(app, port=PORT, host='127.0.0.1', debug=DEBUG)
    else:
        app.run(port=PORT, host='127.0.0.1', debug=DEBUG)
