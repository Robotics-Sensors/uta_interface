from python_API.header_imports import *
import multiprocessing
import time


# Able to handle multiprocessing and shutdown when it is needed
class processing_thread(multiprocessing.Process):
    def __init__(self):

        # Multi processing for the super
        multiprocessing.Process.__init__(self)
        self.exit = multiprocessing.Event()


    # Multiprocessing for the super
    def shutdown(self):
        print("Shutdown Proccess")
        self.exit.set()
    


# Multi processing and being able to proccess
class multi_proccesing_thread(object):
    def __init__(self, function_1, function_2, thread = 2):
        self.number_of_threads = thread
        
        # Number of threads
        if self.number_of_threads == 2:
            self.proccesing_tread_1 = None
            self.proccesing_tread_2 = None

        # Function as auguments
        self.function_1 = function_1 
        self.function_2 = function_2

        # Start function now 
        self.proccess_threads()



    # Create threads from original pid
    def proccess_threads(self):
       
        # Create proccess threads
        self.proccesing_tread_1 = multiprocessing.Process(target=self.function_1)
        self.proccesing_tread_2 = multiprocessing.Process(target=self.function_2)

        self.proccesing_tread_1.daemon = True

        # Start threads
        self.proccesing_tread_1.start()
        self.proccesing_tread_2.start()

        # Wait until the other proccess is finished
        self.proccesing_tread_2.join()

        # Terminate process to for video recording
        self.terminate_process()

        # Print
        print("Recording Process Done!")


    # Terminates process
    def terminate_process(self):
        
        # Terminate video Process if  main process is dead
        if not self.proccesing_tread_2.is_alive():
            time.sleep(2)
            self.proccesing_tread_1.terminate()




