# sender.py - The sender in the reliable data transfer protocol
import socket
import _thread
import udt

ACK_HEADER = 'A'
MSG_HEADER = 'M'
RECEIVER_IP = 'localhost'
RECEIVER_PORT = 8080
RECEIVER_ADDR = (RECEIVER_IP, RECEIVER_PORT)

packet_list = [];
packet_lock = _thread.allocate_lock()

# Adds a packet to the end of packet_list
def push_packet(packet):
    global packet_list
    global packet_lock
    
    packet_lock.acquire()
    packet_list.append(packet)
    packet_lock.release()

# Pops the packet from the front of packet_list
def pop_packet():
    global packet_list
    global packet_lock

    packet_lock.acquire()
    if len(packet_list) == 0:
        packet_lock.release()
        return None

    return packet_list.pop(0)
    packet_lock.release()

# Main function
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    sock.close()
