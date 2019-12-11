from aoc import DataAnalyzer
from anytree import Node, RenderTree

galaxy = dict()


def orbits(sun, debug=False):
    count = 0
    for pre, fill, node in RenderTree(sun):
        count += node.depth
        if debug:
            print("%s%s" % (pre, node.name))

    print("Total orbit, direct+indirect: {:d}".format(count))


def orbital_path(planet):
    path = list()
    current = planet
    while current is not None:
        current = current.parent
        if current is not None:
            path.append(current.name)

    return path


def steps(path, destination):
    count = 0
    for i in path:
        if i == destination:
            break
        count += 1

    return count


def locator(sun, source, target, debug=False):
    if debug:
        orbits(sun, True)

    src = trg = None
    for pre, fill, node in RenderTree(sun):
        if node.name == source:
            src = node
        if node.name == target:
            trg = node
        if src is not None and trg is not None:
            break

    src_planets = orbital_path(src)
    trg_planets = orbital_path(trg)

    common = None
    for planet in src_planets:
        if planet in trg_planets:
            common = planet
            break

    transfers = steps(src_planets, common)
    transfers += steps(trg_planets, common)
    print("Total transfers: {:d}".format(transfers))


def big_bang(system):
    global galaxy
    galaxy.clear()

    center = 'COM'
    wells = list()
    wells.append(center)
    planets = list()
    main = None

    while len(system) > 0:
        processed = list()
        for orbit in system:
            bodies = orbit.split(')')
            body1 = bodies[0].strip()
            body2 = bodies[1].strip()

            if body1 in wells:
                if body1 in galaxy:
                    node1 = galaxy[body1]
                else:
                    node1 = Node(body1)
                    if body1 == center:
                        main = node1

                if body2 in galaxy:
                    node2 = galaxy[body2]
                else:
                    wells.append(body2)
                    node2 = Node(body2, parent=node1)
                    planets.append(node2)
                    processed.append(orbit)

                # redundant, could be cleaner
                galaxy[body1] = node1
                galaxy[body2] = node2

        system = [x for x in system if x not in processed]

    return main


def second():
    values = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
    main = big_bang(values)
    locator(main, 'YOU', 'SAN', True)

    values = DataAnalyzer.load("2019day6.txt")
    main = big_bang(values)
    locator(main, 'YOU', 'SAN')


def first():
    values = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
    main = big_bang(values)
    orbits(main, True)

    values = DataAnalyzer.load("2019day6.txt")
    main = big_bang(values)
    orbits(main)


def solve(puzzle):
    if puzzle == '1':
        first()
    elif puzzle == '2':
        second()
    else:
        first()
        second()
