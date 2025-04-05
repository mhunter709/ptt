I'm working on developing a system to connect to my Yaesu FT-450D to connect to it remotely from another computer for digital modes and SSB.
CAT control for the FT-450D is provided by FLRig connected to the 9-pin serial DB-9 CAT jack through DigiRig Mobile.
I'm experimenting with routing both the digital mode audio and voice audio through the FT-450D 6-pin Data jack, also connected to the computer cia DigiRig mobile.
In this set up, clicking PTT on FLRig running remotely on another computer, connecting to FLRig running on the rig computer, triggers the PTT for the microphone
jack on the FT-450D, but not the Data jack on the back.
To solve this problem, I wrote two small pieces of software in Python

PTTServer.py --- This runs on the computer connected to the FT-450D and listens for a connection from a remote computer. If it gets one and a designated PTT
signal, then PTTServer.py will trigger the PTT on the 6-pin Data jack. 

Using a terminal, launch PTTServer.py with the following command "python3 PTTServer.py"

After PTTServer.py launches, then launch FLRig -- if you launch FLRig first, and the PTTServer.py, PTTServer.py seems to trigger the PTT on the rig immediately.

pttgui.py - This is a simple program that generates a PTT button in a box that you can click with a mouse. When clicked, it sends a signal to the PTTServer.py
program on the rig computer to trigger the PTT on the 6-pin Data jack. When you click the PTT button again, the PTT is released on the rig. In the code of the
pttgui.py software you will need to change the remote computer local network IP address to whatever the IP address is of the computer connected to the rig. 

Using a terminal, launch pttgui.py with the following command "python3 pttgui.py"

Using AudioRelay running on the remote and rig computers I have sucessfully routed the audio from a microphone connected to my remote computer, to the rig
computer and out through the 6-pin Data jack and successfully had one QSO (although remotes were my audio was undermodulated, something I'm working on). 

I've posted the PTTServer and pttgui code here for information only and like the license says, I offer no warranty or promise about functionality. Use at
your own risk! If it ruins your rig, computer, anything else, that's on you. 

73 and good luck,

Mark
VO1BS/VO1MCH
