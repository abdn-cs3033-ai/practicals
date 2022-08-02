from random import choice


def printBoard(result, results):
    if not result:
        print([None])
    if results == 0 and result:
        r = choice(result)
        # print r
        board = []
        for col in r:
            line = ['.'] * len(r)
            line[col] = 'Q'
            board.append(str().join(line))

        charlist = list(map(list, board))
        for line in charlist:
            print(" ".join(line))
    else:
        board = []
        for r in result:
            for c in r:
                line = ['.'] * len(r)
                line[c] = 'Q'
                board.append(str().join(line))

        charlist = list(map(list, board))
        for i in range(0, len(charlist)):
            if i % len(charlist[i]) == 0:
                print("\n")
            print((" ".join(charlist[i])))
    print("\n")
