import os
import PySimpleGUI as sg
import time
import webbrowser
import sys
import logging

import Hero

# URLS

url_docs = 'https://simplefight.readthedocs.io/en/latest/'  # Link to Docs
url_patreon = 'https://www.patreon.com/gemgames2'  # Link to Patreon
url_itch = 'https://summersphinx.itch.io/simplefight'  # Link to Itch.io page
url_home = 'https://gamegames.nicepage.io'  # Link to Website

# Get Local File Path

if sys.platform == 'win32':
    path = os.getenv('LOCALAPPDATA') + '/GEM Games/SimpleFight/'
else:
    path = ''

# Set Up Logging

logging.basicConfig(filename=f'{path}log.txt', format='[%(asctime)s]  %(message)s', level=logging.DEBUG)

# Game Code

sg.theme('DarkGrey15')

layout = [
    [sg.Multiline('', key='log', s=(100, 49), autoscroll=True, auto_refresh=True, disabled=True, no_scrollbar=True)],
    [sg.Input('', key='input', s=(100, 1), disabled=True, enable_events=True)]
]

wn = sg.Window('SimpleFight', layout, finalize=True, font="Arial 12")
wn['input'].bind("<Return>", "_Enter")

sg.cprint_set_output_destination(wn, 'log')

# sg.cprint('Test of red', t='red')

for i in [['SimpleFight', '#1E90FF', '20'], ['By: Summersphinx', '#800000', '14'], ['', 'white', '15'],
          ["Type 'help' for information to start!", 'white', '12']]:
    time.sleep(1.5)
    sg.cprint(i[0], t=i[1], font="Arial {} bold".format(i[2]))

mode = 'main'


if __name__ == '__main__':
    while True:
        logging.info('WAITING FOR NEXT ENTER')
        wn['input'].Update(disabled=False)
        wn['input'].update(value='')
        wn['input'].set_focus(True)
        while True:
            event, values = wn.read()

            if event == "input" + "_Enter" or sg.WIN_CLOSED:
                break

        user = wn['input'].get().lower().split(' ')

        logging.info(f'{user} was entered')

        if user[0] in ['quit', 'q'] or sg.WIN_CLOSED:
            wn.close()
            break

        elif user[0] == 'help':
            webbrowser.open(url_docs)

        elif user[0] == 'patreon':
            webbrowser.open(url_patreon)

        if mode == 'main':

            if user[0] == 'start':
                hero = Hero.Hero(path)
                sg.cprint(hero.hp, t='red')

            if user[0] == 'config':
                pass
            if user[0] == 'data':
                pass
        else:
            sg.cprint('Invalid command. Type help for more commands.')

logging.info('Program Closed')
