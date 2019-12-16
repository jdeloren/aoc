from aoc import DataAnalyzer
import math


def positions(values):
    position_list = list()
    for i in values:
        x = i[i.find("x=")+2:i.find(',', i.index('x='))]
        y = i[i.find("y=")+2:i.find(',', i.index('y='))]
        z = i[i.find("z=")+2:i.find('>', i.index('z='))]
        position_list.append((int(x), int(y), int(z)))

    return position_list


def steps(moons, count=10):

    def total_energy():
        energy = []
        for moon in moons:
            energy.append(sum([abs(m) for m in moon]))

        n = 0
        for vel in velocity_list:
            energy[n] *= sum([abs(v) for v in vel])
            n += 1

        return sum(energy)

    def step():

        def velocity(current, target, planetoids):
            x_adj = current[0]
            y_adj = current[1]
            z_adj = current[2]
            for oid in planetoids:
                x_adj += 0 if oid[0] == target[0] else 1 if oid[0] > target[0] else -1
                y_adj += 0 if oid[1] == target[1] else 1 if oid[1] > target[1] else -1
                z_adj += 0 if oid[2] == target[2] else 1 if oid[2] > target[2] else -1

            return x_adj, y_adj, z_adj

        m = 0
        for moon in moons:
            index = moons.index(moon)
            velocity_list[m] = (velocity(velocity_list[m], moon, moons[:index] + moons[index+1:]))
            m += 1

        n = 0
        for vel in velocity_list:
            moons[n] = (moons[n][0] + vel[0], moons[n][1] + vel[1], moons[n][2] + vel[2])
            n += 1

    velocity_list = list()

    for i in range(len(moons)):
        velocity_list.append((0,)*3)

    if count > 0:
        for i in range(count):
            step()

        print(f"Positions: {moons}")
        print(f"Kinetics: {velocity_list}")

        total = total_energy()
        print(f"Total energy in the system: {total}")
    else:
        cycle = [0, 0, 0]
        count = 1
        step()

        def _lcm(a, b):
            return a * b // math.gcd(a, b)

        while cycle[0] == 0 or cycle[1] == 0 or cycle[2] == 0:
            count += 1
            step()

            idles = []
            for i in range(len(velocity_list[0])):
                idles.append([x[i] for x in velocity_list].count(0))

            for i in range(len(velocity_list[0])):
                cycle[i] = count * 2 if idles[i] == len(velocity_list) and cycle[i] == 0 else cycle[i]

        full_cycle = _lcm(_lcm(cycle[0], cycle[1]), cycle[2])

        print(cycle)
        print(f"System takes {full_cycle} steps to repeat an existing state")


def second():
    moons = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
    print("(test)", end="")
    steps(moons, -1)

    moons = [(-8, -10, 0), (5, 5, 10), (2, -7, 3), (9, -8, -3)]
    print("(test)", end="")
    steps(moons, -1)

    values = DataAnalyzer.load("2019day12.txt")
    moons = positions(values)
    print("(12.1)", end="")
    steps(moons, -1)


def first():
    moons = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
    print("(test)", end="")
    steps(moons)

    values = DataAnalyzer.load("2019day12.txt")
    moons = positions(values)
    print("(12.1)", end="")
    steps(moons, 1000)


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
