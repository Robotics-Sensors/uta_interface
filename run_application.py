from python_API.header_imports import *

# The main file that will determine what to do for all the launch files 
if __name__ == "__main__":
    
    # input_1 = file name(ie: it is by default), input_2 = map to generate(ex: level1)
    augument_list = sys.argv

    # User input so that it can be compared
    user_input = ""
    
    # Verifying if it should move on or not
    verify_1 = False
    
    # Give Instructions and take user input for the type of test you are going to have
    try:

        # Verifying if it should move on or not
        verify_1 = False
        
        # Testing to see if it right or not
        while(verify_1 == False):

            print(texture.BOLD + texture.PURPLE + "\n\tie: Functionality:--> catkin_build_and_source | starting_position | goal_position | run_test_navigation_stack_2d | run_test_navigation_stack_3d | run_test_standard_tuw" + texture.END)
            print(texture.BOLD + texture.PURPLE + "\t                 :--> run_test_modefied_tuw | custom_launch_file | save_launch_files | launch_all | launch_all_loop | show_launch_files" + texture.END)

            # Throw and exception so that it is the exact input from the user that will make it work
            user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)
       
            # Raise Error to determine if it is the incorrect output
            verify_1 = raise_error_functionality(user_input)

            # If it is the correct input it would not execute
            user_input = user_input.split(" ")

            # Verify it so that it can be added to the array 
            if verify_1 == True:
                augument_list = augument_list + user_input


    except ValueError:
        print("Input was wrong")


    # ie create function for other input fromm the user
            
    # catkin build and source anywhere
    if augument_list[1] == "catkin_build_and_source":
        catkin_build_and_source_obj = catkin_build_and_source()



    # Changing starting position base on the world you want and the robot you want to change the starting position
    if augument_list[1] == "starting_position":
        
        # Verifying if it should move on or not
        verify_1, verify_2 = False, False

        # Give Instructions and take user input
        try:

            # Verifying if it should move on or not
            verify_1, verify_2 = False, False 
            
            # Testing to see if it right or not
            while(verify_1 == False or verify_2 == False):

                print(texture.BOLD + texture.PURPLE + "\n\tie: Input should look like:--> world name | robot name | x position | y position | z rotation" + texture.END)
                print(texture.GREEN + "\tie: world name --> level1 | level2 | level3 | level4 | nerve1_base_world | nerve1_full_1cm_cube | nerve1_full_5cm_cube | nerve1_full_high | nerve1_full_high_clip | nerve1_full_low" + texture.END)
                print(texture.GREEN + "\t                   nerve1_full_regular | nerve1_half_high | nerve1_half_low | nerve1_half_regular | nerve1_negative | nerve2_base_world | nerve2_full_high | nerve2_full_low | nerve2_full_regular" + texture.END) 
                print(texture.GREEN + "\t                   nerve2_half_high | nerve2_half_low | nerve2_half_regular | nerve3_base_world | nerve_long_hall | nerve_physical" + texture.END)
                print(texture.GREEN + "\tie: robot name --> robot1 | robot2 | obstacle_bot" + texture.END) 
                user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)
            
                # Seperate input by space
                user_input = user_input.split(" ")

                # Look to see if the user input the correct input
                verify_1 = raise_error_level_position(user_input)
                verify_2 = raise_error_robot(user_input)
                
                # Verify it so that it can be added to the array and continue 
                if verify_1 == True and verify_2 == True:

                    # Starting the auguments 
                    augument_list = augument_list + user_input

                    augument_list.insert(4, "1")
                    starting_position_obj = starting_position(augument_list)
            
        except ValueError:
            print("Input was wrong")



    # Changing goal position base on the world you want and the robot you want to change the goal position
    if augument_list[1] == "goal_position":

        # Give Instructions and take user input 
        try:

            # Verifying if it should move on or not
            verify_1, verify_2 = False, False 
            
            # Testing to see if it right or not
            while(verify_1 == False or verify_2 == False):

                print(texture.BOLD + texture.PURPLE + "\n\tie: Input should look like:--> world name | robot name | number of goal | x position | y position | z rotation" + texture.END)
                print(texture.GREEN + "\tie: world name --> level1 | level2 | level3 | level4 | nerve1_base_world | nerve1_full_1cm_cube | nerve1_full_5cm_cube | nerve1_full_high | nerve1_full_high_clip | nerve1_full_low" + texture.END)
                print(texture.GREEN + "\t                   nerve1_full_regular | nerve1_half_high | nerve1_half_low | nerve1_half_regular | nerve1_negative | nerve2_base_world | nerve2_full_high | nerve2_full_low | nerve2_full_regular" + texture.END) 
                print(texture.GREEN + "\t                   nerve2_half_high | nerve2_half_low | nerve2_half_regular | nerve3_base_world | nerve_long_hall | nerve_physical" + texture.END)
                print(texture.GREEN + "\tie: robot name --> robot1 | robot2 | obstacle_bot" + texture.END) 
                user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

                # Seperate input by space
                user_input = user_input.split(" ")

                # Look to see if the user input the correct input
                raise_error_level_position(user_input)
                raise_error_robot(user_input)

                # Verify it so that it can be added to the array and continue 
                if verify_1 == True and verify_2 == True:

                    # Starting the auguments 
                    augument_list = augument_list + user_input
                    
                    # Starting auguments
                    goal_position_obj = goal_position(augument_list)

        except ValueError:
            print("Input was wrong")



    # Start running the test for navigation stack
    if augument_list[1] == "run_test_navigation_stack_2d":

        # Give Instructions and take user input
        try:

            # Verifying if it should move on or not
            verify_1, verify_2 = False, False 
            
            # Testing to see if it right or not
            while(verify_1 == False or verify_2 == False):

                print(texture.GREEN + "\n\tie: world name --> level1 | level2 | level3 | level4 | nerve1_base_world | nerve1_full_1cm_cube | nerve1_full_5cm_cube | nerve1_full_high | nerve1_full_high_clip | nerve1_full_low" + texture.END)
                print(texture.GREEN + "\t                   nerve1_full_regular | nerve1_half_high | nerve1_half_low | nerve1_half_regular | nerve1_negative | nerve2_base_world | nerve2_full_high | nerve2_full_low | nerve2_full_regular" + texture.END) 
                print(texture.GREEN + "\t                   nerve2_half_high | nerve2_half_low | nerve2_half_regular | nerve3_base_world | nerve_long_hall | nerve_physical" + texture.END)
                user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

                # Seperate input by space
                user_input = user_input.split(" ")

                # Look to see if the user input the correct input
                raise_error_level(user_input)
                
                # Verify it so that it can be added to the array and continue 
                if verify_1 == True and verify_2 == True:

                    # Starting the auguments 
                    augument_list = augument_list + user_input
                    
                    # Make it so that it does not retain the element in index 1 since we don't need it 
                    util_launch_files_obj = launch_api_for_navigation_stack_and_tuw(input_augument = augument_list)

        except ValueError:
            print("Input was wrong")



    # Start running the test for navigation stack
    if augument_list[1] == "run_test_navigation_stack_3d":

        # Give Instructions and take user input
        try:

            # Verifying if it should move on or not
            verify_1, verify_2 = False, False 
            
            # Testing to see if it right or not
            while(verify_1 == False or verify_2 == False):

                print(texture.GREEN + "\n\tie: world name --> level1 | level2 | level3 | level4 | nerve1_base_world | nerve1_full_1cm_cube | nerve1_full_5cm_cube | nerve1_full_high | nerve1_full_high_clip | nerve1_full_low" + texture.END)
                print(texture.GREEN + "\t                   nerve1_full_regular | nerve1_half_high | nerve1_half_low | nerve1_half_regular | nerve1_negative | nerve2_base_world | nerve2_full_high | nerve2_full_low | nerve2_full_regular" + texture.END) 
                print(texture.GREEN + "\t                   nerve2_half_high | nerve2_half_low | nerve2_half_regular | nerve3_base_world | nerve_long_hall | nerve_physical" + texture.END)
                user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

                # Seperate input by space
                user_input = user_input.split(" ")

                # Look to see if the user input the correct input
                raise_error_level(user_input)
                
                # Verify it so that it can be added to the array and continue 
                if verify_1 == True and verify_2 == True:

                    # Starting the auguments 
                    augument_list = augument_list + user_input
                    
                    # Make it so that it does not retain the element in index 1 since we don't need it 
                    util_launch_files_obj = launch_api_for_navigation_stack_and_tuw(input_augument = augument_list)

        except ValueError:
            print("Input was wrong")



    # Start running the test for  standard tuw
    if augument_list[1] == "run_test_standard_tuw":

        # Give Instructions and take user input
        try:
           
            # Verifying if it should move on or not
            verify_1, verify_2 = False, False 
            
            # Testing to see if it right or not
            while(verify_1 == False or verify_2 == False):

                print(texture.GREEN + "\n\tie: world name --> level1 | level2 | level3 | level4 | nerve1_base_world | nerve1_full_1cm_cube | nerve1_full_5cm_cube | nerve1_full_high | nerve1_full_high_clip | nerve1_full_low" + texture.END)
                print(texture.GREEN + "\t                   nerve1_full_regular | nerve1_half_high | nerve1_half_low | nerve1_half_regular | nerve1_negative | nerve2_base_world | nerve2_full_high | nerve2_full_low | nerve2_full_regular" + texture.END) 
                print(texture.GREEN + "\t                   nerve2_half_high | nerve2_half_low | nerve2_half_regular | nerve3_base_world | nerve_long_hall | nerve_physical" + texture.END)
                user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

                # Seperate input by space
                user_input = user_input.split(" ")

                # Look to see if the user input the correct input
                raise_error_level(user_input)
                
                # Verify it so that it can be added to the array and continue 
                if verify_1 == True and verify_2 == True:

                    # Starting the auguments 
                    augument_list = augument_list + user_input
                    
                    # Make it so that it does not retain the element in index 1 since we don't need it 
                    util_launch_files_obj = launch_api_for_navigation_stack_and_tuw(input_augument = augument_list)

        except ValueError:
            print("Input was wrong")



    # Start running the test for tuw with a diffrent local planner
    if augument_list[1] == "run_test_modefied_tuw":

        # Give Instructions and take user input
        try:
           
            # Verifying if it should move on or not
            verify_1, verify_2 = False, False 
            
            # Testing to see if it right or not
            while(verify_1 == False or verify_2 == False):

                print(texture.GREEN + "\n\tie: world name --> level1 | level2 | level3 | level4 | nerve1_base_world | nerve1_full_1cm_cube | nerve1_full_5cm_cube | nerve1_full_high | nerve1_full_high_clip | nerve1_full_low" + texture.END)
                print(texture.GREEN + "\t                   nerve1_full_regular | nerve1_half_high | nerve1_half_low | nerve1_half_regular | nerve1_negative | nerve2_base_world | nerve2_full_high | nerve2_full_low | nerve2_full_regular" + texture.END) 
                print(texture.GREEN + "\t                   nerve2_half_high | nerve2_half_low | nerve2_half_regular | nerve3_base_world | nerve_long_hall | nerve_physical" + texture.END)
                user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

                # Seperate input by space
                user_input = user_input.split(" ")

                # Look to see if the user input the correct input
                raise_error_level(user_input)
                
                # Verify it so that it can be added to the array and continue 
                if verify_1 == True and verify_2 == True:

                    # Starting the auguments 
                    augument_list = augument_list + user_input
                    
                    # Make it so that it does not retain the element in index 1 since we don't need it 
                    util_launch_files_obj = launch_api_for_navigation_stack_and_tuw(input_augument = augument_list)

        except ValueError:
            print("Input was wrong")



    # Create your own custom when you are going into
    if augument_list[1] == "custom_launch_file":

        # Give Instructions and take user input 
        try:

            print(texture.PURPLE + "\n\tie: Input should look like:--> Package | launch_file1 | launch1_augument_1 | launch1_augument_2 | launch_file2 | launch2_augument_1 | launch2_augument_2" + texture.END)
            user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

            print("ie: How many iterations")
            user_input_iteration = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

            # Seperate input by space
            user_input = user_input.split(" ")
            augument_list = augument_list + user_input
                
            util_launch_files_obj = launch_api_for_navigation_stack_and_tuw(input_augument = augument_list, iterations = user_input_iteration)

        except ValueError:
            print("Input was wrong")



    # Saving the launch files
    if augument_list[1] == "save_launch_files":
        

        # How many launch files you want to 
        user_reset_files = input(texture.YELLOW + "\n\tHow many launch files do you want to add: --> " + texture.PURPLE)
        
        # Determine how many launch files you want to add
        for i in range(int(user_reset_files)):

            # Give Instructions and take user input 
            try:
                # Determine to reset cvs file or not
                user_reset = input(texture.YELLOW + "\n\tDo you want to reset files:--> yes or no : " + texture.PURPLE)
                
                print(texture.PURPLE + "\n\tie: Input should look like:--> Package | launch_file1 | launch1_augument_1 | launch1_augument_2 | launch1_augument_3 | launch1_augument_4" + texture.END)
                user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

                # If it is there to delete it would for the input that was put in
                if  i > 0:
                    del augument_list[2:]


                # Seperate input by space
                user_input = user_input.split(" ")
                augument_list = augument_list + user_input
                
                util_launch_files_obj = launch_api_for_navigation_stack_and_tuw(input_augument = augument_list, reset = user_reset)


            except ValueError:
                print("Input was wrong")



    # Launch all the files in the csv file
    if augument_list[1] == "launch_all":

        # Give Instructions and take user input 
        try:
            print(texture.PURPLE + "\n\tie: How many iterations" + texture.END)
            iteration_user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

            print(texture.PURPLE + "\n\tie: What file is your termination file (Number)" + texture.END)
            terminate_user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)
            
            print(texture.GREEN + "\n\tie: world name --> level1 | level2 | level3 | level4 | nerve1_base_world | nerve1_full_1cm_cube | nerve1_full_5cm_cube | nerve1_full_high | nerve1_full_high_clip | nerve1_full_low" + texture.END)
            print(texture.GREEN + "\t                   nerve1_full_regular | nerve1_half_high | nerve1_half_low | nerve1_half_regular | nerve1_negative | nerve2_base_world | nerve2_full_high | nerve2_full_low | nerve2_full_regular" + texture.END) 
            print(texture.GREEN + "\t                   nerve2_half_high | nerve2_half_low | nerve2_half_regular | nerve3_base_world | nerve_long_hall | nerve_physical" + texture.END)
            user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

            # Look to see if the user input the correct input
            raise_error_level(user_input)

            # Seperate input by space
            user_input = user_input.split(" ")
            augument_list = augument_list + user_input

            util_launch_files_obj = launch_api_for_navigation_stack_and_tuw(input_augument = augument_list, iterations = iteration_user_input, terminate_file_number = terminate_user_input)

        except ValueError:
            print("Input was wrong")



    # Launch all the files in the csv file with user defining what launch file you want to loop in 
    if augument_list[1] == "launch_all_loop":

        # Give Instructions and take user input 
        try:
            print(texture.PURPLE + "\n\tie: How many iterations" + texture.END)
            iteration_user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

            print(texture.PURPLE + "\n\tie: Launch File you want to keep looping for by number" + texture.END)
            user_input_loop = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

            print(texture.PURPLE + "\n\tie: How many time you want to loop within that launch file" + texture.END)
            user_input_loop_iterations = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)


            print(texture.GREEN + "\n\tie: world name --> level1 | level2 | level3 | level4 | nerve1_base_world | nerve1_full_1cm_cube | nerve1_full_5cm_cube | nerve1_full_high | nerve1_full_high_clip | nerve1_full_low" + texture.END)
            print(texture.GREEN + "\t                   nerve1_full_regular | nerve1_half_high | nerve1_half_low | nerve1_half_regular | nerve1_negative | nerve2_base_world | nerve2_full_high | nerve2_full_low | nerve2_full_regular" + texture.END) 
            print(texture.GREEN + "\t                   nerve2_half_high | nerve2_half_low | nerve2_half_regular | nerve3_base_world | nerve_long_hall | nerve_physical" + texture.END)
            user_input = input(texture.YELLOW + "\n\tUser Input--> " + texture.END)

            # Look to see if the user input the correct input
            raise_error_level(user_input)

            # Seperate input by space
            user_input = user_input.split(" ")
            augument_list = augument_list + user_input

            util_launch_files_obj = launch_api_for_navigation_stack_and_tuw(input_augument = augument_list, iterations = iteration_user_input , loop_launch_file = user_input_loop, loop_launch_file_iterations = user_input_loop_iterations)

        except ValueError:
            print("Input was wrong")
     


    # Show all the current launch files
    if augument_list[1] == "show_launch_files":
        util_launch_files_obj = launch_api_for_navigation_stack_and_tuw(input_augument = augument_list)
            

