import time
import serial
import threading

class arduino():
    def __init__(self, port='', speed=9600):
        self.SerialConnection = serial.Serial('/dev/ttyACM0',9600)
        self.lock = threading.Lock()
        print("inside init")
        time.sleep(2)

    def write_to(self, string):
        self.lock.acquire()
        self.SerialConnection.write((string + '|').encode())
        self.lock.release()

    def readline_from(self):
        self.lock.acquire()
        data = self.SerialConnection.read_until(b'\n').decode()
        print("Data", data)
        self.lock.release()
        return data

    def LCD_print(self, string):
        if (len(string) >= 32):
            raise Exception("String To Large for LCD: '" + string + "'")
        elif (len(string) <= 16 ):
            self.write_to("LCD-1"+string)
        else:
            self.write_to("LCD-1"+string[:16])
            self.write_to("LCD-2"+string[16:])
    
    def LCD_clear(self):
        self.write_to("LCD-1")
        self.write_to("LCD-2")


        

    
