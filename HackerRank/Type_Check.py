s = input()
print(any(str1.isalnum() for str1 in s) )
print(any(str1.isalpha() for str1 in s) )
print(any(str1.isdigit() for str1 in s) )
print(any(str1.islower() for str1 in s) )
print(any(str1.isupper() for str1 in s) )