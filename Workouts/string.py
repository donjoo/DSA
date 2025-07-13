# Check if Two Strings Are Anagrams (Without sorted())
# Task: Return True if one string is an anagram of the other.
# # Input: "listen", "silent"
# # Output: True
# Twist: Account for spaces and case insensitivity.
def ana(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    
    if len(str1) != len(str2):
        return False
        
    str1_map = {}
    str2_map = {}
    
    for char in str1:
        str1_map[char] = str1_map.get(char,0) +1 
    for char in str2:
        str2_map[char] = str2_map.get(char,0) +1

    return str1_map == str2_map
    
print(ana("listen", "silEnt"))



# Replace all occurrences of a substring old in string text with a new substring new.
text = "ababab"
old = "ab"
new = "xy"
n = 2
# Output: "xyxyxy"
# Task: Replace the first n occurrences of old with new in text.
def replace(text,old,new,n):
    i = 0
    result = ''
    count  = 0
    
    while i < len(text):
        if text[i:i+ len(old)] == old and count < n:
            result += new
            i += len(old)
            count += 1
        else:
            result += text[i]
            i += 1
    return result
    
print(replace(text,old,new,n))





    