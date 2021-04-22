import sched, time, internal_clock

class pet:
    def __init__(self, name):
        self.state = "Happy"
        self.alive = True
        
        self.max_hunger = 100
        self.hunger = 100
        self.hunger_threshold = 30
        self.hunger_state = "hungry"

        self.max_anger = 100
        self.anger = 100
        self.anger_threshold = 30
        self.anger_state = "angry"
        
        self.max_attention = 100
        self.attention = 100
        self.attention_threshold = 30
        self.attention_state = "lonely"
        
        self.max_tiereness = 100
        self.tiereness = 100
        self.tiered_threshold = 30
        self.tiered_state = "tiered"
        
        self.internal_clock = internal_clock.internal_clock()

        self.name = name

        self.internal_clock.add_job(self.lower_Hunger, 30, args=(1,))
        self.internal_clock.add_job(self.Anger, 50, args=(1,))
        self.internal_clock.add_job(self.Become_lonely, 20, args=(1,))
        self.internal_clock.add_job(self.tiered_out, 60, args=(1,))
        self.internal_clock.add_job(self.show_stats, 60, args=())
        self.internal_clock.run()
        
    def show_stats(self):
        print('Name: {}'.format(self.name))
        print('Hunger: {}/{}'.format(self.hunger, self.max_hunger))
        print('Anger: {}/{}'.format(self.anger, self.max_anger))
        print('Lonelyness: {}/{}'.format(self.attention, self.max_attention))
        print('Tieredness: {}/{}'.format(self.tiereness, self.max_tiereness))


    # Life is rough

    def lower_Hunger(self, x):
        if self.hunger - x > 0:
            self.hunger -= x
        
    def Anger(self, x):
        if self.anger - x > 0:
            self.anger -= x

    def Become_lonely(self,x ):
        if self.attention - x > 0:
            self.attention -= x

    def tiered_out(self, x):
        if self.tiereness - x > 0:
            self.tiereness -= x



    # uppers

    def raise_Hunger(self,x):
        if self.hunger + x < self.max_hunger:
           self.hunger += x

    def calm(self,x):
        if self.anger + x < self.max_anger:
           self.anger += x
    
    def give_attention(self,x):
        if self.attention + x < self.max_attention:
           self.attention += x
    
    def rest(self,x):
        if self.tiereness + x < self.max_tiereness:
           self.tiereness += x
    



    # Mood Getters

    def isHungry(self, threshold):
        if self.hunger <= threshold:
            return True
        else:
            return False

    def isAnrgy(self, threshold):
        if self.anger <= threshold:
            return True
        else:
            return False

    def isLonely(self, threshold):
        if self.attention <= threshold:
            return True
        else:
            return False

    def isTiered(self, threshold):
        if self.tiereness <= threshold:
            return True
        else:
            return False




    # main
    def live(self):
        while self.alive:
            current = self.get_state()
            if current != "":
                print(current)
            time.sleep(10)

    def get_state(self):
        curr_state = ""
        if self.isHungry(self.hunger_threshold):
            curr_state += self.hunger_state
        
        if self.isAnrgy(self.anger_threshold):
            curr_state += self.anger_state

        if self.isLonely(self.attention_threshold):
            curr_state += self.attention_state

        if self.isTiered(self.tiered_threshold):
            curr_state += self.tiered_state
        
        return curr_state