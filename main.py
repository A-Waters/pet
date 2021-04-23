import pet
import time
import serial
import arduino_connetor as ac


def main():
    mypet = pet.pet("Danny")
    Arduino = ac.Ardiono('/dev/ttyACM0')

    while True:
        Arduino.LCD_print("01234567")
        time.sleep(2)


   


if __name__ == "__main__":
    main()
