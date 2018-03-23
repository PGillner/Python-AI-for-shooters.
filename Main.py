from WinChecker import Checker
## from EnemyDetection import Search
import Outputs
import numpy as np
from Grab_Screen import grab_screen
import os
import cv2
from getkeys import key_check
import time
import Outputs

starting_value = 1
folder = 1
ScreenCount = 1

while True:
    file_name = "F:\IronSight_AI\Training_Data\AI_made_training_data{}.npy".format(starting_value)

    if os.path.isfile(file_name):
        print("File exists, moving along", starting_value)
        starting_value += 1       
    else:
        print("File doesn't exist, starting fresh!", starting_value)

        break

while True:
    folder_path = "F:\IronSight_AI\Data\{}".format(folder)
    if os.path.isfile(folder_path):
        print("Folder path exists, moving along", folder)
        folder += 1
    else:
        print("Folder path doesn't exist, starting fresh!", starting_value)

        break

def Main(file_name, starting_value, folder, ScreenCount):
    training_data = []

    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)
    
    while True:
        screen = grab_screen(region = (0, 0, 1920, 1080))
##      last_time = time.time()
        screen = cv2.resize(screen, (int(1920 / 2), int(1080 / 2)))

        np.save(screen, "F:\IronSight_AI\Data\{}\Screen{}.jpg".format(folder, ScreenCount))

        Result = Checker(folder, ScreenCount, screen)
        
##      cv2.imshow("Screen", cv2.resize(screen, (1920, 1080)))
##      print("{} FPS.".format(1 / (time.time() - last_time)))

        output = keys_being_output()
        training_data.append([screen, output])

        ScreenCount += 1

        if len(training_data) % 100 == 0:
            print(len(training_data))

        if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

        if Result == "Victory":
            np.save(file_name, training_data)
            print("Data saved because of victory.")
            training_data = []
            starting_value += 1
            ScreenCount = 1
            folder += 1
            file_name = "F:\IronSight_AI\Training_Data\AI_made_training_data{}.npy".format(starting_value)
        elif Result == "Defeat":
            ScreenCount = 1
            training_data = []
    
