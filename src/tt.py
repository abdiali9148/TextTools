#!/usr/bin/env python

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
from Concatenate import cat, nl, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        usage(error="Too few arguments were given")
    elif sys.argv[1] == "cat":
        cat(sys.argv[2:])
    elif sys.argv[1] == "head":
        head(sys.argv[2:])
    elif sys.argv[1] == "grep":
        grep(sys.argv[2:])
    elif sys.argv[1] == "nl":
        nl(sys.argv[2:])
    elif sys.argv[1] == "wc":
        wc(sys.argv[2:])
    elif sys.argv[1] == "sort":
        sort(sys.argv[2:])
    elif sys.argv[1] == "tac":
        tac(sys.argv[2:])
    elif sys.argv[1] == "tail":
        tail(sys.argv[2:])
    elif sys.argv[1] == "cut":
        cut(sys.argv[2:])
    elif sys.argv[1] == "paste":
        paste(sys.argv[2:])
    else:
        usage(error=f"Unknown tool {sys.argv[1]}")
