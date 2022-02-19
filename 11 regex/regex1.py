# regex homework 1, due 2/13 10:30 am rayyan khan

# determine a regular expression which will match only on the indicated strings,
# or else will find the indicated matches.  The form for the submission will be
# a command line script that takes a single integer as input from 31 to 40,
# inclusive, and outputs the corresponding regular expression pattern, as it was
# done in class:  the pattern is to be delimited by forward slashes and any options
# should immediately follow the final slash.

import sys

inp = int(sys.argv[1]) - 31 if len(sys.argv) > 1 else 0

answerArray = [  # 31. Determine whether a string is either 0, 100, or 101.
               '/^0$|^10[10]$/',

               # 32. Determine whether a given string is a binary string
               # (ie. composed only of  0 and 1 characters).
               '/^[01]*$/',

               # 33. An integer (sub)string refers to a non-empty (sub)string
               # that will convert to an integer but has no leading 0.  Zero
               # is represented as the single digit 0.  Given a binary integer
               # string, what regular expression determines whether it is even?
               '/^0$|^1[01]*0$/',

               # 34. What is a regular expression to determine (ie. match) those
               # words in a text that have at least two vowels?
               '/\\b\w*[aeiou]\w*[aeiou]\w*\\b/i',

               # 35. Given a string, determine whether it is an even binary integer string.
               '/^0$|^1[01]*0$/',

               # 36. Determine whether a given string is a binary string containing
               # 110 as a substring.
               '/^[01]*110[01]*$/',

               # 37. Match on all strings of length at least two, but at most four.
               '/\A...?.?\Z/s',

               # 38. Validate a social security number entered into a field
               # (ie. recognize ddd-dd-dddd where the d represents digits and
               # where the dash indicates an arbitrary number of spaces with
               # at most one dash).  For example, 542786363,   542  786363,
               # and 542 – 78-6263 are all considered valid.
               '/^\d{3}\s*-?\s*\d\d\s*-?\s*\d{4}$/',

               # 39. Determine a regular expression to help you find the first
               # word of each line of text with a  d  in it.
               '/^.*?d\\b/m',

               # 40. Determine whether a string is a binary string that has the
               # same number of 01 substrings as 10 substrings.
               '/^1+[01]*0+[01]*1$|^0+[01]*1+[01]*0+$|^1+$|^0+$/'
                 ]

print(answerArray[inp])

# print(sum([len(k) for k in answerArray]))
