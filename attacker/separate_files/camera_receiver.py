#!/usr/bin/env python

from __future__ import division
import cv2
import numpy as np
import socket
import struct

MAX_DGRAM = 2**16

def dump_buffer(s):
    """ Emptying buffer frame """
    while True:
        seg, addr = s.recvfrom(MAX_DGRAM)
        print(seg[0])
        if struct.unpack("B", seg[0:1])[0] == 1:
            print("finish emptying buffer")
            break

def main(host='127.0.0.1', port=5002):
    
    # Set up socket
    s = socket.socket()
    s.connect((host, port))
    dat = b''
    dump_buffer(s)

    while True:
        seg, addr = s.recvfrom(MAX_DGRAM)
        if struct.unpack("B", seg[0:1])[0] > 1:
            dat += seg[1:]
        else:
            dat += seg[1:]
            img = cv2.imdecode(np.fromstring(dat, dtype=np.uint8), 1)
            cv2.imshow('frame', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            dat = b''

    # cap.release()
    cv2.destroyAllWindows()
    s.close()

if __name__ == '__main__':
    import argparse
    import sys
    
    cli_args = argparse.ArgumentParser()
    cli_args.add_argument('--host', default='127.0.0.1', type=str)
    cli_args.add_argument('--port', default=5002, type=int)
    options = cli_args.parse_args(sys.argv[1:])
    
    main(host=options.host, port=options.port)