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

@app.route('/service/<service_number>', methods=['POST','GET'])
def place(service_number):
    if request.method =='POST':
        if request.values['place']=='Place Order':
            return render_template('index2.html',status="Order Success!", service=os.environ['SERVICE_NAME'], host=socket.gethostname(), host2=socket.gethostbyname(socket.gethostname()))
    return render_template('index2.html',status="")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
