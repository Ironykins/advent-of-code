#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 konrad <konrad@serenity>
#
# RPG
import itertools

boss = {}
player = {}

# Items are tuples. (name, cost, dmg, armor)
rings = [
    ("Nothing 1"    , 0  , 0 , 0 ),
    ("Nothing 2"    , 0  , 0 , 0 ),
    ("Damage 1"  , 25  , 1 , 0  ),
    ("Damage 2"  , 50  , 2 , 0  ),
    ("Damage 3"  , 100 , 3 , 0 ),
    ("Defense 1" , 20  , 0 , 1 ),
    ("Defense 2" , 40  , 0 , 2 ),
    ("Defense 3" , 80  , 0 , 3 )
]

armors = [
    ("Nothing"    , 0  , 0 , 0 ),
    ("Leather"    , 13  , 0 , 1 ),
    ("Chainmail"  , 31  , 0 , 2 ),
    ("Splintmail" , 53  , 0 , 3 ),
    ("Bandedmail" , 75  , 0 , 4 ),
    ("Platemail"  , 102 , 0 , 5 )
]

weapons = [
    ("Dagger"     , 8  , 4 , 0),
    ("Shortsword" , 10 , 5 , 0),
    ("Warhammer"  , 25 , 6 , 0),
    ("Longsword"  , 40 , 7 , 0),
    ("Greataxe"   , 74 , 8 , 0)
]

# Returns true if player wins.
def fightBoss(player,boss):
    playerTurn = True
    while boss['hp'] > 0 and player['hp'] > 0:
        if playerTurn:
            damage = player['dmg'] - boss['arm']
            damage = 1 if damage < 1 else damage
            boss['hp'] -= damage
        else:
            damage = boss['dmg'] - player['arm']
            damage = 1 if damage < 1 else damage
            player['hp'] -= damage

        playerTurn = not playerTurn

    return player['hp'] > 0

# Gets player stats from an equipment loadout.
def equip(loadout):
    player = {'hp':100, 'dmg': 0, 'arm': 0, 'cost': 0}
    for item in loadout:
        player['cost'] += item[1]
        player['dmg'] += item[2]
        player['arm'] += item[3]
    return player

with open('day21.txt') as inFile:
    for line in inFile:
        m = line.split(' ')
        if m[0] == 'Hit':
            boss['hp'] = int(m[-1])
        elif m[0] == 'Damage:':
            boss['dmg'] = int(m[-1])
        elif m[0] == 'Armor:':
            boss['arm'] = int(m[-1])

# Iterate through all loadouts
maxCost = 0
for weapon in weapons:
    for armor in armors:
        for (ring1, ring2) in itertools.product(rings, repeat=2):
            if ring1 == ring2: # Can't have duplicate rings.
                continue
            loadout = [weapon, armor, ring1, ring2]
            player = equip(loadout)
            if player['cost'] > maxCost and not fightBoss(player,boss.copy()):
                print player
                maxCost = player['cost']

print maxCost
