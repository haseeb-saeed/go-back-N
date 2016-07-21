# receiver.py - The receiver in the reliable data transer protocol
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
        data, _ = udt.recv(sock)
        if not data:
            break
        
        # TODO: Remove the sequence number
        # Send back an ACK
        packet = str.encode(str(expected_num))
        udt.send(packet, sock, RECEIVER_ADDR)
        if seq_num == expected_num:
            expected_num += 1
            file.write(data)

    file.close()

# Main function
if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(RECEIVER_ADDR) 
    sock.close()
