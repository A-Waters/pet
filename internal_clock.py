import threading
import time

 
class internal_clock:
    ''' simple class used for indepenednt multithreaded schedueling'''
    def __init__(self):
        self.Live_jobs = []
        self.running = False

    def add_job(self, target_func='', delay=60, args=()):
        ''' add a job to be started when start func is called '''
        if target_func == '':
            raise Exception('target_func must be assigned')

        self.Live_jobs.append(threading.Thread(target=self.loop_job, args=( (delay, target_func) + args )))

    
    def loop_job(self, delay, function, args=()):
        ''' used to loop the functions while adding delays inbetween '''
        time.sleep(delay)
        if self.running == True:
            
            if args != ():
                function(args)
            else:
                function()
            
            self.loop_job(delay, function, args)

    def run(self):
        ''' run all the functions that were added with add func '''
        if self.running == False:
            for job in self.Live_jobs:
                job.daemon = True
                job.start()
            
            self.running = True
        
        else:
            raise Exception('Internal Clock Already Running, Need to Call End() to run more jobs')


    def end(self):
        ''' stop rerunning threads and empty job list'''
        self.running = False
        self.Live_jobs = []


    
            

    


    

