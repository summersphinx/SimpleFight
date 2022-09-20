import pandas
import os
from random import choices
import names


class Enemy:
    def __init__(self):
        data = pandas.read_csv('basic.csv', index_col=0)
        enemy = data.loc[choices(data.index.tolist(), data['CHANCE'].tolist())]
        self.HP = enemy['HP'].values[0]
        self.MP = enemy['MP'].values[0]
        self.DMG = enemy['DMG'].values[0]
        self.AMR = enemy['AMR'].values[0]
        self.VAR = enemy['VAR'].values[0]
        self.name = names.get_first_name()


if __name__ == '__main__':
    gef = Enemy()
    print(gef.name)
