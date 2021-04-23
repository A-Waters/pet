import pet
import time
import serial
import arduino_connetor as ac


def main():
    mypet = pet.pet("Danny")
    Arduino = ac.Ardiono('/dev/ttyACM0')

    while True:
        Arduino.write_to(mypet.get_state())
        time.sleep(1)


   


if __name__ == "__main__":
    main()
