import os
import PySimpleGUI as sg
import time

sg.theme('DarkGrey15')

layout = [[sg.Multiline('', key='log', s=(100, 49), autoscroll=True, auto_refresh=True, disabled=True, no_scrollbar=True)], [sg.Input('', key='input', s=(100, 1))]]

wn = sg.Window('SimpleFight', layout, finalize=True)

sg.cprint_set_output_destination(wn, 'log')

sg.cprint('Test of red', t='red')
time.sleep(3)
sg.cprint('Test of white', t='white')

for i in range(60):
    sg.cprint(i, t='white')

event, values = wn.read()
wn.close()
