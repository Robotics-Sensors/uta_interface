# Error Function and utilities for the API and Catkin build and source 

class catkin_build_and_source(object):
    def __init__(self):
        # Absolute path so that it is able to be launched anywhere
        self.absolute_path = os.path.abspath(os.getcwd())

        # catkin build and source
        for i in range(10):
            os.system("cd ../../.. catkin build")
            os.system("cd ../../.. source devel/setup.bash")




# Flaver for testing 
class texture:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



# Verifying
def verifying(input):
    pass



# It is to determine if the user inputs an incorrect input 
def raise_error_functionality(user_input):
   
    # Tell the User if they misspelled the Functionality
    if (user_input == "catkin_build_and_source"):
        return True
    elif user_input == "starting_position":
        return True
    elif user_input == "goal_position":
        return True
    elif user_input == "run_test_navigation_stack_2d":
        return True
    elif user_input == "run_test_navigation_stack_3d":
        return True
    elif user_input == "run_test_standard_tuw":
        return True
    elif user_input == "run_test_modefied_tuw":
        return True
    elif user_input == "custom_launch_file":
        return True
    elif user_input == "save_launch_files":
        return True
    elif user_input == "launch_all":
        return True
    elif user_input == "launch_all_loop":
        return True
    elif user_input == "show_launch_files":
        return True
    else:
        print(texture.BOLD + texture.RED + texture.UNDERLINE + "\n\t                                                                     " + texture.END)
        print(texture.BOLD + texture.RED + "\t        Misspelled the Functionality, or Unavailable Functionality " + texture.END)
        print(texture.BOLD + texture.RED + texture.UNDERLINE + "\t                             Try Again                               \n" + texture.END)
        return False



# This will raise error if you type the incorrent levels
def raise_error_level(user_input):
    
    # Tell the User if they misspelled the world
    if (user_input == "level1"):
        return True
    elif user_input == "level2":
        return True
    elif user_input == "level3":
        return True
    elif user_input == "level4":
        return True
    elif user_input == "nerve1_base_world":
        return True
    elif user_input == "nerve1_full_1cm_cube":
        return True
    elif user_input == "nerve1_full_5cm_cube":
        return True
    elif user_input == "nerve1_full_high":
        return True
    elif user_input == "nerve1_full_high_clip":
        return True
    elif user_input == "nerve1_full_low":
        return True
    elif user_input == "nerve1_full_regular":
        return True
    elif user_input == "nerve1_half_high":
        return True
    elif user_input == "nerve1_half_low":
        return True
    elif user_input == "nerve1_half_regular":
        return True
    elif user_input == "nerve1_full_regular":
        return True
    elif user_input == "nerve1_negative":
        return True
    elif user_input == "nerve2_base_world":
        return True
    elif user_input == "nerve2_full_high":
        return True
    elif user_input == "nerve2_full_low":
        return True
    elif user_input == "nerve2_full_regular":
        return True
    elif user_input == "nerve2_half_high":
        return True
    elif user_input == "nerve2_half_low":
        return True
    elif user_input == "nerve2_half_regular":
        return True
    elif user_input == "nerve3_base_world":
        return True
    elif user_input == "nerve_long_hall":
        return True
    elif user_input == "nerve_physical":
        return True
    else:
        print(texture.BOLD + texture.RED + texture.UNDERLINE + "\n\t                                                               " + texture.END)
        print(texture.BOLD + texture.RED + "\t       Misspelled the World Name, or Unavailable World Name      " + texture.END)
        print(texture.BOLD + texture.RED + texture.UNDERLINE + "\t                            Try Again                        \n" + texture.END)
        return False


# This will raise error if you type the incorrent levels
def raise_error_level_position(user_input):
   
    # Tell the User if they misspelled the world
    if (user_input[0] == "level1"):
        return True
    elif user_input[0] == "level2":
        return True
    elif user_input[0] == "level3":
        return True
    elif user_input[0] == "level4":
        return True
    elif user_input[0] == "nerve1_base_world":
        return True
    elif user_input[0] == "nerve1_full_1cm_cube":
        return True
    elif user_input[0] == "nerve1_full_5cm_cube":
        return True
    elif user_input[0] == "nerve1_full_high":
        return True
    elif user_input[0] == "nerve1_full_high_clip":
        return True
    elif user_input[0] == "nerve1_full_low":
        return True
    elif user_input[0] == "nerve1_full_regular":
        return True
    elif user_input[0] == "nerve1_half_high":
        return True
    elif user_input[0] == "nerve1_half_low":
        return True
    elif user_input[0] == "nerve1_half_regular":
        return True
    elif user_input[0] == "nerve1_full_regular":
        return True
    elif user_input[0] == "nerve1_negative":
        return True
    elif user_input[0] == "nerve2_base_world":
        return True
    elif user_input[0] == "nerve2_full_high":
        return True
    elif user_input[0] == "nerve2_full_low":
        return True
    elif user_input[0] == "nerve2_full_regular":
        return True
    elif user_input[0] == "nerve2_half_high":
        return True
    elif user_input[0] == "nerve2_half_low":
        return True
    elif user_input[0] == "nerve2_half_regular":
        return True
    elif user_input[0] == "nerve3_base_world":
        return True
    elif user_input[0] == "nerve_long_hall":
        return True
    elif user_input[0] == "nerve_physical":
        return True
    else:
        print(texture.BOLD + texture.RED + texture.UNDERLINE + "\n\t                                                               " + texture.END)
        print(texture.BOLD + texture.RED + "\t       Misspelled the World Name, or Unavailable World Name      " + texture.END)
        print(texture.BOLD + texture.RED + texture.UNDERLINE + "\t                            Try Again                        \n" + texture.END)
        return False


def raise_error_robot(user_input):

    # Tell the User if they misspelled the robot name
    if (user_input[1] == "robot1"):
        return
    elif user_input[1] == "robot2":
        return
    elif user_input[1] == "obstacle_bot":
        return
    else:
        print(texture.BOLD + texture.RED + texture.UNDERLINE + "\n\t                                                               " + texture.END)
        print(texture.BOLD + texture.RED + "\t      Misspelled the robot name, or Unavailable Robot Name     " + texture.END)
        print(texture.BOLD + texture.RED + texture.UNDERLINE + "\t                            Try Again                        \n" + texture.END)
        return False



# Starting position so that it does not overlap
def skip_overlap(input_augument):

    # Skip overlap
    if input_augument[1] == "show_launch_files":
        return True
    elif input_augument[1] == "launch_all_loop":
        return True
    elif input_augument[1] == "launch_all":
        return True
    elif input_augument[1] == "save_launch_files":
        return True
    else:
        return False


