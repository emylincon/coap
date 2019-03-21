from coapthon.server.coap import CoAP
from exampleresources import Big
import os

os.system('clear')
print('---------------------------------------')
print('Welcome to Coapthon3 Server Shell')
print('---------------------------------------')
print('\n')
print('Server is listening...')

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('big/', Big())

def main():
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")

if __name__ == '__main__':
    main()
