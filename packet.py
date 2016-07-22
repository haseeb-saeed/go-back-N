# packet.py - Packet-related functions

# Creates a packet from a sequence number and byte data
def make(seq_num, data = b''):
    seq_bytes = seq_num.to_bytes(4, byteorder = 'little', signed = True)
    return seq_bytes + data

# Creates an empty packet
def make_empty():
    return b''

# Extracts sequence number and data from a non-empty packet
def extract(packet):
    seq_num = int.from_bytes(packet[0:4], byteorder = 'little', signed = True)
    return seq_num, packet[4:]
