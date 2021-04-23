import time
import serial

class arduino():
    def __init__(self, port='', speed=9600):
        self.SerialConnection = serial.Serial('/dev/ttyACM0',9600)
        time.sleep(2)

    def write_to(self, string):
        self.SerialConnection.write(string.encode())

    def readline_from(self, string):
        return self.SerialConnection.readline().decode()

    def LCD_print(self, string):
        if (len(string) > 8 ):
            self.write_to("LDC-1"+string)
        elif (len(string) < 16):
            self.write_to("LDC-1"+string[:8])
            self.write_to("LDC-2"+string[8:16])

        else:
            raise Exception("String To Large for LCD: '" + string + "'")


    
