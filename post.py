from coapthon.client.helperclient import HelperClient
import sys

host = "127.0.0.1"
port = 5683
path ="big"


client = HelperClient(server=(host, port))
response = client.post(path, str(sys.argv[1]))
#print(response.payload)
client.stop()


