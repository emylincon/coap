from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5683
path ="big"

client = HelperClient(server=(host, port))
response = client.get(path)
print(response.payload)
client.stop()
