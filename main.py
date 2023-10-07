# IMPORT MODULES

import threading
import time
import psutil
import pygetwindow
import screeninfo

# VARIABLES

robloxProcess = "Windows10Universal.exe"
cmdProcess = "cmd.exe"
fluxusSpam = "Fluxus"
timeSortWindows = 30
timeSpamErrors = 5
timeCloseAll = 10800  # 3 HOUR


# MAIN PROGRAM

title = """

   ______    _______  _______  ___   __    _  __   __  _______    _______  _______  _______  ___       
  |    _ |  |       ||  _    ||   | |  |  | ||  | |  ||       |  |       ||       ||       ||   |      
  |   | ||  |   _   || |_|   ||   | |   |_| ||  |_|  ||   _   |  |_     _||   _   ||   _   ||   |      
  |   |_||_ |  | |  ||       ||   | |       ||       ||  | |  |    |   |  |  | |  ||  | |  ||   |      
  |    __  ||  |_|  ||  _   | |   | |  _    ||       ||  |_|  |    |   |  |  |_|  ||  |_|  ||   |___   
  |   |  | ||       || |_|   ||   | | | |   ||   _   ||       |    |   |  |       ||       ||       |  
  |___|  |_||_______||_______||___| |_|  |__||__| |__||_______|    |___|  |_______||_______||_______|  

"""

print(title)
print()
print("NOW SORTING WINDOWS, CLOSING SPAM ERRORS AND CLOSING ALL INSTANCES EVERY 3 HOURS IS WORKING")
print()

def sortWindows():
    while True:
        try:
            time.sleep(timeSortWindows)
            windows = pygetwindow.getWindowsWithTitle("Roblox")
            windows = [window for window in windows if window.title != "Roblox Account Manager"]

            monitor_info = screeninfo.get_monitors()[0]
            monitor_width, monitor_height = monitor_info.width, monitor_info.height

            max_windows_per_row, x_offset, y_offset, width, height = (10, 100, 100, 100, 100,)

            current_x, current_y, windows_in_current_row = 0, 0, 0

            for i, window in enumerate(windows):
                if windows_in_current_row >= max_windows_per_row:
                    current_x, current_y, windows_in_current_row = (0, current_y + y_offset, 0,)

                if current_x + width > monitor_width:
                    current_x, current_y, windows_in_current_row = (0, current_y + y_offset, 0,)

                if current_y + height > monitor_height:
                    break

                window.resizeTo(width, height)
                window_x = min(current_x, monitor_width - width)
                window_y = min(current_y, monitor_height - height)
                window.moveTo(window_x, window_y)

                current_x += x_offset
                windows_in_current_row += 1
        except:
            continue


def closeCmdSpam(cmdProcess):
    while True:
        try:
            time.sleep(timeSpamErrors)
            for process in psutil.process_iter(["name"]):
                if process.info["name"] == cmdProcess:
                    process.kill()
        except:
            continue
                
def closeFluxusSpam(fluxusSpam):
    while True:
        try:
            time.sleep(timeSpamErrors)
            window = pygetwindow.getWindowsWithTitle(fluxusSpam)
            if window:
                window[0].close()
        except:
            continue

def closeAllInstances(robloxProcess):
    while True:
        try:
            time.sleep(timeCloseAll)
            for process in psutil.process_iter(["name"]):
                if process.info["name"]() == robloxProcess:
                    process.kill()
        except:
            continue

if __name__ == '__main__':
    threadSortWindows = threading.Thread(target=sortWindows)
    threadCloseCmdSpam = threading.Thread(target=closeCmdSpam, args=(cmdProcess,))
    threadCloseFluxusSpam = threading.Thread(target=closeFluxusSpam, args=(cmdProcess,))
    threadCloseAllInstances = threading.Thread(target=closeAllInstances, args=(robloxProcess,))

    threadSortWindows.start()
    threadCloseCmdSpam.start()
    threadCloseFluxusSpam.start()
    threadCloseAllInstances.start()