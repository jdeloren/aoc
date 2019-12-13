from aoc import DataAnalyzer


def positions(values):
    position_list = list()
    for i in values:
        x = i[i.find("x=")+2:i.find(',', i.index('x='))]
        y = i[i.find("y=")+2:i.find(',', i.index('y='))]
        z = i[i.find("z=")+2:i.find('>', i.index('z='))]
        position_list.append((x, y, z))

    return position_list


def velocity(target, moons):
    x_adj = y_adj = z_adj = 0
    for moon in moons:
        x_adj += 0 if moon[0] == target[0] else 1 if moon[0] > target[0] else -1
        y_adj += 0 if moon[1] == target[1] else 1 if moon[1] > target[1] else -1
        z_adj += 0 if moon[2] == target[2] else 1 if moon[2] > target[2] else -1

    return x_adj, y_adj, z_adj


def step(moons):
    velocity_list = list()

    for moon in moons:
        index = moons.index(moon)
        velocity_list.append(velocity(moon, moons[:index] + moons[index+1:]))

    print(f"Velocities: {velocity_list}")

    i = 0
    for vel in velocity_list:
        moons[i] = (moons[i][0] + vel[0], moons[i][1] + vel[1], moons[i][2] + vel[2])
        i += 1

    print(f"Positions: {moons}")


def steps(moons, count=10):
    print(f"Positions: {moons}")
    for i in range(count):
        step(moons)


def second():
    values = DataAnalyzer.load("2019day12.txt")
    moons = positions(values)
    steps(moons)


def first():
    moons = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
    steps(moons)

    # values = DataAnalyzer.load("2019day12.txt")
    # moons = positions(values)
    # steps(moons)


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
