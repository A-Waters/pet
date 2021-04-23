import pet
import time
import serial
import arduino_connetor as ac


def main():
    mypet = pet.pet("Danny")
    Arduino = ac.arduino('/dev/ttyACM0')

    while True:
        data = input()
        Arduino.LCD_print(data)
        time.sleep(2)


   


if __name__ == "__main__":
    main()
