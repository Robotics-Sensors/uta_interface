import roslaunch
import rospy
import time
import sys
import numpy as np
import csv
import os
import string
import pandas as pd
import cv2
import pyautogui
from sys import argv
import datetime
import matplotlib
import matplotlib.pyplot as plt
import pathlib
import datetime
from python_API.initialize_starting_and_goal_position import *
from python_API.record_screen import *
from python_API.multi_processing_threads.multi_processing import *
from python_API.launch_file_api import *
from python_API.utilities import *
import multiprocessing
import time

# Multi processing and being able to proccess
class multi_proccesing_thread_launch(object):
    def __init__(self, ros_launch_file , parent_launch_files, terminate_launch_files, node_server, thread = 3):
        self.number_of_threads = thread
        
        # Number of threads
        if self.number_of_threads == 3:
            self.proccesing_tread_1 = None
            self.proccesing_tread_2 = None
            self.proccesing_tread_3 = None

        # Parent launch files
        self.root_parent_launch_files = ros_launch_file

        # Function as auguments
        self.parent_launch_files = parent_launch_files
        self.terminate_launch_files = terminate_launch_files
        self.node_server = node_server
       
        # Determine when to terminate program
        self.determine_to_terminate = False

        # Determine the array it can be stored at to compare
        self.compare_server_nodes = None
        self.matching_node = "/checker_node"

        # Trigger to determine if it should terminate or not
        self.node_is_dead = None

        # Determine it it should continue or not
        self.parent_launch = None
        self.verify_launch = None
        self.server_launch = None

        # Current path minus the current directory
        self.absolute_path = os.path.abspath(os.getcwd()) + "/src/goal_checker_server/node_check_file/node_check.csv" 
        
        # Start function now 
        self.proccess_threads()


    def parent_process(self):

        # Launching the launch files that is stored in the array
        self.parent_launch = roslaunch.parent.ROSLaunchParent(self.root_parent_launch_files, self.parent_launch_files)
        self.parent_launch.start()


    def terminate_launch_process(self):

        # Terminates launch files processed
        self.verify_launch = roslaunch.parent.ROSLaunchParent(self.root_parent_launch_files, self.terminate_launch_files)
        self.verify_launch.start()


    def node_checker_process(self):
        
        # Node checker server launch file processed
        self.server_launch =  roslaunch.parent.ROSLaunchParent(self.root_parent_launch_files, self.node_server)
        self.server_launch.start()
 
    
    # It would be a function that keeps on checking if the file has been written in the csv file to then set the condition
    def node_reader_launch_process(self):

        # Ros run the scripts to for the server
        time.sleep(2)
        os.system("rosrun robot_navigation check_node_is_alive")
        os.system("rosrun robot_navigation check_node_is_alive_server")


    # Launch the rosrun so that it can be there for the one that it is for, it would read it so that it can determine when it is true or not
    def node_reader_process(self):
        
        # Sleep time before it does anything
        time.sleep(4)
        
        # Count for the loop
        count = 0

        # Reads the csv file to see if there is a node that has changed so that it can move on to the next one 
        with open(self.absolute_path, "r") as csvfileOutput:
            writer = csv.writer(csvfileOutput, delimiter=",")
            
            # Determine if it has seen the not seen the node
            while True:

                # When the input for the user will be saved it so it can be used later
                self.compare_server_nodes([self.node_server[count]])
                print("------------------------------------------------------ THE NODE PRINT OF SERVER STARTS HERE -------------------------------------:", self.compare_server_nodes)

                # Determine when it is time to reset or exit
                self.node_is_dead = None

                # Count for the loop
                count += 1 




    # Create threads from original pid
    def proccess_threads(self):
       
        # Create proccess threads
        self.proccesing_tread_1 = multiprocessing.Process(target=self.parent_process)
        self.proccesing_tread_2 = multiprocessing.Process(target=self.terminate_launch_process)
        self.proccesing_tread_3 = multiprocessing.Process(target=self.node_checker_process)

        # Thread for the robot navigation so that it does not have to know
        self.proccesing_tread_4 = multiprocessing.Process(target=self.node_reader_launch_process)
        self.proccesing_tread_5 = multiprocessing.Process(target=self.node_reader_process)

        # Thread to determine if it should terminate or not
        self.proccesing_tread_6 = multiprocessing.Process(target=self.terminate_process)

        # self.proccesing_tread_1.daemon = True

        # Start threads
        self.proccesing_tread_1.start()
        self.proccesing_tread_2.start()
        self.proccesing_tread_3.start()
        self.proccesing_tread_4.start()
        self.proccesing_tread_5.start()
        self.proccesing_tread_6.start()

        # Wait until the other proccess is finished
        self.proccesing_tread_2.join()
        # self.proccesing_tread_1.join()
        
        print("-------------------------second 1111111111111------------------------------------------------------------------------------------IT IS ALIVE", self.proccesing_tread_2.is_alive())
        



    def terminate_all_nodes_in_terminal(self):
        # Terminates everything
        os.system("killall -9 gazebo")
        os.system("killall -9 rviz")
        os.system("killall -9 gzserver")
        os.system("killall -9 gzclient")
        os.system("killall -9 rosmaster")


    # Terminates process
    def terminate_process(self):

        # Tell me if process 2 is still alive
        print("------------------------- second 222222222222222 --------------------------------------------------------------------------------------------IT IS ALIVE", self.proccesing_tread_2.is_alive())

        # Terminate video Process if  main process is dead
        if self.determine_to_terminate == False:
            time.sleep(100)

            print("------------------------- second 3333333333333 -------------------------------------------------------------------------------------IT IS ALIVE", self.proccesing_tread_2.is_alive())

            self.terminate_all_nodes_in_terminal()

            # Terminate every process when the condition is meet and it is time for to finish
            self.proccesing_tread_1.terminate()
            self.proccesing_tread_2.terminate()
            self.proccesing_tread_3.terminate()
            self.proccesing_tread_4.terminate()
            self.proccesing_tread_5.terminate()


        # Print when it is done with determinig and processing
        print("Terminate Node, Server and Launch Files!")
