# receiver.py - The receiver in the reliable data transer protocol
import packet
import socket
import udt

RECEIVER_IP = 'localhost'
RECEIVER_PORT = 8080
RECEIVER_ADDR = (RECEIVER_IP, RECEIVER_PORT)

# Receive packets from the sender
def receive(sock, filename):
    # TODO: Open the file for writing
    expected_num = 0
    while True:
        # Get the next packet from the sender
        pkt, _ = udt.recv(sock)
        if not pkt:
            break
        seq_num, data = packet.extract(pkt)
        
        # Send back an ACK
        pkt = packet.make(expected_num)
        udt.send(pkt, sock, RECEIVER_ADDR)
        if seq_num == expected_num:
            expected_num += 1
            file.write(data)

    file.close()

# Main function
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(RECEIVER_ADDR) 
    sock.close()
