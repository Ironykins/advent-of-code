import itertools

boss = {}
player = {'hp': 50, 'mp': 500, 'manaspent': 0, 'arm': 0}
spells = { 'missile': 53,'drain': 73, 'shield': 113,'poison': 173, 'recharge': 229 }

# Fight the boss. Returns mana spent. -1 if the player dies.
# Effects are tuples with (name, timer)
def fightBoss(player, boss, effects, playersTurn):
    newPlayer = player.copy()
    newEffects = effects.copy()
    newBoss = boss.copy()

    newPlayer['arm'] = 0 # Reset armor.

    # Apply Effects
    for effect in newEffects:
        if newEffects[effect] < 1:
            continue
        elif effect == 'poison':
            newBoss['hp'] -= 3
        elif effect == 'shield':
            newPlayer['arm'] = 7
        elif effect == 'recharge':
            newPlayer['mp'] += 101

        newEffects[effect] -= 1

    # Check End Conditions
    if newBoss['hp'] < 1 and newPlayer['hp'] > 0:
        return newPlayer['manaspent']
    elif newPlayer['hp'] < 1 or newPlayer['mp'] < 53:
        return 9999

    if playersTurn:
        # Take that 1 point of damage
        newPlayer['hp'] -= 1
        if newPlayer['hp'] < 1:
            return 9999

        # Branch for each spell we can cast
        results = []
        for spell in spells:
            if spells[spell] > newPlayer['mp']:
                continue
            if spell in newEffects and newEffects[spell] > 0:
                continue

            newNewBoss = newBoss.copy()
            newNewPlayer = newPlayer.copy()
            newNewEffects = newEffects.copy()
            newNewPlayer['mp'] -= spells[spell]
            newNewPlayer['manaspent'] += spells[spell]

            if spell == 'missile':
                newNewBoss['hp'] -= 4
            elif spell == 'drain':
                newNewBoss['hp'] -= 2
                newNewPlayer['hp'] += 2
            elif spell == 'shield':
                newNewEffects[spell] = 6
            elif spell == 'poison':
                newNewEffects[spell] = 6
            elif spell == 'recharge':
                newNewEffects[spell] = 5

            results.append(fightBoss(newNewPlayer,newNewBoss,newNewEffects,False))

        return min(results)

    else: # Boss's turn
        damage = newBoss['dmg'] - newPlayer['arm']
        damage = 1 if damage < 1 else damage
        newPlayer['hp'] -= damage
        return fightBoss(newPlayer, newBoss, newEffects, True)

with open('day22.txt') as inFile:
    for line in inFile:
        m = line.split(' ')
        if m[0] == 'Hit':
            boss['hp'] = int(m[-1])
        elif m[0] == 'Damage:':
            boss['dmg'] = int(m[-1])

print fightBoss(player, boss, { }, True)
