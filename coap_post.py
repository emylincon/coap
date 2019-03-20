from coapthon.client.helperclient import HelperClient
import os

os.system('clear')
print('-----------------------------------')
print('Welcome to CoAP Post Agent')
print('-----------------------------------')
host = input('Enter Server Ip: ')
port = 5683
path = "big"
print('-----------------------------------')

client = HelperClient(server=(host, port))


def main():
    try:
        while True:
            msg = input('Input Post Command: ')
            client.post(path, msg)
            print('Post Agent: {}'.format(msg))
    except KeyboardInterrupt:
        print('\nProgramme Terminated')


if __name__ == '__main__':
    main()
