import time
import serial

class Ardiono():
    def __inti__(self, Port='', speed=9600):
        self.SerialConnection = serial.Serial('/dev/ttyACM0',9600)
        time.sleep(2)

    def write_to(self, string):
        self.SerialConnection.write(string.encode())

    def readline_from(self, string):
        return self.SerialConnection.readline().decode()

