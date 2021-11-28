from python_API.header_imports import *
from python_API.utilities import *
from python_API.multi_processing_threads.multi_processing_launch_files import *


class launch_api_for_navigation_stack_and_tuw(object):
    def __init__(self, input_augument, time_sleep=2, reset = "no", iterations = 1, loop_launch_file = 1 , loop_launch_file_iterations = 1, terminate_file_number = 1):
        
        # catkin build and source it everytime you you run the api
        # catkin_build_and_source_obj = catkin_build_and_source()

        self.time_sleep = time_sleep

        self.time_for_each_iteration = 100
        self.input_augument = input_augument
        self.ros_file_launch = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(self.ros_file_launch)

        # Getting all the necessary location for the for the csv file
        self.absolute_path = os.path.abspath(os.getcwd()) + "/python_API" + "/launch_files_data"
        self.launch_csv_file = self.absolute_path + "/launch_data.csv"

        # Inputs for the setup
        self.setup_input = 2

        # Determine if it should be reset or not
        self.reset = reset

        # Determine what Launch file should be looped and how much time you want to loop from it
        self.loop_launch_file = loop_launch_file
        self.loop_launch_file_iterations = loop_launch_file_iterations
        
        # The launch file that had to shutdown if it needs to
        self.parent_launch = None
        self.verify_launch = None
        
        # Number of the launch files that needs to be terminated
        self.terminate_launch_files = terminate_file_number


        # Terminate file architecture
        # self.terminate_launch = roslaunch.scriptapi.ROSLaunch()

        # Input array so that it stores all the input in one, so that it can be run with the terminate function for the multi proccesing thread
        self.store_all_launch_files = []
        self.store_terminate_file = []
        self.store_server_node_checker = []


        # Recording of the screen
        self.screen_recorder_obj = record_screen()
        self.screen_recorder = True
        
        # Date and time of them the folder needs to be created for the launch files
        date_and_time = datetime.datetime.now()
        self.test_date_and_time = "/test_on_date_" + str(date_and_time.month) + "_" + str(date_and_time.day) + "_" + str(date_and_time.year) + "_time_at_" + date_and_time.strftime("%H:%M") 

        # Determine if it is going to be navigation stack or tuw for the video recording
        self.video_path_name = ""

        # Interation for testing for custom and run all
        self.iterations = iterations 

        # Number of robots
        self.number_of_robots = 3
        
        # Level for the starting position
        # Path for input of the user array to be read for location
        self.starting_position_path = os.path.abspath(os.getcwd()) +  "/starting_position/" 
        # self.starting_position_path = "/starting_position/"

        # Save the starting position in an array
        self.starting_position_reader = []

        # Loop between there so that it does not overlap
        # Call the function that stores all the input position for all the robots
        overlap = skip_overlap(self.input_augument)
        if overlap == False:
            self.loop_starting_position()
        
        # ie: Make it so that you are able to test for each test name

        # File directory for
        self.path_for_record_save = ""

        # ie: Call the Multi proccessing class and determine how much tread you want it to have

        # ROS launch the first launch file
        if self.input_augument[1] == "run_test_navigation_stack_2d":

            # run test for navigation 2d and record video
            self.path_for_record_save = "/2d_navigation_stack/" 
            self.video_path_name = self.path_for_record_save + self.input_augument[2] + self.test_date_and_time

            # Determine how much launch file you want to be running with amount of auguments in the csv file
            multi_proccesing_thread_obj = multi_proccesing_thread(self.screen_recorder_api, self.robot_and_obstacle_bot_navigation_stack_2d, thread = 2)



        elif self.input_augument[1] == "run_test_navigation_stack_3d":

            # run test for navigation stack 3d and record video
            self.path_for_record_save = "/3d_navigation_stack/" 
            self.video_path_name = self.path_for_record_save + self.input_augument[2] + self.test_date_and_time

            # Determine how much launch file you want to be running with amount of auguments in the csv file
            multi_proccesing_thread_obj = multi_proccesing_thread(self.screen_recorder_api, self.robot_and_obstacle_bot_navigation_stack_3d, thread = 2)



        elif self.input_augument[1] == "run_test_standard_tuw":

            # run test for regular tuw and record video
            self.path_for_record_save = "/standard_tuw/" 
            self.video_path_name = self.path_for_record_save + self.input_augument + self.test_date_and_time
            
            # Determine how much launch file you want to be running with amount of auguments in the csv file
            multi_proccesing_thread_obj = multi_proccesing_thread(self.screen_recorder_api, self.robot_and_obstacle_bot_standard_tuw_simulation_launch, thread = 2)



        elif self.input_augument[1] == "run_test_modefied_tuw":

            # run test for tuw with move base local planner and record video 
            self.path_for_record_save = "/modified_tuw/" 
            self.video_path_name = self.path_for_record_save + self.input_augument[2] + self.test_date_and_time

            # Determine how much launch file you want to be running with amount of auguments in the csv file
            multi_proccesing_thread_obj = multi_proccesing_thread(self.screen_recorder_api, self.robot_and_obstacle_bot_modified_tuw_simulation_launch, thread = 2)



        elif self.input_augument[1] == "custom_launch_file":

            # run test for the custom file and record
            self.path_for_record_save = "/custom_launch_file/" 
            self.video_path_name = self.path_for_record_save + self.input_augument[2] + self.test_date_and_time

            # Determine how much launch file you want to be running with amount of auguments in the csv file
            multi_proccesing_thread_obj = multi_proccesing_thread(self.screen_recorder_api, self.custom_launch_file, thread = 2)



        elif self.input_augument[1] == "save_launch_files":

            # Saves the launch file as an input of 2 launch file together
            self.save_launch_data()



        elif self.input_augument[1] == "launch_all":

            # Launch all the files that are in the csv file
            # Loop for how many iteration there is and record the video
            for i in range(int(self.iterations)):

                # Launch path for where it should be imported, can know the path
                self.path_for_record_save = "/launch_all/" 
                self.video_path_name = self.path_for_record_save + self.input_augument[2] + self.test_date_and_time

                # Determine how much launch file you want to be running with amount of auguments in the csv file
                multi_proccesing_thread_obj = multi_proccesing_thread(self.screen_recorder_api, self.run_all_custom_launch_files, thread = 2)



        elif self.input_augument[1] == "launch_all_loop":

            # Launch all the files that are in the csv file
            # Loop for how many iteration there is and record the video
            for i in range(int(self.iterations)):
                
                print("loop1 -->",i)
                # Launch path for where it should be imported, can know the path
                self.path_for_record_save = "launch_all/" 
                self.video_path_name = self.path_for_record_save + self.input_augument[2] + self.test_date_and_time

                # Determine how much launch file you want to be running with amount of auguments in the csv file
                multi_proccesing_thread_obj = multi_proccesing_thread(self.screen_recorder_api, self.run_all_custom_launch_files_with_loops, thread = 2)



        elif self.input_augument[1] == "show_launch_files":

            # Shows all the launch files in the csv file
            self.show_current_files()


    # Loop to all the csv file, so that it can get the input for all 
    def loop_starting_position(self):

        # Name of the robot
        robot1 = "robot1"
        robot2 = "robot2"
        obstacle_bot = "obstacle_bot"
        
        self.read_starting_position_array(robot_name = robot1)
        self.read_starting_position_array(robot_name = robot2)
        self.read_starting_position_array(robot_name = obstacle_bot)

        # Remove the word for starting position
        for i in range(self.number_of_robots):
            self.starting_position_reader.remove('starting_position')

        # Remove it so that it can be like for the format wants it to be
        count = 2
        for i in range(self.number_of_robots):
            self.starting_position_reader.pop(count)

            # The plus is for the format
            count += 2

    

    # Checks for all the nodes to see if they ar a line or not acts like a server to see if it is dead or not
    def checker_nodes_server(self):
        
        launch1 = launch1 = ['robot_navigation', 'node_server.launch']

        roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)[0]
        roslaunch_args1 = launch1[2:]


        # launch file with auguments
        launch_files = (roslaunch_file1, roslaunch_args1)

        # stores the array so that it does not have to to launch it here
        self.store_server_node_checker.append(launch_files)

        
    
    # Shutdown feature for the API
    def shutdown_launch_file(self):
        
        # Shutdown everything if it meets the condition
        multi_proccesing_thread_obj = multi_proccesing_thread_launch(self.ros_file_launch ,self.store_all_launch_files , self.store_terminate_file, self.store_server_node_checker, thread = 2)


    # Read what is in the CSV file for users
    def read_starting_position_array(self, robot_name):
        # Put all the position of all the robots in one array so that it can be used with the launch files
        
        # Open the csv file so that it can read the starting position so that it can be moved
        # Reading the csv file so that it is able to be used in the launch file in a loop
        print(self.starting_position_path)
        with open(self.starting_position_path + self.input_augument[2] + "/" + robot_name + "_starting_position.csv", "rU") as csvfileOutput:
            reader = csv.reader(csvfileOutput, delimiter=",")

            # Artifitial Count
            count = 0
            
            # for row in reader:
            for starting_position_input in reader:

                # Skip the first row since it is a description
                if count != 0:
                    self.starting_position_reader.extend(starting_position_input)
                count += 1
         
        


    # ie I might need to revisite the internal foundation for the launch
    def robot_and_obstacle_bot_standard_tuw_simulation_launch(self):
        
        # Launch file 1
        launch1 = ['robot_navigation', 'robot_and_obstacle_bot_tuw.launch', 'room:='+ self.input_augument[2]]

        roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)
        roslaunch_args1 = launch1[2:]

        launch_files = [(roslaunch_file1, roslaunch_args1)]
        self.parent_launch = roslaunch.parent.ROSLaunchParent(self.ros_file_launch, roslaunch_file1)

        self.parent_launch.start()

        # Time sleep so that it dont overlap with that with other packages 
        time.sleep(self.time_sleep)
        self.parent_launch.shutdown()


        # Make it so that you are able run two launch files ar the same time
        # Launch 2
        launch2 = ['robot_navigation', 'robot_and_obstacle_bot_simulation_tuw.launch', ('room:='+ self.input_augument[2])]

        roslaunch_file2 = roslaunch.rlutil.resolve_launch_arguments(launch2)
        roslaunch_args2 = launch2[2:]
        launch_files = [roslaunch_file2, roslaunch_args2]
        self.parent_launch = roslaunch.parent.ROSLaunchParent(self.ros_file_launch, roslaunch_file2)

        # Start the launch file
        self.parent_launch.start()
        time.sleep(self.time_for_each_iteration)
        self.shutdown_launch_file()

        



    def robot_and_obstacle_bot_modified_tuw_simulation_launch(self):

        # Launch file 1
        launch1 = ['robot_navigation', 'robot_and_obstacle_bot_tuw.launch', ('room:='+ self.input_augument[2])]

        roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)[0]
        roslaunch_args1 = launch1[2:]

        # Launch file with auguments
        launch_files = [(roslaunch_file1, roslaunch_args1)]
        self.parent_launch = roslaunch.parent.ROSLaunchParent(self.ros_file_launch, launch_files)

        self.parent_launch.start()

        # Time sleep so that it dont overlap with that with other packages 
        time.sleep(self.time_sleep)
        self.parent_launch.shutdown()

        # Launch file 2
        launch1 = ['robot_navigation', 'launch_testing_tuw.launch', ('room:='+ self.input_augument[2])]

        roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)[0]
        roslaunch_args1 = launch1[2:]

        # Launch file with auguments
        launch_files = [(roslaunch_file1, roslaunch_args1)]
        self.parent_launch = roslaunch.parent.ROSLaunchParent(self.ros_file_launch, launch_files)

        # Start the launch file
        self.parent_launch.start()
        self.shutdown_launch_file()



    # ie determine how to do the input for the 2d and 3d for navigation stack with auguments


    def robot_and_obstacle_bot_navigation_stack_2d(self):
        
        launch1 = ['robot_navigation', 'launch_testing.launch', 'world_name:='+self.input_augument[2], 'robot1_x:='+self.starting_position_reader[0], 'robot1_y:='+self.starting_position_reader[1], 'robot2_x:='+self.starting_position_reader[2], 'robot2_y:='+self.starting_position_reader[3], 'obstacle_bot_x:='+self.starting_position_reader[4], 'obstacle_bot_y:='+self.starting_position_reader[5]]
        
        launch2 = launch1 = ['robot_navigation', 'launch_testing.launch']

        roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)[0]
        roslaunch_args1 = launch1[2:]

        roslaunch_file2 = roslaunch.rlutil.resolve_launch_arguments(launch2)[0]
        roslaunch_args2 = launch1[2:]

        # launch file with auguments
        launch_files = (roslaunch_file1, roslaunch_args1)
        launch_files2 = (roslaunch_file2, roslaunch_args2)

        # stores the array so that it does not have to to launch it here
        self.store_all_launch_files.append(launch_files)
        self.store_terminate_file.append(launch_files2)

        self.shutdown_launch_file()




    def robot_and_obstacle_bot_navigation_stack_3d(self):

        launch1 = ['robot_navigation', 'launch_testing.launch', 'world_name:='+self.input_augument[2], 'robot1_x:='+self.starting_position_reader[0], 'robot1_y:='+self.starting_position_reader[1], 'robot2_x:='+self.starting_position_reader[2], 'robot2_y:='+self.starting_position_reader[3], 'obstacle_bot_x:='+self.starting_position_reader[4], 'obstacle_bot_y:='+self.starting_position_reader[5]]
        
        launch2 = launch1 = ['robot_navigation', 'launch_testing.launch']

        roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)[0]
        roslaunch_args1 = launch1[2:]

        roslaunch_file2 = roslaunch.rlutil.resolve_launch_arguments(launch2)[0]
        roslaunch_args2 = launch1[2:]

        # Launch file with auguments
        launch_files = (roslaunch_file1, roslaunch_args1)
        launch_files2 = (roslaunch_file2, roslaunch_args2)

        # Stores the array so that it does not have to to launch it here
        self.store_all_launch_files.append(launch_files)
        self.store_terminate_file.append(launch_files2)

        self.shutdown_launch_file()




    
    # Launch file save for diffent custom inputs  
    def save_launch_data(self):
        
        # Determine if you should be reseting the csv file or appending it
        if self.reset == "yes":
            edit_type = "w"
        elif self.reset == "no":
            edit_type = "a"    
       
        # open to save all the input launch files 
        with open(self.launch_csv_file, edit_type) as csvfileOutput:
            writer = csv.writer(csvfileOutput, delimiter=",")

            if edit_type == "w":
                writer.writerow(["Package","launch_file1","launch1_augument_1","launch1_augument_2","launch1_augument_3","launch1_augument_4"])

            count = 2 
            for l_input in range(self.setup_input):

                # When the input for the user will be saved it so it can be used later
                if l_input != 0:
                    writer.writerow([self.input_augument[count], self.input_augument[count + 1], self.input_augument[count + 2], self.input_augument[count + 3], self.input_augument[count + 4], self.input_augument[count + 5],])
                    if l_input == (int(self.setup_input) - 1):
                        break
                    count += 3
        




    # Create custom file and than save it for later use in a csv file
    def custom_launch_file(self):
        
        # first launch file
        launch1 = [self.input_augument[2], self.input_augument[3],self.input_augument[4], self.input_augument[5]]

        roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)[0]
        roslaunch_args1 = launch1[2:]

        # Launch file with auguments
        launch_files = [(roslaunch_file1, roslaunch_args1)]
        self.parent_launch = roslaunch.parent.ROSLaunchParent(self.ros_file_launch, launch_files)

        # Time sleep so that it don't overlap
        time.sleep(self.time_sleep)

        # Second launch files
        launch2 = [self.input_augument[2], self.input_augument[6], self.input_augument[7], self.input_augument[8]]

        roslaunch_file2 = roslaunch.rlutil.resolve_launch_arguments(launch2)[0]
        roslaunch_args2 = launch2[2:]

        # Launch file with auguments
        launch_files = (roslaunch_file2, roslaunch_args2)
        self.parent_launch = roslaunch.parent.ROSLaunchParent(self.ros_file_launch, launch_files)

        # Start the launch file
        self.parent_launch.start()
        self.shutdown_launch_file()

 


    # Run all the launch files that is in the csv file  
    def run_all_custom_launch_files(self):
                
        # Reading the csv file so that it is able to be used in the launch file in a loop
        with open(self.launch_csv_file, "rU") as csvfileOutput:
            reader = csv.reader(csvfileOutput, delimiter=",")

            # Artifitial Count
            count = 0
            
            # for row in reader:
            for i, line in enumerate(reader):

                # Skip the first row since it is a description
                if count != 0:

                    # Input from each of the input that was taken 
                    launch1 = [line[0], line[1], line[2], line[3], line[4], line[5]]

                    roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)[0]
                    roslaunch_args1 = launch1[2:]

                    # Launch file with auguments
                    launch_files = (roslaunch_file1, roslaunch_args1)

                    # self.parent_launch.append(launch_files)
                    # Determine that number it is for the launch file to terminate
                    if count == int(self.terminate_launch_files):
                        # Store where the launch files needs to terminate
                        self.store_terminate_file.append(launch_files)

                    # Stores the array so that it does not have to to launch it here
                    if count == int(self.terminate_launch_files):
                        pass
                    else:
                        self.store_all_launch_files.append(launch_files)
                    

                count += 1

            # Add node server launch file 
            self.checker_nodes_server()
            self.shutdown_launch_file()



    # Terminating file diffrent styleq
    def terminating_obj(self):
        pass

    

    # Loop thought a function that you want to dependig on the amount of loop the user wants
    def run_all_custom_launch_files_with_loops(self):
                
        # Reading the csv file so that it is able to be used in the launch file in a loop
        with open(self.launch_csv_file, "rU") as csvfileOutput:
            reader = csv.reader(csvfileOutput, delimiter=",")

            # Artifitial Count
            count = 0
            
            # for row in reader:
            for i, line in enumerate(reader):

                # Skip the first row since it is a description
                if count != 0:

                    # Input from each of the input that was taken 
                    launch1 = [line[0], line[1], line[2], line[3], line[4], line[5]]
                    
                    if count == int(self.loop_launch_file):
                        # Loop in those launch files
                        self.looping_in_launch_files(launch1)

                    
                    # Skip that number of file since you are going to loop throught that a certain amount of time
                    if count != self.loop_launch_file:

                        roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)[0]
                        roslaunch_args1 = launch1[2:]

                        # Launch file with auguments
                        launch_files = (roslaunch_file1, roslaunch_args1)

                        # Determine that number it is for the launch file to terminate
                        if count == int(self.terminate_launch_files):
                            # Store where the launch files needs to terminate
                            self.store_terminate_file.append(launch_files)

                        # Stores the array so that it does not have to to launch it here
                        self.store_all_launch_files.append(launch_files)

                count += 1
            self.shutdown_launch_file(parent)


    

    # Loop in those in those things so that it does loops for a sertain launch file
    def looping_in_launch_files(self, launch_file):
 
        # looping in the certain launch files
        for i in range(int(self.loop_launch_file_iterations)):

            roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(launch1)[0]
            roslaunch_args1 = launch1[2:]

            # Launch file with auguments
            launch_files = [(roslaunch_file1, roslaunch_args1)]
            parent = roslaunch.parent.ROSLaunchParent(self.ros_file_launch, launch_files)

            # Time sleep so that it dont overlap with that with other packages 
            time.sleep(self.time_sleep)

            # Start the launch file
            parent.start()




    # Show all current files currently in stock
    def show_current_files(self):

        # Reading the csv file so that it is able to be used in the launch file in a loop
        with open(self.launch_csv_file, "rU") as csvfileOutput:
            reader = csv.reader(csvfileOutput, delimiter=",")

            # Artifitial Count
            count = 0

            # Reading all the launch files 
            for i, line in enumerate(reader):

                # Skip the first row since it is a description
                if count != 0:

                    print('Launch File {} = {}'.format(i, line))

                count += 1



    # Screen Recorder to record screen for each test run
    def screen_recorder_api(self):

        # Start the the screen recorder
        self.screen_recorder_obj.record(self.screen_recorder, folder = self.path_for_record_save, level_path = self.input_augument[2], input_name = self.video_path_name)

        # stop recording
        self.screen_recorder_obj.stop_recording()

