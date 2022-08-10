import os
import PySimpleGUI as sg
import time
import webbrowser
import keyboard as k

import Hero

url1 = 'https://simplefight.readthedocs.io/en/latest/'  # Link to Docs
url2 = 'https://www.patreon.com/gemgames2'  # Link to Patreon
url3 = 'https://summersphinx.itch.io/simplefight'  # Link to Itch.io page
url4 = 'https://gamegames.nicepage.io'  # Link to Website

# Game Code

sg.theme('DarkGrey15')

layout = [
    [sg.Multiline('', key='log', s=(100, 49), autoscroll=True, auto_refresh=True, disabled=True, no_scrollbar=True)],
    [sg.Input('', key='input', s=(100, 1), disabled=True, enable_events=True)]
]

wn = sg.Window('SimpleFight', layout, finalize=True, font="Arial 12")

sg.cprint_set_output_destination(wn, 'log')

# sg.cprint('Test of red', t='red')

for i in [['SimpleFight', '#1E90FF', '20'], ['By: Summersphinx', '#800000', '14'], ['', 'white', '15'],
          ["Type 'help' for information to start!", 'white', '12']]:
    time.sleep(1.5)
    sg.cprint(i[0], t=i[1], font="Arial {} bold".format(i[2]))

mode = 'main'


def input():
    new = ''
    wn['input'].Update(disabled=False)
    wn['input'].update(value='')
    wn['input'].set_focus(True)

    while True:
        # Wait for the next event.
        event = k.read_event()
        if event.event_type == k.KEY_DOWN and event.name == 'enter':
            wn['input'].Update(disabled=True)
            break
        else:
            wn.refresh()


if __name__ == '__main__':
    while True:
        print('next')
        input()

        user = wn['input'].get()

        if user.lower() in ['quit', 'q'] or sg.WIN_CLOSED:
            wn.close()
            break

        elif user == 'help':
            webbrowser.open(url1)

        elif user == 'patreon':
            webbrowser.open(url2)

        elif user == 'start':
            sg.cprint('You:     HP [{hp}]   MP [{mp}]\nEnemy:   HP [{ehp}]    MP [{emp}]'.format(hp=Hero.Stats.hp[0],
                                                                                                 mp=Hero.Stats.mp[0]))
