# sender.py - The sender in the reliable data transfer protocol
import socket
import _thread
import udt

PACKET_SIZE = 512
RECEIVER_IP = 'localhost'
RECEIVER_PORT = 8080
RECEIVER_ADDR = (RECEIVER_IP, RECEIVER_PORT)
TIMER_STOP = -1
WINDOW_SIZE = 4

# Shared resources across threads
packets = []
mutex = _thread.allocate_lock()
base = 0
timer_start = TIMER_STOP

def send(filename, sock):
    global packets
    global mutex
    global base
    global timer_start

    # TODO: Open file
    # Add all the packets to the window
    while True:
        data = file.read(PACKET_SIZE)
        if not data:
            break
        packets.append(data)

    num_packets = len(packets)
    next_to_send = 0
    base = 0

    # Start the receiver thread
    _thread.start_new_thread(receive, (sock,))

    # Check the next to send and see if it's in the window
    # If so, send it
    # If no timer has started, start the timer for the packet
    # While we cannot send any more, and there has been no timeout, sleep for a little bit

def receive(sock):
    global mutex
    global base
    global timer_start

    while True:
        data = socket.recvfrom(sock, RECEIVER_ADDR);
        msg = data.decode('utf-8');
        ack = int(msg);

        # If we get an ACK for the first in-flight packet
        if (ack == base):
            mutex.acquire()
            base += 1
            timer_start = TIMER_STOP
            mutex.release()

        # Receive thread
        # Once we receive an ACK for the send packet, increment the window base
        # Stop the timer

# Main function
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.close()
