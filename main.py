import os
import PySimpleGUI as sg
import time
import webbrowser

sg.theme('DarkGrey15')

layout = [[sg.Multiline('', key='log', s=(100, 49), autoscroll=True, auto_refresh=True, disabled=True, no_scrollbar=True)], [sg.Input('', key='input', s=(100, 1))]]

wn = sg.Window('SimpleFight', layout, finalize=True, font="Arial 12")

sg.cprint_set_output_destination(wn, 'log')

# sg.cprint('Test of red', t='red')

for i in [['SimpleFight', '#1E90FF', '20'], ['By: Summersphinx', '#800000', '14'], ['', 'white', '15'], ["Type 'help' for information to start!", 'white', '12']]:
    time.sleep(1.5)
    sg.cprint(i[0], t=i[1], font="Arial {} bold".format(i[2]))


event, values = wn.read()
wn.close()
