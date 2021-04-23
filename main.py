import pet
import time
import serial

ArduinoSerial = serial.Serial('/dev/ttyACM0',9600)


def main():
    # mypet = pet.pet("Danny")
    # mypet.live()

    print (ArduinoSerial.readline().decode())

    print ("you have a new message from ")

    while True:

        var = input(">>>>")

        if (var == '1'):
            ArduinoSerial.write('1'.encode())
            print("LED ON")


        if (var == '0'):
            ArduinoSerial.write('0'.encode())
            print("LED ON")

        time.sleep(1)


if __name__ == "__main__":
    main()
