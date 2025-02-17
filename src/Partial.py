#               Copyright © DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it isn't allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macrame, and warm (but
#  .'(  _.='         |            not frozen) desserts.
# {   ``  _.='       |         1. "The Program" refers to any copyrightable
#  {    \`     ;    /             work, recipe, or social media post
#   `.   `'=..'  .='              licensed under this License.
#     `=._    .='              2. "Licensees" and "recipients" may be
#  jgs  '-`\\`__                  individuals, organizations, or both;
#           `-._(                 further, they may be artificially or
#                                 naturally sentient (or close enough).
from Usage import usage


def head(args):
    """output the first part of files"""
    if len(args) == 0:
        usage("Too few arguments", 'head')
    if args[0] == '-n':
        if len(args) < 2 or not args[1].isdigit():
            usage("Number of lines is required", 'head')
        count = int(args[1])
        args.pop(0)
        args.pop(0)
        if len(args) == 0:
            usage("At least one filename is required", 'head')
    else:
        count = 10

    multiple_files = len(args) > 1

    for file in args:
        if multiple_files:
            print("\n")
            print("==> {} <==".format(file))
        f = open(file)
        i = 0
        for line in f:
            if i < count:
                print(line, end='')
                i += 1
        f.close()


def tail(args):
    """output the last part of files"""
    if len(args) == 0:
        usage("Too few arguments", 'head')
    if args[0] == '-n':
        if len(args) < 2 or not args[1].isdigit():
            usage("Number of lines is required", 'head')
        count = int(args[1])
        args.pop(0)
        args.pop(0)
        if len(args) == 0:
            usage("At least one filename is required", 'head')
    else:
        count = 10

    multiple_files = len(args) > 1

    for file in args:
        if multiple_files:
            print("\n")
            print("==> {} <==".format(file))
        f = open(file)
        lines = f.readlines()
        for line in lines[-count:]:
            print(line, end='')
        f.close()


