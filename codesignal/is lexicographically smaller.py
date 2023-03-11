"""LAST HIDDENT TEST DID NOT PASS

Given two strings s and t both consisting of lowercase English
letters and digits, your task is to calculate
how many ways exactly one digit could be removed from
one of the strings so that s is lexicographically
smaller than t after the removal. Note that we are removing
only a single instance of a single digit, rather
than all instances (eg: removing 1 from the string al1b1c
could result in albic or allbc but not abc ).
Also note that digits are considered lexicographically smaller than letters.

NOT ALL TEST CASES PASSED
"""


def solution(s, t):
    def lexicographical_order(string1, string2):
        i = 0
        while i < len(string1) and i < len(string2):
            if string1[i] < string2[i]:
                return True
            elif string1[i] > string2[i]:
                return False
            i += 1
        return len(string1) <= len(string2)

    count = 0

    for i in s:
        if i.isdigit():
            index = s.index(i)
            remove_digit = s[:index] + s[index + 1:]
            if lexicographical_order(remove_digit, t):
                count += 1
            else:
                s = s[:index] + i + s[index + 1:]

    for i in t:
        if i.isdigit():
            index = t.index(i)
            remove_digit = t[:index] + t[index + 1:]
            if lexicographical_order(s, remove_digit):
                count += 1
            else:
                t = t[:index] + i + t[index + 1:]
    return count


s = "ab12c"
t = "ab24z"
print(solution(s, t))
