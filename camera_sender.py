#!/usr/bin/env python

from __future__ import division
import cv2
import numpy as np
import socket
import struct
import math
import threading
MAX_DGRAM = 2**16
MAX_IMAGE_DGRAM = MAX_DGRAM - 64 # extract 64 bytes in case UDP frame overflown


def capturevid(conn):

    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        _, frame = cap.read()
        compress_img = cv2.imencode('.jpg', frame)[1]
        dat = compress_img.tostring()
        size = len(dat)
        count = math.ceil(size/(MAX_IMAGE_DGRAM))
        array_pos_start = 0
        while count:
            array_pos_end = min(size, array_pos_start + MAX_IMAGE_DGRAM)
            conn.send(struct.pack("B", count)  +dat[array_pos_start:array_pos_end])
            array_pos_start = array_pos_end
            count -= 1
    cap.release()
    cv2.destroyAllWindows()
    conn.close()

def camsender(port=5000):
    host="0.0.0.0"
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(5)
        print('Server started.')

        while 'connected':
            conn, addr = sock.accept()
            print('Client connected IP:', addr)
            thread = threading.Thread(target=capturevid, args=(conn,))
            thread.start()


if __name__ == '__main__':
    import argparse
    import sys
    
    cli_args = argparse.ArgumentParser()
    cli_args.add_argument('--port', default=5000, type=int)
    options = cli_args.parse_args(sys.argv[1:])
    threadshell = threading.Thread(target=camsender,args=(options.port+2,)) #port 5001
    threadshell.start()