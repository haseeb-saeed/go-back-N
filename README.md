# go-back-N

A Python version of reliable data transfer over UDP implemented using the go-back-N algorithm. This algorithm uses a sliding window to send
multiple packets to a receiver. If a packet or acknowledgement is lost, the sender re-transmits the entire window of packets.
This implementation will reliably copy a file from the sender's location to the receiver's location provided both the sender and
the receiver are running locally on the same machine.

To run the system:
* Run the receiver:
`python receiver.py [filename of the file to write to]`
* Run the sender:
`python sender.py [filename of file to read from]`
