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


def wc(files):
    total_lines = 0
    total_words = 0
    total_bytes = 0

    if len(files) == 0:
        usage("Too few arguments", 'wc')

    for file in files:
        f = open(file)
        lines = f.readlines()
        line_count = len(lines)
        word_count = 0

        # i asked the internet how to read the byte count of a file
        byte_count = 0
        for line in lines:
            byte_count += len(line)
            word_count += len(line.split())

        print(f"{line_count:>7} {word_count:>7} {byte_count:>7} {file}")
        total_lines += line_count
        total_words += word_count
        total_bytes += byte_count

    if len(files) > 1:
        print(f"{total_lines:>7} {total_words:>7} {total_bytes:>7} total")