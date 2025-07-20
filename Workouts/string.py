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


# Return all substrings of a string that are palindromes (case-sensitive, length ≥ 1).
def pallidrome(s):
    result = set()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            subset = s[i:j]
            if subset == subset[::-1]:
                result.add(subset)
    return result
    
print(pallidrome('madam'))

# Given a string, return a new string where characters are sorted by descending frequency. 
# If two characters have the same frequency, keep their original order of appearance.
def frequency_sort(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    unique_chars = []
    for char in s:
        if char not in unique_chars:
            unique_chars.append(char)

    unique_chars.sort(key=lambda x: -freq[x])

    result = ''
    for char in unique_chars:
        result += char * freq[char]

    return result


print(frequency_sort("tree"))     #output : eetr
print(frequency_sort("abaabc"))   # output: aaabbc

# another version
def sort(s):
    count = {}
    new = ''
    for char in s:
        count[char] = count.get(char,0) + 1
    n = len(count)
    while count:
        maxx = max(count.items(), key = lambda x: x[1])
        new += maxx[0] * maxx[1]
        del count[maxx[0]]
    return new
    
    