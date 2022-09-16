import pandas
from random import randint as r
import sys
import pickle
import os
import urllib3
from cryptography.fernet import Fernet

http = urllib3.PoolManager()
key = Fernet(http.request('GET', 'https://gemgames.w3spaces.com/SimpleFight-key.txt').data)


class Hero:
    def __init__(self, path):
        with open(path + '/Hero.pkl', 'rb') as fh:
            data = key.decrypt(pickle.load(fh))
            with open('temp.csv', 'wb') as temp:
                temp.write(data)

        data = pandas.read_csv('temp.csv', index_col=0, header=0)
        os.remove('temp.csv')

        self.hp = [data['value']['HP'], data['value']['maxHP']]
