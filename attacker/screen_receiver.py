import socket
import zlib

import pygame

# from server import WIDTH, HEIGHT
WIDTH = 1900
HEIGHT = 1000


def recvall(conn, length):
    """ Récupération de tous les pixels. """

    #print(length % 1024, 'ko')
    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def main(host='127.0.0.1', port=5000):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    with socket.socket() as sock:
        sock.connect((host, port))
        watching = True

        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break

            # Récupération de la taille de la taille des pixels, la taille des pixels et les pixels
            size_len = int.from_bytes(sock.recv(1), byteorder='big')
            size = int.from_bytes(sock.recv(size_len), byteorder='big')
            pixels = recvall(sock, size)
            pixels = zlib.decompress(pixels)

            # Création d'une Surface depuis les pixels brutes
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')

            # Affichage de l'image
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)


if __name__ == '__main__':
    import argparse
    import sys
    
    cli_args = argparse.ArgumentParser()
    cli_args.add_argument('--host', default='127.0.0.1', type=str)
    cli_args.add_argument('--port', default=5000, type=int)
    options = cli_args.parse_args(sys.argv[1:])
    
    main(host=options.host, port=options.port)