# regex homework 3, due 2/22 10:30 am rayyan khan

# Determine a regular expression which will match only
# on the indicated strings, or else will find the indicated
# matches. The form for the submission will be a command
# line script that takes a single integer as input from 41
# to 50, inclusive, and outputs the corresponding regular
# expression pattern, just as with the prior HW. The pattern
# is to be delimited by forward slashes and any options
# should immediately follow the final slash.

import sys

inp = int(sys.argv[1]) - 51 if len(sys.argv) > 1 else 0

# For problems 51-53 no look ahead or look behind is allowed.
# For the remaining problems, you may use the full power of
# Python's regular expressions. For all the problems mentioning
# words (rather than strings), substrings and other comparisons
# are meant to be case insensitive unless otherwise specified.
# With strings, the default is case sensitive.

answerArray = [ # 51. Match all words where some letter appears
                # twice in the same word.
                '/\\b\w*(\w)\w*\\1\w*\\b/i',

                # 52. Match all words where some letter appears 4
                # times in the same word.
                '/\\b\w*(\w)(\w*\\1\w*){2}\\b/i',

                # 53. Match all non-empty binary strings with the same
                # number of 01 substrings as 10 substrings.
                '/^([01])([01]*\\1)*$/',

                # 54. Match all 6 letter words containing the substring
                # 'cat'.
                '/(?=\\b\w{6}\\b)\w*cat\w*/i',

                # 55. Match all 5-9 letter words containing both the
                # substrings bri and ing.
                '/(?=\w*bri.*)(?=\w*i?ng)\\b\w{5,9}\\b/i',

                # 56. Match all 6 letter words not containing the
                # substring 'cat'.
                '/(?!\w*cat.*)\\b\w{6}\\b/i',

                # 57. Match all words with no repeated characters.
                '/(?!\w*(\w)\w*\\1\w*)\\b\w+/i',

                # 58. Match all binary strings not containing the
                # forbidden substring 10011.
                '/(?!.*10011.*)^[01]*$/',

                # 59. Match all words having two different adjacent
                # vowels.
                '/\w*([aeiou])(?!\\1)[aeiou]\w*/i',

                # 60. Match all binary strings containing neither 101 nor
                # 111 as substrings.
                '/(?![01]*(1.1)[01]*)^[01]*$/'
]

print(answerArray[inp])
