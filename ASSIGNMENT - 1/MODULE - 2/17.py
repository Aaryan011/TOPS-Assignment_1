# Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string. 

str1=input("Enter string 1 :")
str2=input("Enter string 2 :")

x = str2[:2] + str1[2:]
y = str1[:2] + str2[2:]

print(x)
print(y)