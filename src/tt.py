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

  # DELETE ME
from Usage import usage


# Print statement debugging: display command line arguments
# This block of code may be removed before you submit your project
#
# You can keep this block so long as the output goes to sys.stderr
# for i, arg in enumerate(sys.argv):
#     num = f"arg #{i})"
#     print(f"{num:<8} {arg}", file=sys.stderr)
# print(file=sys.stderr)



# if len(sys.argv) < 2:
#     usage()
#     sys.exit(1)
#
# if tool == 'cat':
#     if len(args) < 1:
#         usage("Too few arguments", 'cat')
#         sys.exit(1)
#     cat(args)
# if tool == 'head':
#     if len(args) < 1:
#         usage("Too few arguments", 'head')
#         sys.exit(1)
#     if args[0] == '-n':
#         if len(args) < 2:
#             usage("Number of lines is required", 'head')
#             sys.exit(1)
#         if not args[1].isdigit():
#             usage("Number of lines is required", 'head')
#             sys.exit(1)
#     head(args)
# if tool == 'grep':
#     if len(args) < 1:
#         usage("Please provide a pattern and at least one filename", 'grep')
#         sys.exit(1)
#     if args[0] == '-v':
#         if len(args) < 3:
#             usage("Please provide a pattern and at least one filename", 'grep')
#             sys.exit(1)
#     if not args:
#         usage("Please provide a pattern and at least one filename", "grep")
#     grep(args)
# if tool == 'nl':
#     if len(args) < 1:
#         usage("Too few arguments", 'nl')
#         sys.exit(1)
#     nl(args)
# if tool == 'wc':
#     if len(args) < 1:
#         usage("Too few arguments", 'nl')
#         sys.exit(1)
#     wc(args)


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
