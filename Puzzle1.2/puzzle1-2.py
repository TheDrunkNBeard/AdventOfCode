import re
total = 0
wordlist = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4','5','6','7','8','9','enin', 'thgie','neves','xis','evif','ruof','eerht','owt','eno']
with open("Puzzle1.2/input.txt") as file:
    while line := file.readline():
        one = re.search('|'.join(wordlist), line).group()
        two = re.search('|'.join(wordlist), line[::-1]).group()
        for word in wordlist:
            if(one == word):
                match one:
                    case 'one':
                        one = '1'
                    case 'two':
                        one = '2'
                    case 'three':
                        one = '3'
                    case 'four':
                        one = '4'
                    case 'five':
                        one = '5'
                    case 'six':
                        one = '6'
                    case 'seven':
                        one = '7'
                    case 'eight':
                        one = '8'
                    case 'nine':
                        one = '9'
            if(two == word):
                match two:
                    case 'eno':
                        two = '1'
                    case 'owt':
                        two = '2'
                    case 'eerht':
                        two = '3'
                    case 'ruof':
                        two = '4'
                    case 'evif':
                        two = '5'
                    case 'xis':
                        two = '6'
                    case 'neves':
                        two = '7'
                    case 'thgie':
                        two = '8'
                    case 'enin':
                        two = '9'
        total += int(one + two)
    print(total)