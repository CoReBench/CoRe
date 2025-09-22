def leastHacks(shieldStrength, robotsProgram):
    shoot  = 'S'
    charge = 'C'
    totalDamage      = 0
    currentDamage    = 1
    hacksRequired    = 0
    chargeIndexes    = []
    chargeInfo       = {}
    shotsAfterCharge = 0
    firstCharge      = True
    previousCharge   = 0
    for index, action in enumerate(robotsProgram):
        if action == charge:
            if firstCharge:
                chargeInfo[index] = {'shotsAfter': shotsAfterCharge, 'damage': currentDamage, 'previousCharge': None}
                firstCharge = False
            else:
                chargeInfo[previousCharge]['shotsAfter'] = shotsAfterCharge
                chargeInfo[index] = {'shotsAfter': 0, 'damage': currentDamage, 'previousShot': previousCharge}
                shotsAfterCharge = 0
            previousCharge = index
            chargeIndexes.append(index)
            currentDamage *= 2
        else:
            if not firstCharge:
                shotsAfterCharge += 1
            totalDamage += currentDamage
    if not firstCharge:
        chargeInfo[previousCharge]['shotsAfter'] = shotsAfterCharge
    stackLength = len(chargeIndexes)
    if totalDamage <= shieldStrength:
        return hacksRequired
    elif stackLength == 0:
        return "IMPOSSIBLE"
    for index, action in enumerate(robotsProgram[::-1]):
        if action == shoot:
            if stackLength == 0:
                return "IMPOSSIBLE"
            closestCharge = chargeInfo[chargeIndexes.pop()]
            stackLength -= 1
            totalDamage -= closestCharge['shotsAfter'] * closestCharge['damage']
            hacksRequired += closestCharge['shotsAfter']
            if totalDamage <= shieldStrength:
                return hacksRequired
            if not closestCharge['previousShot']:
                chargeInfo[closestCharge['previousShot']]['shotsAfter'] += closestCharge['shotsAfter']
    return "IMPOSSIBLE"
def main():
    T     = int(raw_input().strip())
    cases = []
    for _ in range(T):
        temp = raw_input().strip().split(' ')
        temp[0] = int(temp[0])
        cases.append(temp)
    print(T, cases)
    for shieldStrength, robotsProgram in cases:
        print(leastHacks(shieldStrength, robotsProgram))
if __name__ == "__main__":
    main()