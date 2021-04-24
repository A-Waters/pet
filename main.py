import pet
import time
import serial
import arduino_connetor as ac
import threading


def main():
    mypet = pet.pet("Danny")
    Arduino = ac.arduino('/dev/ttyACM0')

    t1 = threading.Thread(target=start_sending, args=(Arduino, mypet))
    t2 = threading.Thread(target=start_reciving, args=(Arduino, mypet))
    t1.start()
    t2.start()
    t1.join()
    t2.join()




def start_reciving(Arduino, mypet):
    while True: 
        data = Arduino.readline_from().rstrip()
        if data == "feelgood":
            mypet.set_Anger(100)
            mypet.set_Hunger(100)
            mypet.set_Lonelyness(100)
            mypet.set_Tieredness(100)


def start_sending(Arduino, mypet):
    current_state = ""

    while True:
        if current_state != mypet.get_state():
            
            if mypet.get_state() != "":
                Arduino.write_to("State:Triggered")
                Arduino.LCD_print(mypet.get_state())

            else:
                Arduino.write_to("State:Not")
                Arduino.LCD_clear()
            
            current_state = mypet.get_state()

        
        time.sleep(1)
        print(last_state)


if __name__ == "__main__":
    main()
