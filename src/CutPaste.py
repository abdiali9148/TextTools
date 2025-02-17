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


def cut(args):
    # """remove sections from each line of files"""
    # if len(args) == 0:
    #     usage("Too few arguments", "cut")
    # if args[0] == "-f":
    print("TODO: remove sections from each line of files")


def paste(args):
    if len(args) == 0:
        usage("Too few arguments", "paste")

    files = []
    max_lines = 0

    for file in args:
        f = open(file)
        lines = []
        for line in f:
            lines.append(line.rstrip('\n'))
        files.append(lines)
        if len(lines) > max_lines:
            max_lines = len(lines)

    for i in range(max_lines):
        line_parts = []
        for lines in files:
            if i < len(lines):
                line_parts.append(lines[i])
            else:
                line_parts.append('')
        print(','.join(line_parts))
