import win32ui, win32process, win32gui, pyautogui, time, sys
##########################
# Defining game constant #
GAME_ACTIVE = False # Check whether game session is active
MATCH_ACTIVE = False # Check whether player is in match
MATCH_ENDED = False # Check if the match has ended

pyautogui.FAILSAFE = True

wave = 0 # Indicates the starting wave
timer = 16 # Indicates the intermission between waves
##########################
def matchend():
    matchend = pyautogui.locateOnScreen('bin/end.png')
    if matchend is not None:
        MATCH_ENDED = True
        print('\nMatch has ended!')
        sys.exit(0)

def train_merc():
    global wave

    if wave == 0:
        pyautogui.click(649, 838, clicks=1, button='left')
        pyautogui.click(658, 651, clicks=1, button='left')
        pyautogui.click(649, 838, clicks=1, button='left')
        pyautogui.click(1182, 659, clicks=1, button='left')
        print('Training heavy blade slave')
    elif wave == 1:
        pyautogui.click(724, 838, clicks=1, button='left')
        pyautogui.click(575, 653, clicks=1, button='left')
        pyautogui.click(724, 838, clicks=1, button='left')
        pyautogui.click(1182, 659, clicks=1, button='left')
        print('Training silver guardian')
    elif wave == 2:
        pyautogui.click(800, 838, clicks=1, button='left')
        pyautogui.click(639, 651, clicks=1, button='left')
        pyautogui.click(800, 838, clicks=1, button='left')
        pyautogui.click(1182, 659, clicks=1, button='left')
        print('Training scholar')
    elif wave == 5:
        pyautogui.click(517, 853, clicks=1, button='left')
        print('Upgrading essence mine')
    elif wave == 10:
        pyautogui.click(874, 838, clicks=1, button='left')
        pyautogui.click(956, 650, clicks=1, button='left')
        pyautogui.click(874, 838, clicks=1, button='left')
        pyautogui.click(1182, 659, clicks=1, button='left')
        print('Training Vajra')
    elif wave == 11:
        pyautogui.click(952, 838, clicks=1, button='left')
        pyautogui.click(787, 651, clicks=1, button='left')
        pyautogui.click(952, 838, clicks=1, button='left')
        pyautogui.click(1182, 659, clicks=1, button='left')
        print('Training wrath chanter')
    elif wave > 11:
        pyautogui.click(874, 838, clicks=1, button='left')
        pyautogui.click(1182, 659, clicks=1, button='left')
        print('Training Vajra')
    else:
        print('Idle, gaining essence.')

def ingame():
    global timer, wave, MATCH_ENDED
    MATCH_ACTIVE = True
    # While match is active & in game
    while (MATCH_ACTIVE):
        if (MATCH_ENDED != True):
            if timer > 0:
                timer -= 1
            elif timer <= 0:
                wave += 1
                timer = 9
            print('Bot Level: '+str(wave) +'\nLeveling in: '+str(timer))
            train_merc()
            matchend()

def pregame():
    GAME_ACTIVE = True
    print('Waiting for match to start..')
    # Waiting for match to start
    while (GAME_ACTIVE):
        matchstart = pyautogui.locateOnScreen('bin/start.png')
        # Once match has started
        if matchstart is not None:
            print('Match found!')
            GAME_ACTIVE = False
            ingame()

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def main():
    # Find game window
    window_handle = win32ui.FindWindow(None, u"Red Tides").GetSafeHwnd()
    # Get process id
    pid = win32process.GetWindowThreadProcessId(window_handle)[1]

    if window_handle:
        # Pulling game screen's onto the foreground
        results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            print(i)
            if "red tides" in i[1].lower():
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                break
        print("-"*30)
        print('[Red Tides]\nProcess ID: '+str(pid))
        time.sleep(0.5)
        # Once game has been found, run func_pregame()
        pregame()

    else:
        print("-"*30)
        print('Unable to find specific window. Make sure it is running.')

if __name__ == "__main__":
   main()
