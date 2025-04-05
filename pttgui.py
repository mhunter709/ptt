import socket
import tkinter as tk
from tkinter import messagebox

# Configure the connection to Computer 1
server_ip = '10.0.0.108'  # Replace with the IP address of Computer Connected to Rig
server_port = 50007

# Create a socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))
except socket.error as e:
    messagebox.showerror("Connection Error", f"Could not connect to server: {e}")
    exit(1)

# Create the main application window
root = tk.Tk()
root.title("PTT Control")

# Variable to track the state of the PTT button
ptt_active = False

def toggle_ptt():
    global ptt_active
    if ptt_active:
        client_socket.sendall('PTT_OFF'.encode('utf-8'))
        ptt_button.config(text="PTT")
        ptt_active = False
    else:
        client_socket.sendall('PTT_ON'.encode('utf-8'))
        ptt_button.config(text="PTT (Active)")
        ptt_active = True

# Create a button for PTT
ptt_button = tk.Button(root, text="PTT", command=toggle_ptt, width=20, height=2)
ptt_button.pack(pady=20)

# Function to close the socket on exit
def on_closing():
    client_socket.close()
    root.destroy()

# Set the protocol for closing the window
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the GUI event loop
root.mainloop()

