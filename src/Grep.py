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


def grep(args):
    """print lines that match patterns"""
    invert = False
    if len(args) == 0:
        usage("Please provide a pattern and at least one filename", 'grep')

    if args[0] == '-v':
        if len(args) < 3:
            usage("Please provide a pattern and at least one filename", 'grep')
        invert = True
        pattern = args[1]
        args.pop(0)
        args.pop(0)
        if len(args) == 0:
            usage("Please provide a pattern and at least one filename", 'grep')
    else:
        pattern = args[0]
        args.pop(0)
        if len(args) == 0:
            usage("Please provide a pattern and at least one filename", 'grep')

    for file in args:
        f = open(file)
        for line in f:
            line = line.rstrip()
            if (pattern in line) != invert:
                if len(args) > 1:
                    print(f"{file}:{line}")
                else:
                    print(line)
        f.close()
