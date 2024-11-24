#Given a string sample = "madamracecar", write a program that checks if the first half of the string is a palindrome of the second half (i.e., slice and compare).


s = "madamracecar"
if s[ : len(s) // 2 ] == s[ len(s) // 2 : ]:
    print("first half of the string is a palindrome of the second half ")
else:
    print("first half of the string is 'NOT' a palindrome of the second half ")
