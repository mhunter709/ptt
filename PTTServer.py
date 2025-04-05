import socket
import serial

# Software to run on the computer connected to the FT-450D 9-pin serial DB-9 CAT jack
# Configure the serial connection to the FT-450D
ser = serial.Serial('/dev/cu.usbserial-141110', baudrate=38400, rtscts=False)

# Set up the server to listen for connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 50007))
server_socket.listen(1)

print("Waiting for connection from Remote Computer...")

# Accept a connection from Remote Computer
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

try:
    while True:
        # Receive data from Remote Computer
        data = client_socket.recv(1024).decode('utf-8')
        if data == 'PTT_ON':
            # Engage PTT
            ser.setRTS(True)
#            print("PTT Engaged")
        elif data == 'PTT_OFF':
            # Disengage PTT
            ser.setRTS(False)
#           print("PTT Disengaged")
finally:
    # Close connections
    client_socket.close()
    server_socket.close()
    ser.close()
Now

