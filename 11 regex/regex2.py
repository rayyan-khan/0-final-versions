# regex homework 2, due 2/15 10:30 am rayyan khan

# Determine a regular expression which will match only
# on the indicated strings, or else will find the indicated
# matches. The form for the submission will be a command
# line script that takes a single integer as input from 41
# to 50, inclusive, and outputs the corresponding regular
# expression pattern, just as with the prior HW. The pattern
# is to be delimited by forward slashes and any options
# should immediately follow the final slash.

import sys

inp = int(sys.argv[1]) - 41 if len(sys.argv) > 1 else 0

# For problems 41-43, an Othello board will be construed to
# be and 8 × 8 board, represented as a single string, where
# holes (blanks) are indicated by a period (.), and the black
# tokens are indicated by either an x or X, and the white
# tokens are indicated by an o or O. The boards have no “buffer
# edge”. For the purposes of this problem, we are not concerned
# about whether we could actually reach a board in real play.
# For example, a board with tokens only at the corners would be
# considered a valid Othello board, and so would a completely
# empty board.

answerArray = [ # 41. Write a regular expression that will
               # match on an Othello board represented as a string.
               '/^([.xo]){64}$/i',

               # 42. Given a string of length 8, determine whether
               # it could represent an Othello edge with exactly one hole.
               '/^[xo]*\.[xo]*$/i',

               # 43. Given an Othello edge as a string, determine whether
               # there is a hole such that if X plays to the hole (assuming
               # it could), it will be connected to one of the corners
               # through X tokens.
               '/^(\.[xo.]*|[xo.]*\.|x+o*\.+[xo.]*|[xo.]*\.o*x+)$/i',

               # 44. Match on all strings of odd length.
               '/^(.)(..)*$/s',

               # 45. Match on all odd length binary strings starting with 0, and on even
               # length binary strings starting with 1.
               '/^((1[10])([10][10])*|0([10][10])*)$/',

               # 46. Match all words having two adjacent vowels that differ.
               '/\\b\w*(ae|ai|ao|au|ea|ei|eo|eu|ia|ie|io|iu|oa|oe|oi|ou|ua|ue|ui|uo)+\w*\\b/i',

               # 47. Match on all binary strings which DON’T contain the substring 110.
               '/^((0*(1?010)*)*1*|((10)(1?0)*)*1*|0*1*)$/',

               # 48. Match on all non-empty strings over the alphabet {a, b, c} that
               # contain at most one a.
               '/^([bc]+a?[bc]*|a)$/',

               # 49. Match on all non-empty strings over the alphabet {a, b, c} that
               # contain an even number of a's
               '/^([bc]([bc]*a[bc]*a)*[bc]*|(a[bc]*a[bc]*)+)$/',

               # 50. Match on all base 3 integer strings that are even.
               '/^(2([20]*1[20]*1)*[20]*|(1[20]*1[20]*)+)$/'
]

print(answerArray[inp])

# print(sum([len(k) for k in answerArray]))
