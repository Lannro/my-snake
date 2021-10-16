
def print_odict(odict, depth=0, name=""):
    if type(odict) == str or type(odict) == int:
        print("{}{}".format("   " * depth, odict))
    elif type(odict) == list or type(odict) == tuple:
        for i in range(len(odict)):
            if type(odict[i]) == str or type(odict[i]) == int:
                print("{}{}[{}] = {}".format("   " * (depth), name, i, odict[i]))
            else:
                print("{}{}[{}]".format("   " * (depth), name, i))
                print_odict(odict[i], depth+1)
    elif type(odict) == collections.OrderedDict or type(odict) == dict:
        for key in odict.keys():
            if type(odict[key]) == list or type(odict[key]) == dict or type(odict[key]) == collections.OrderedDict:
                print("{}{}[{}]".format("   " * depth, name, key))
                print_odict(odict[key], depth+1)
            else:
                print("{}{}[{}] = {}".format("   " * depth, name, key, odict[key]))

def print_board(board):
    print("".join(["[x]" for x in range(len(board)+2)]))
    for y in board:
        l = "[x]"
        for x in y:
            l += "[{}]".format(" " if x==0 else x)
        l += "[x]"
        print(l)
    print("".join(["[x]" for x in range(len(board)+2)]))

