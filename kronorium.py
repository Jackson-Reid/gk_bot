def get_input():
    start = int(input("""
1: Dept. Store
2: Armory
3: Infirmary
4: Tank Station
5: Supply Depot
6: Dragon Command  
"""))

    end = int(input("""
1: Dept. Store
2: Armory
3: Infirmary
4: Tank Station
5: Supply Depot
6: Dragon Command  
"""))

    return start, end


def output(start, end):
    ### ARMORY TO X ###

    if start == 2 and end == 4:
        print("""
Armory - 3
Dept. Store(3rd Floor) - 2
Infirmary - 1
Dragon Command - 2
Supply Depot - 3
Tank Factory - END
""")

    elif start == 2 and end == 1:
        print("""
Armory - 1
Dept. Store(3rd Floor) - END
Infirmary - 1
Dragon Command - 2
Supply Depot - 3
Tank Factory - 1
""")

    elif start == 2 and end == 6:
        print("""
Armory - 3
Dept. Store(3rd Floor) - 2
Infirmary - 2
Dragon Command - END
Supply Depot - 1
Tank Factory - 2
""")

    elif start == 2 and end == 5:
        print("""
Armory - 2
Dept. Store(3rd Floor) - 3
Infirmary - 1
Dragon Command - 1
Supply Depot - END
Tank Factory - 1
""")


    elif start == 2 and end == 3:
        print("""
Armory - 2
Dept. Store(3rd Floor) - 2
Infirmary - END
Dragon Command - 2
Supply Depot - 1
Tank Factory - 2
""")

    ### DEPT. STORE TO X ###

    elif start == 1 and end == 2:
        print("""
Armory - END
Dept. Store(3rd Floor) - 3
Infirmary - 2
Dragon Command - 3
Supply Depot - 2
Tank Factory - 2
""")

    elif start == 1 and end == 6:
        print("""
Armory - 1
Dept. Store(3rd Floor) - 2
Infirmary - 2
Dragon Command - END
Supply Depot - 1
Tank Factory - 3
""")

    elif start == 1 and end == 5:
        print("""
Armory - 2
Dept. Store(3rd Floor) - 1
Infirmary - 3
Dragon Command - 3
Supply Depot - END
Tank Factory - 1
""")

    elif start == 1 and end == 3:
        print("""
Armory - 2
Dept. Store(3rd Floor) - 1
Infirmary - END
Dragon Command - 3
Supply Depot - 1
Tank Factory - 2
""")


    elif start == 1 and end == 4:
        print("""
Armory - 2
Dept. Store(3rd Floor) - 2
Infirmary - 3
Dragon Command - 1
Supply Depot - 2
Tank Factory - END
""")
    ### DRAGON COMMAND TO X ###

    elif start == 6 and end == 5:
        print("""
Armory - 1
Dept. Store(3rd Floor) - 2
Infirmary - 2
Dragon Command - 2
Supply Depot - END
Tank Factory - 3
""")

    elif start == 6 and end == 3:
        print("""
Armory - 3
Dept. Store(3rd Floor) - 2
Infirmary - END
Dragon Command - 1
Supply Depot - 3
Tank Factory - 3
""")

    elif start == 6 and end == 4:
        print("""
Armory - 1
Dept. Store(3rd Floor) - 1
Infirmary - 1
Dragon Command - 3
Supply Depot - 3
Tank Factory - END
""")

    elif start == 6 and end == 1:
        print("""
Armory - 2
Dept. Store(3rd Floor) - END
Infirmary - 1
Dragon Command - 1
Supply Depot - 2
Tank Factory - 1
""")

    elif start == 6 and end == 2:
        print("""
Armory - END
Dept. Store(3rd Floor) - 1
Infirmary - 1
Dragon Command - 1
Supply Depot - 3
Tank Factory - 1
""")
    ### SUPPLY DEPOT TO X ###

    if start == 5 and end == 3:
        print("""
Armory - 3
Dept. Store(3rd Floor) -3
Infirmary - END
Dragon Command - 3
Supply Depot - 3
Tank Factory - 3
""")

    elif start == 5 and end == 4:
        print("""
Armory - 3
Dept. Store(3rd Floor) - 3
Infirmary - 2
Dragon Command - 3
Supply Depot - 2
Tank Factory - END
""")

    elif start == 5 and end == 6:
        print("""
Armory - 3
Dept. Store(3rd Floor) - 2
Infirmary - 3
Dragon Command - END
Supply Depot - 3
Tank Factory - 3
""")

    elif start == 5 and end == 1:
        print("""
Armory - 2
Dept. Store(3rd Floor) - END
Infirmary - 3
Dragon Command - 2
Supply Depot - 2
Tank Factory - 1
""")

    elif start == 5 and end == 2:
        print("""
Armory - END
Dept. Store(3rd Floor) - 1
Infirmary - 3
Dragon Command - 2
Supply Depot - 3
Tank Factory - 1
""")

    ### INFIRMARY TO X ###

    if start == 3 and end == 4:
        print("""
Armory - 1
Dept. Store(3rd Floor) - 1
Infirmary - 3
Dragon Command - 2
Supply Depot - 3
Tank Factory - END
""")

    elif start == 3 and end == 5:
        print("""
Armory - 2
Dept. Store(3rd Floor) - 1
Infirmary - 3
Dragon Command - 2
Supply Depot - END
Tank Factory - 2
""")

    elif start == 3 and end == 6:
        print("""
Armory - 2
Dept. Store(3rd Floor) - 3
Infirmary - 2
Dragon Command - END
Supply Depot - 2
Tank Factory - 2
""")

    elif start == 3 and end == 1:
        print("""
Armory - 3
Dept. Store(3rd Floor) - END
Infirmary - 3
Dragon Command - 1
Supply Depot - 3
Tank Factory - 3
""")

    elif start == 3 and end == 2:
        print("""
Armory - 2
Dept. Store(3rd Floor) - 1
Infirmary - 2
Dragon Command - 2
Supply Depot - 1
Tank Factory - 2
""")

    ### TANK TO X ###

    if start == 4 and end == 3:
        print("""
Armory - 3
Dept. Store(3rd Floor) - 3
Infirmary - END
Dragon Command - 3
Supply Depot - 2
Tank Factory - 2
""")

    elif start == 4 and end == 5:
        print("""
Armory - 1
Dept. Store(3rd Floor) - 1
Infirmary - 3
Dragon Command - 2
Supply Depot - END
Tank Factory - 1
""")

    elif start == 4 and end == 6:
        print("""
Armory - 1
Dept. Store(3rd Floor) - 1
Infirmary - 1
Dragon Command - END
Supply Depot - 1
Tank Factory - 1
""")

    elif start == 4 and end == 1:
        print("""
Armory - 3
Dept. Store(3rd Floor) - END
Infirmary - 3
Dragon Command - 1
Supply Depot - 2
Tank Factory - 1
""")

    elif start == 4 and end == 2:
        print("""
Armory - END
Dept. Store(3rd Floor) - 3
Infirmary - 1
Dragon Command - 1
Supply Depot - 2
Tank Factory - 1
""")

    #input("Enter to continue...")


def main():
    while True:
        choices = get_input()
        output(choices[0], choices[1])


if __name__ == '__main__':
    main()
