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
import sys

from Usage import usage


def cat(args):
    """concatenate files and print on the standard output"""
    if len(args) == 0:
        usage("Too few arguments", 'cat')

    for file in args:
        f = open(file)
        for line in f:
            print(line, end="")
        f.close()


def tac(args):
    """concatenate and print files in reverse"""
    if len(args) == 0:
        usage("Too few arguments", 'tac')
    for file in args:
        f = open(file)
        lines = f.readlines()
        for line in reversed(lines):
            print(line, end='')


def nl(args):
    """number lines of files"""
    if len(args) == 0:
        usage("Too few arguments", 'nl')

    include_blank_lines = False
    if args[0] == '-ba':
        include_blank_lines = True
        args = args[1:]

    line_number = 1

    for file in args:
        f = open(file)
        for line in f:
            if line.strip() == '' and not include_blank_lines:
                print(line, end='')
            else:
                print(f"{line_number}\t{line}", end='')
                line_number += 1
        f.close()
