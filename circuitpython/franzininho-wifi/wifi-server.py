import time
import ipaddress
import wifi
import socketpool
from adafruit_httpserver import Server, Request, Response

ssid=""
passwd=""


print("Conectando...")
print(wifi.radio.connect(ssid=ssid,password=passwd))
#print("Meu IP", wifi.radio.ipv4_address)

pool = socketpool.SocketPool(wifi.radio)

server = Server(pool, "/static", debug=True)

@server.route("/")
def base(request: Request):
    """
    Serve a default static plain text message.
    """
    return Response(request, "Hello from the CircuitPython HTTP Server!")


server.serve_forever(str(wifi.radio.ipv4_address))
