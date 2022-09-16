import os
import pickle
import urllib3
import sys
import pandas

from cryptography.fernet import Fernet

http = urllib3.PoolManager()
key = Fernet(http.request('GET', 'https://gemgames.w3spaces.com/SimpleFight-key.txt').data)

if sys.platform == 'win32':
    path = os.getenv('LOCALAPPDATA') + '/GEM Games/SimpleFight/'
else:
    path = ''


class Hero:
    def __init__(self, load_name, custom_character=False, autosaves=True):
        self.mp = None
        self.hp = None
        self.gold = None
        self.carry = None
        self.armour = None
        self.hands = None
        self.magic = None
        self.inventory = None
        self.name = load_name

        if not os.path.isdir(path):
            os.makedirs(path)

        if load_name not in os.listdir(path):
            os.mkdir(path + load_name)

            with open(path + load_name + '/Hero.pkl', 'wb') as fh:
                pickle.dump(key.encrypt(http.request('GET', 'https://gemgames.w3spaces.com/SimpleFight-key.txt').data),
                            fh)

            if not custom_character:
                pass

    def load(self):
        load_name = self.name
        if load_name in os.listdir(path):
            with open(path + load_name + '/Hero.pkl', 'rb') as fh:
                data = key.decrypt(pickle.load(fh))
                with open('temp.csv', 'wb') as temp:
                    temp.write(data)

            data = pandas.read_csv('temp.csv', index_col=0, header=0)
            os.remove('temp.csv')

            self.hp = data['value']['HP']
            self.mp = data['value']['HP']
            self.gold = data['value']['HP']
            self.carry = data['value']['HP']
            self.armour = data['value']['HP']


def settings(setting=None):
    if setting is None:
        return


if __name__ == '__main__':
    stuff = Hero('Gavin')
    stuff.load()
    print(stuff.gold)
