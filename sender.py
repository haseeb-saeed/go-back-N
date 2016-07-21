# sender.py - The sender in the reliable data transfer protocol
import socket
import _thread
import time
import udt

PACKET_SIZE = 512
RECEIVER_IP = 'localhost'
RECEIVER_PORT = 8080
RECEIVER_ADDR = (RECEIVER_IP, RECEIVER_PORT)
TIMEOUT_INTERVAL = 500
TIMER_STOP = -1
WINDOW_SIZE = 4
SLEEP_INTERVAL = 0.05

# Shared resources across threads
mutex = _thread.allocate_lock()
base = 0
timer_start = TIMER_STOP

# Sets the window size
def set_window_size(num_packets):
    global base
    return min(WINDOW_SIZE, num_packets - base)

# Check the next to send and see if it's in the window
# If so, send it
# If no timer has started, start the timer for the packet
# While we cannot send any more, and there has been no timeout, sleep for a little bit
def send(filename, sock):
    global mutex
    global base
    global timer_start

    # TODO: Open file
    # Add all the packets to the window
    packets = []
    while True:
        data = file.read(PACKET_SIZE)
        if not data:
            break
        packets.append(data)

    num_packets = len(packets)
    window_size = set_window_size(num_packets)
    next_to_send = 0
    base = 0

    # Start the receiver thread
    _thread.start_new_thread(receive, (sock,))

    # Send all the packets in the window
    mutex.acquire()
    while next_to_send < base + window_size:
        # TODO: Add sequence number of packet
        udt.send(packets[next_to_send], sock, RECEIVER_ADDR)
        next_to_send += 1

    # Start the timer
    # TODO: Make timer great again
    if timer_start == TIMER_STOP:
        timer_start = time.clock()

    # Wait until a timer goes off or we get an ACK
    while time_start != TIMER_STOP and time.clock() - time_start < TIMEOUT_INTERVAL:
        mutex.release()
        time.sleep(SLEEP_INTERVAL)
        mutex.acquire()

    if time_start != TIMER_STOP:
        # We looks like we timed out
        next_to_send = base
    else:
        window_size = set_window_size(num_packets)
    mutex.release()
    
# Receive thread
# Once we receive an ACK for the send packet, increment the window base
# Stop the timer
def receive(sock):
    global mutex
    global base
    global timer_start

    while True:
        msg, _ = udt.recv(sock);
        ack = int(msg);

        # If we get an ACK for the first in-flight packet
        if (ack >= base):
            mutex.acquire()
            base = ack + 1
            timer_start = TIMER_STOP
            mutex.release()

# Main function
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.close()
