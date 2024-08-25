from mapeamento import *
import network
import socket
import re
from machine import Pin, PWM
import time

ssid = ''
password = ''

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    print('Tentando conectar...')
    time.sleep(1)

lr = PWM(Pin(A_A), freq=5000, duty=0)  
lg = PWM(Pin(A_B), freq=5000, duty=0)  
lb = PWM(Pin(A_C), freq=5000, duty=0)  

def liga_led(r, g, b):
    lr.duty(r * 1023 // 255)  # 1023 é o máximo valor para PWM no MicroPython
    lg.duty(g * 1023 // 255)
    lb.duty(b * 1023 // 255)

pagina = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Escolha a cor do quadro</title>
    <style>
         body{
             background-color: bisque;
             display: flex;
             flex-direction: column;
             text-align: center;
         }   

         input{
             width: 150px;
             height: 100px;
         }

         button{
             font-size: 16px;
             width: 50px;
         }

    </style>
</head>
<body>
    <div>
    <h1>Ligue e desligue</h1>
    <button id="liga">ON</button>
    <button id="desliga">OFF</button>
    <h1>Escolha uma cor</h1>   
    <input type="color" id="cor">
    </div>

    <script>
        const fazRequisicao = function(url){
            console.log(url);
            let request = new XMLHttpRequest();
            request.open("GET", url, true);
            request.send();
        }

        document.getElementById("liga").addEventListener("click", function(){fazRequisicao("/liga");});
        document.getElementById("desliga").addEventListener("click", function(){fazRequisicao("/desliga");});
        document.getElementById("cor").addEventListener("change", function(){
            let corHexa = cor.value.toString().substring(1); // tira o #
            let r = parseInt(corHexa.substring(0,2),16);
            let g = parseInt(corHexa.substring(2,4),16);
            let b = parseInt(corHexa.substring(4,6),16);
            fazRequisicao(`/cor?r=${r}&g=${g}&b=${b}`);
        });
    </script>
</body>
</html>
"""

def lidar_requisicao(cliente):
    request = cliente.recv(1024)
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

    path = str(request).split(" ")[1]

    if path == "/":
        response +=  pagina
    elif path.startswith("/cor"):
        match = re.search(r"r=(\d+)&g=(\d+)&b=(\d+)", path)
        if match:
            r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
            liga_led(r, g, b)
    elif path == "/liga":
        liga_led(255, 255, 255)
    elif path == "/desliga":
        liga_led(0, 0, 0)

    cliente.send(response)
    cliente.close()

addr = wlan.ifconfig()[0]
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((addr, 80))
server.listen(5)

print("Servidor HTTP rodando em", addr)

while True:
    cliente, addr = server.accept()
    lidar_requisicao(cliente)
