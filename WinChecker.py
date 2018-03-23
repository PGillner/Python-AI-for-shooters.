import pickle
from WinCondition import WinChecker

def Checker(folder, ScreenCount, screen):
    img = pickle.load(r"F:\IronSight_AI\Images\{}\Screen{}.jpg".format(folder, ScreenCount))
    if WinChecker(folder, ScreenCount) == "Victory":
        GameResult = "Victory"
        for i in range(90):
            os.remove(r"F:\IronSight_AI\Images\{}\Screen{}.jpg".format(folder, (ScreenCount - i)))
        return GameResult
    elif WinChecker(folder, ScreenCount) == "Defeat":
        os.remove(r"F:\IronSight_AI\Images\{}".format(folder))
        GameResult = "Defeat"
        return GameResult
        
