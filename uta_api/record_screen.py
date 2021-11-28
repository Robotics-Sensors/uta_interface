from python_API.header_imports import *

class record_screen(object):
    def __init__(self):

        # Display screen resolution, get it from your OS settings
        self.SCREEN_SIZE = (1920, 1080)

        # Define the codec
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")

        self.file_path = None

        # Count for how long the video should go
        self.count = 0

        # Path for the video output
        self.save_path = os.path.abspath(os.getcwd())  + "/recording_videos/"



    # Records the video for each launch files
    def record(self, input_condition, folder, level_path, input_name):
        
        # Determine if there is already a directory for that so that it can create the directory for the levels
        if os.path.isdir(self.save_path + folder + level_path + "/") == False:
            os.mkdir(self.save_path + folder + level_path + "/")
        
        # Create the video write object
        self.out = cv2.VideoWriter(self.save_path + input_name + ".avi", self.fourcc, 20.0, (self.SCREEN_SIZE))
            
        self.count_update = None

        while input_condition == True:

            # make a screenshot
            img = pyautogui.screenshot()

            frame = np.array(img)

            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # write the frame for video
            self.out.write(frame)
            

    # End recording
    def stop_recording(self):
        
        # Make sure everything is closed when exited
        cv2.destroyAllWindows()
        self.out.release()


