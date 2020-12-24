# -*- coding: utf-8 -*-
"""
Created on Dec 02 2020

@autor Tiz
"""
import socket

def main(host='127.0.0.1', port=5000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    BUFFER_SIZE = 1024
    print("host:",host,"\nport:",port)
    s.connect((host, port))
    message = s.recv(BUFFER_SIZE).decode()
    print("Server:", message)#First message of the server to know it's connected


    while True:
        command = input("Enter the command you wanna execute:")
        s.send(command.encode())

        if command.lower() == "exit":
            break

        results = s.recv(BUFFER_SIZE).decode()
        print(results)
      
    s.close()

if __name__ == '__main__':
    import argparse
    import sys
    
    cli_args = argparse.ArgumentParser()
    cli_args.add_argument('--host', default='127.0.0.1', type=str)
    cli_args.add_argument('--port', default=5000, type=int)
    options = cli_args.parse_args(sys.argv[1:])
    
    main(host=options.host, port=options.port)