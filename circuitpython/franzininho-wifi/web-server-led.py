import ipaddress
import wifi
import socketpool
from adafruit_httpserver import Server, Request, Response # a instalação da lib não funcionou corretamente pelo thonny
from mapeamento import *
from pwmio import PWMOut

ssid=""
passwd=""

print("Conectando...")
print(wifi.radio.connect(ssid=ssid,password=passwd))

lr = PWMOut(A_A, frequency=5000, duty_cycle=0)
lg = PWMOut(A_B, frequency=5000, duty_cycle=0)
lb = PWMOut(A_C, frequency=5000, duty_cycle=0)

def liga_led(r,g,b): 
    lr.duty_cycle = r*64
    lg.duty_cycle = g*64
    lb.duty_cycle = b*64

  
pagina =  """
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
    <button id = "liga">ON</button>
    <button id = "desliga">OFF</button>
    <h1>Escolha uma cor</h1>   
    <input type = "color" id = "cor">
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
        document.getElementById("cor").addEventListener("mouseleave", function(){
            
            let corHexa = cor.value.toString().substring(1);// tira o #
            //manipulação das cores
            let r = parseInt(corHexa.substring(0,2),16);
            let g = parseInt(corHexa.substring(2,4),16);
            let b = parseInt(corHexa.substring(4,6),16);

            fazRequisicao(`/cor?r=${r}&g=${g}&b=${b}`);
        
        });

    </script>
</body>
</html>
"""
  
pool = socketpool.SocketPool(wifi.radio)

server = Server(pool, "/static", debug=True)


@server.route("/")
def base(request: Request):
    """
    Servir a página principal
    """
    return Response(request, pagina, content_type="text/html")

@server.route("/cor")
def setCor(request: Request):
    """
    Colore o Led
    """
    r = int(request.query_params["r"])
    g = int(request.query_params["g"])
    b = int(request.query_params["b"])
    
    liga_led(r,g,b)

    return Response(request)

@server.route("/liga")
def liga(request: Request):
    """
    liga o Led
    """    
    liga_led(255,255,255)

    return Response(request)

@server.route("/desliga")
def desliga(request: Request):
    """
    desliga o Led
    """
    
    liga_led(0,0,0)

    return Response(request)


server.serve_forever(str(wifi.radio.ipv4_address))
