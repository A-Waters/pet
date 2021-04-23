import pet
import time
import serial
import arduino_connetor as ac


def main():
    mypet = pet.pet("Danny")
    Arduino = ac.arduino('/dev/ttyACM0')

    last_state = ""
    while True:
        data = Arduino.readline_from()
        print("waiting on you babe")

        if data == "feelgood":
            mypet.anger = 100
            mypet.hunger = 100
            mypet.tiereness = 100
            mypet.attention = 100


        if mypet.get_state() != "":
            Arduino.LCD_print(mypet.get_state())
            Arduino.write_to("State:Triggered")
            last_state = mypet.get_state()
        else:
            Arduino.LCD_clear()
            if last_state != "":
                Arduino.write_to("State:NotTriggered")
                last_state=""
        
        time.sleep(1)


   


if __name__ == "__main__":
    main()
