import PySimpleGUI as sg
from time import time

sg.theme("black")
button_size = 4
layout = [
    [sg.Push(), sg.Text(tooltip="Right click to change theme", key="INPUT",
     background_color="black", justification="center", font="Arial, 40", pad=(0, 10)), sg.Push()],
    [sg.Button(1, expand_x=True, size=button_size, pad=(0, 10)),
     sg.Button(2, expand_x=True, size=button_size, pad=(0, 10)),
     sg.Button(3, expand_x=True, size=button_size, pad=(0, 10)),
     sg.Button(4, expand_x=True, size=button_size, pad=(0, 10)),
     sg.Button(5, expand_x=True, size=button_size, pad=(0, 10))],
    [sg.Button(6, expand_x=True, size=button_size, pad=(0, 10)),
     sg.Button(7, expand_x=True, size=button_size, pad=(0, 10)),
     sg.Button(8, expand_x=True, size=button_size, pad=(0, 10)),
     sg.Button(9, expand_x=True, size=button_size, pad=(0, 10)),
     sg.Button(0, expand_x=True, size=button_size, pad=(0, 10))],
    [sg.Button("Start", key="START-STOP", expand_x=True),
     sg.Button("Reset", key="RESET", expand_x=True),
     sg.Button("Exit", key="EXIT", expand_x=True)]
]

window = sg.Window("New timer", layout=layout, size=(500, 300), no_titlebar=True, font="Arial, 30")
nums = []
start_time = 0
lapse_time = 0
timer_start = 0
timer_active = False
time_entered = False
while True:
    event, values = window.read(timeout=10)
    # Enter number as time
    if event in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        nums.append(event)
        # Avoid leading 0
        if nums[0] == "0":
            nums.pop()
        timer_start = ''.join(nums)
        window["INPUT"].update(timer_start)
    # Start button function
    if event == "START-STOP":
        if window["INPUT"].get():
            time_entered = True
        if timer_active:
            window["START-STOP"].update("Start")
            timer_active = False
            time_entered = False
        else:
            start_time = time()
            timer_active = True
            if window["INPUT"].get():
                time_entered = True
                timer_start = window["INPUT"].get()
    # With time entered to start. Work as a timer
    if time_entered:
        if float(window["INPUT"].get()) > 0:
            window["START-STOP"].update("Stop")
            lapse_time = round(float(timer_start) - time() + start_time, 1)
            window["INPUT"].update(lapse_time)
        else:
            time_entered = False
            window["INPUT"].update("")
            timer_active = False
            window["START-STOP"].update("Start")
            # sg.popup("Times up!", font="Arial, 20")
    # Without time entered. Work as a stopwatch
    elif timer_active:
        window["START-STOP"].update("Stop")
        lapse_time = round(time() - start_time, 1)
        window["INPUT"].update(lapse_time)
    # Reset the timer
    if event == "RESET":
        window["INPUT"].update("")
        nums = []
        timer_active = False
        start_time = 0
        lapse_time = 0
    # Close window
    if event == "EXIT":
        window.close()
        break
