import re

# 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b's.
pattern1 = r"a[b]*"
test_string1 = "abbbb"
result1 = re.match(pattern1, test_string1)
print("1. Match 'a' followed by zero or more 'b's:", result1.group() if result1 else "No match")

# 2. Write a Python program that matches a string that has an 'a' followed by two to three 'b's.
pattern2 = r"a[b]{2,3}"
test_string2 = "abb"
result2 = re.match(pattern2, test_string2)
print("2. Match 'a' followed by two to three 'b's:", result2.group() if result2 else "No match")

# 3. Write a Python program to find sequences of lowercase letters joined with an underscore.
pattern3 = r"[a-z]+(?:_[a-z]+)*"
test_string3 = "hello_world_example"
result3 = re.findall(pattern3, test_string3)
print("3. Sequences of lowercase letters joined with an underscore:", result3)

# 4. Write a Python program to find the sequences of one uppercase letter followed by lowercase letters.
pattern4 = r"[A-Z][a-z]+"
test_string4 = "Hello World"
result4 = re.findall(pattern4, test_string4)
print("4. Sequences of one uppercase letter followed by lowercase letters:", result4)

# 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
pattern5 = r"a.*b$"
test_string5 = "abcdefb"
result5 = re.match(pattern5, test_string5)
print("5. Match 'a' followed by anything, ending in 'b':", result5.group() if result5 else "No match")

# 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
pattern6 = r"[ ,.]"
test_string6 = "Hello, world. How are you?"
result6 = re.sub(pattern6, ":", test_string6)
print("6. Replace space, comma, or dot with a colon:", result6)

# 7. Write a Python program to convert snake case string to camel case string.
pattern7 = r"_(.)"
test_string7 = "hello_world_example"
result7 = re.sub(pattern7, lambda x: x.group(1).upper(), test_string7)
print("7. Convert snake case to camel case:", result7)

# 8. Write a Python program to split a string at uppercase letters.
pattern8 = r"(?=[A-Z])"
test_string8 = "HelloWorldExample"
result8 = re.split(pattern8, test_string8)
print("8. Split string at uppercase letters:", result8)

# 9. Write a Python program to insert spaces between words starting with capital letters.
pattern9 = r"([a-z])([A-Z])"
test_string9 = "HelloWorldExample"
result9 = re.sub(pattern9, r"\1 \2", test_string9)
print("9. Insert spaces between words starting with capital letters:", result9)

# 10. Write a Python program to convert a given camel case string to snake case.
pattern10 = r"([a-z0-9])([A-Z])"
test_string10 = "helloWorldExample"
result10 = re.sub(pattern10, r"\1_\2", test_string10).lower()
print("10. Convert camel case to snake case:", result10)