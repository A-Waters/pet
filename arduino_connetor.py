import time
import serial

class arduino():
    def __init__(self, port='', speed=9600):
        self.SerialConnection = serial.Serial('/dev/ttyACM0',9600)
        time.sleep(2)

    def write_to(self, string):
        self.SerialConnection.write((string + '|').encode())

    def readline_from(self):
        return self.SerialConnection.readline().decode()

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


        

    
