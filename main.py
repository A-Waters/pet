import pet
import time
import serial
import arduino_connetor as ac
import threading


def main():
    mypet = pet.pet("Danny")
    Arduino = ac.arduino('/dev/ttyACM0')

    threading.Thread(target=start_sending, args=(mypet, Arduino)).start().join()
    threading.Thread(target=start_reciving, args=(mypet, Arduino)).start().join()





def start_reciving(Arduino, mypet):
    while True: 
        data = Arduino.readline_from()

        if data == "feelgood":
            mypet.anger = 100
            mypet.hunger = 100
            mypet.tiereness = 100
            mypet.attention = 100


def start_sending(Arduino, mypet):
    last_state = ""
    while True:

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
        print(mypet.get_state())


if __name__ == "__main__":
    main()
