from python_API.header_imports import *


# Changing Starting Position 
class starting_position(object):
    def __init__(self, input_augument):
        self.input_augument = input_augument

        # Determine the world to be changed  
        self.change_world_spawn = self.input_augument[2]
        self.determine_path_for_robot = self.input_augument[3]

        # Determine starting position
        self.spawn_determine = self.input_augument[4]
        self.spawn_file_path = "starting_position/"
        self.world_spawn_map_path = self.spawn_file_path + self.change_world_spawn
        self.number_to_letters = dict(zip(range(1, 27), string.ascii_lowercase))

        # Current path minus the current directory
        self.absolute_path = os.path.abspath(os.getcwd())

        # Call function 
        self.changing_spawn_position()

        # Also add it every time you are done to the end of the goal; there is no need to toggle
        goal_position_obj = goal_position(self.input_augument, adding="true")
        


    # changing the spawn position base on the world and robot
    def changing_spawn_position(self):

        # Opening csv file and write in csv file
        with open(self.absolute_path + "/" + self.world_spawn_map_path + "/" + self.determine_path_for_robot + "_starting_position.csv", "w") as csvfileOutput:
            writer = csv.writer(csvfileOutput, delimiter=",")
            writer.writerow(["Spawn Description","X Position","Y Position","Theta"])
            
            # Count is for the input that will be added
            count = 4

            for spawn in range(int(self.spawn_determine) + 1):
                # Where to start seperating the starting position from the input array
                if spawn != 0:
                    writer.writerow(["starting_position", self.input_augument[count + 1], self.input_augument[count + 2], self.input_augument[count + 3]])
                    if spawn == (len(self.spawn_determine) - 1):
                        break
                    count += 3
 


# Changing goal Position and also add the spawn position at the end of the csv file as a goal for easy looping 
class goal_position(object):
    def __init__(self, input_augument, adding = "false"):
        self.input_augument = input_augument

        # Determine the the world to be changed  
        self.change_world_goal = self.input_augument[2]
        self.determine_path_for_robot = self.input_augument[3]

        # Determine where it is to be
        self.adding = adding

        self.goal_file_path = "goals/"
        self.world_goal_map_path = self.goal_file_path + self.change_world_goal
        self.number_to_letters = dict(zip(range(1, 27), string.ascii_lowercase))
        
        # Current path minus the current directory
        self.absolute_path = os.path.abspath(os.getcwd())
        
        # Determine how many goals
        if self.adding == "true":

            # Determine the size of the csv file
            self.goal_determine  = len(pd.read_csv(self.absolute_path + "/" + self.world_goal_map_path + "/" + self.determine_path_for_robot + "_goals.csv"))
        else:
            self.goal_determine = self.input_augument[4]

        # Call function 
        self.changing_goal_position()


        
    # changing the goal position base on the world and robot
    def changing_goal_position(self):
        
        # Detetmine if you should write or append
        if self.adding == "false":
            edit_input = "w"
        elif self.adding == "true":
            edit_input = "a"

        # Opening csv file and write in csv file
        with open(self.absolute_path + "/" + self.world_goal_map_path + "/" + self.determine_path_for_robot + "_goals.csv", edit_input) as csvfileOutput:
            writer = csv.writer(csvfileOutput, delimiter=",")

            # Determine if it is needed or not
            if self.adding == "false":
                writer.writerow(["Goal Description","X Position","Y Position","Theta"])
            else:
                pass
            
            # Count is for the loop that will be added
            count, count_sp = 4, 4
            
            # Determine if you have need it for the starting porition or the goal
            if self.adding == "false":
                input = 2
            elif self.adding == "true":
                input = 3

            # For the self Determine of the csv input
            for goal in range(int(self.goal_determine) + input):

                # Where to start seperating the goal from the input array
                if goal != 0:

                    # For the input starting position
                    if self.adding == "true":

                        # The goal is the letter to be determine when converting to number to letter
                        if goal == (self.goal_determine):
                            writer.writerow(["spawn_position", self.input_augument[count_sp + 1], self.input_augument[count_sp + 2], self.input_augument[count_sp + 3]])
                    elif self.adding == "false":
                            writer.writerow(["goal_" + self.number_to_letters[goal], self.input_augument[count + 1], self.input_augument[count + 2], self.input_augument[count + 3]])

                    if goal == int(self.goal_determine):
                        break
                    count += 3

