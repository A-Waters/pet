import pet
import time
import serial
import arduino_connetor as ac


def main():
    mypet = pet.pet("Danny")
    Arduino = ac.arduino('/dev/ttyACM0')

    while True:
        if mypet.get_state() != "":
            Arduino.LCD_print(mypet.get_state())
        else:
            Arduino.LCD_clear()

        time.sleep(10)
        print(mypet.get_state())


   


if __name__ == "__main__":
    main()
