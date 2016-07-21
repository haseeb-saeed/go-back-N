# udt.py - Unreliable data transfer using UDP
import random
import socket

DROP_PROB = 4

# Send a packet across the unreliable channel
# Packet may be lost
def send(packet, sock, addr):
    if random.randint(0, DROP_PROB) > 0:
        sock.sendto(packet, addr)
    return

# Receive a packet from the unreliable channel
def recv(sock):
    data, addr = sock.recvfrom(512)
    return packet, addr
