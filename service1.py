from flask import Flask
from flask import request, render_template
import os
import requests
import socket
import sys

app = Flask(__name__)

TRACE_HEADERS_TO_PROPAGATE = [
    'X-Ot-Span-Context',
    'X-Request-Id',

    # Zipkin headers
    'X-B3-TraceId',
    'X-B3-SpanId',
    'X-B3-ParentSpanId',
    'X-B3-Sampled',
    'X-B3-Flags',

    # Jaeger header (for native client)
    "uber-trace-id",

    # SkyWalking headers.
    "sw8"
]

class Reservation:
    def __init__(self, name, people, cel, date):
        self.name = name
        self.people = people
        self.cel = cel
        self.date = date

reservationArray = []

@app.route('/service/<service_number>', methods=['POST','GET'])
def hello(service_number):
    print (
        'Hello from behind Envoy (service {})! hostname: {} resolved'
        'hostname: {}\n'.format(
            os.environ['SERVICE_NAME'], socket.gethostname(),
            socket.gethostbyname(socket.gethostname())))
    if request.method =='POST':
        if request.values['send']=='send':
            reservation = Reservation(request.values['user'], request.values['people'], request.values['phone-number'], request.values['reserved_date'])
            reservationArray.append(reservation)
            return render_template('index1.html',service=os.environ['SERVICE_NAME'],hostnameOne=socket.gethostname(),hostnameTwo=socket.gethostbyname(socket.gethostname()))
    return render_template('index1.html',service=os.environ['SERVICE_NAME'],hostnameOne=socket.gethostname(),hostnameTwo=socket.gethostbyname(socket.gethostname()))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
