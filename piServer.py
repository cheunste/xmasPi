import subprocess
import socket
import threading

#CONSTANTS
#Interger Command to turn the power off
POWER_OFF=0
#Command to play music in spectrum mode
SPECTRUM_MODE=1
#TODO:Add import for the lightshow library and the PWM library

#create an INET socket
try:
    s=socket.socket()
except socket.error:
    print 'Failed to create socket'
    sys.exit()
#Remember, meaningful names
host=socket.gethostname()

#port number to bind to
port=12345

#Bind to port
s.bind((host,port))

#Let the socket listen to port
#Note. May not work and need to be put in background thread. See NOTE for accept()
s.listen(5)

def listenSocket():
    havePower=true
    while havePower:
        #read port
        
        """
        NOTE:
        I sincerely hope you have put a socket.close() or something similar in the android app.
        Also, you need to put the accept code somewhere else. The problem is that it will listen....the tree will
        never run the default light show. 
        
        Do you have to thread this?
        Can you make do with an interupt?
        """
        #c,addr=s.accept()
        #print "Got connection from ", addr

        #store the data received from socket to dataReceived
        dataReceived=s.recv(4096)

        #Parse dataReceived
        for data in dataRecieved:
            pass
            #TODO: Parse data.

        #If Client sends a POWER OFF command, break out of while loop and shutdown the pi. The c[0] is just a placeholder
        #if c[0] == POWER_OFF:
        #    havePower=False
        #    s.close()
        #    #perform subprocess command
        #    subprocess.call(["halt","-p"])

        #If client sends a spectrum mode command, then play music in spectrum mode
        #TODO: Implment
        #elif c[0] == SPECTRUM_MODE:
        #    pass

        #Any other command will result in the default method
        else:
            default()
    #Reaching here means the code has gotten out of the while loop and user have decided to close the raspberry pi
    #close the socket
    s.close()
   
    #TEST: If it gets to here, exit the system
    sys.exit()
    #Shut down the pi. NOTE: Needs to be sudo
    #subprocess.call(["halt","-p"])

#Thread the listenSocket function
socketThread=threading.Thread(target=listenSocket)
socketThread.start()

"""
This method calls on the methods from lightshow to start playing music and start a lightshow
"""
#TODO: Implement
def spectrum(songTitle):
    return 

"""
The default method displays certain light patterns.
"""
#TODO: Implement
def default():
    return
