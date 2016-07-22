# udt.py - Unreliable data transfer using UDP
import random
import socket


# Send a packet across the unreliable channel
# Packet may be lost
def send(packet, sock, addr):
        sock.sendto(packet, addr)
    return

# Receive a packet from the unreliable channel
def recv(sock):
    packet, addr = sock.recvfrom(1024)
    return packet, addr
