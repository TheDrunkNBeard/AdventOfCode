import re
total = 0

with open("Puzzle2.1/input.txt") as file:
    while line := file.readline():
        colors = ['eulb', 'neerg', 'der', 'emaG']
        gameNum = re.search('[0-9]+', line).group()
        game = re.split('[;:]+', line)
        gameBool = True

        for section in game[1:]:
            greenNum = 0
            blueNum = 0
            redNum = 0
            test = section.split(',')  # Initialize test list for each section

            for part in test:
                two = re.search('|'.join(colors), part[::-1]).group()

                for color in colors:
                    if two == color:
                        match two:
                            case 'neerg':
                                greenNum += int(re.search('[0-9]+', part).group())
                            case 'eulb':
                                blueNum += int(re.search('[0-9]+', part).group())
                            case 'der':
                                redNum += int(re.search('[0-9]+', part).group())
                if redNum > 12 or blueNum > 14 or greenNum > 13:
                    gameBool = False
                    break

        if gameBool:
            total += int(gameNum)

    print(total)
