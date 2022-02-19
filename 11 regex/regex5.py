# regex homework 4, due 3/1 10:30 am rayyan khan

# Determine a regular expression which will match only
# on the indicated strings, or else will find the indicated
# matches. The form for the submission will be a command
# line script that takes a single integer as input from 71
# to 80, inclusive, and outputs the corresponding regular
# expression pattern, just as with the prior HW. The pattern
# is to be delimited by forward slashes and any options
# should immediately follow the final slash.

import sys

inp = int(sys.argv[1]) - 71 if len(sys.argv) > 1 else 0

answerArray = [ # 71. Find the shortest word where some letter occurs 4 times.
                '/(?=\\b\w*(\w)(\w*\\1\w*){3}\\b)\w{,6}$/im',

                # 72. Find the shortest word where each vowel appears at least once.
                '/\\b(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w{,7}$/im',

                # 73. Find the longest word containing exactly 5 vowels.
                '/^(?=\w{18,})([b-d,f-h,j-n,p-t,v-z]*[aeiou]){5}[b-d,f-h,j-n,p-t,v-z]*$/mi',

                # 74. Find the longest word where the first three letters form a
                # palindrome with the final three letters.
                '/(?=\w*(.)(.)(.)$)^\\3\\2\\1\w{8,}/im',

                # 75. Find the longest word with the longest contiguous block of
                # one letter.
                '/(?=\\b\w*(\w)\\1{1,}\w*\\b)\w{18,}$/m',

                # 76. Find the longest word with the greatest number of a repeated
                # letters.
                '/\w*(\w)(\w*\\1){5,}\w*$/im',

                # 77. Find the longest word with the most number of adjacent pairs
                # of identical letters.
                '/(?=\w{13,})(\w*?(\w)\\2){3,}\w*$/im',

                # 78. Find the longest word where each letter is repeated at least
                # once.
                '',

                # 79. Find the longest word where each letter is repeated exactly
                # one time.
                '',

                # 80. Find the longest word where no letter is repeated more than
                # once.
                '/^(?:(\w)(?!.*\\1.*\\1)){18,}$/im'
]

print(answerArray[inp])
