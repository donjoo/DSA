def replace_alphabets(string,n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    mapping = {}
    for i, char in enumerate(alphabet):
        replacement_index = (i + n) % 26 
        mapping[char] = alphabet[replacement_index]
    
    replaced_string = ''
    for char in string:
        if char.lower() in alphabet:
            if char.isupper():
                replaced_string += mapping[char.lower()].upper()
            else:
                replaced_string += mapping[char.lower()]
        else:
            replaced_string += char
    
    return replaced_string


string = "hello, world!"
n = 3
result = replace_alphabets(string, n)
print("Original String:", string)
print("Replaced String:", result)




def reverse_words(s):
    words = s.split()
    print(words)
    reversed_words = ' '.join(reversed(words))
    return reversed_words


s = "the sky is blue"
print(reverse_words(s)) 

def reverse_words(s):
    words = s.split()
    reverse_words = ' '.join(reversed(words))
    return reverse_words


def is_palindrome(s):
    cleaned_string = ''.join(e for e in s if e.isalnum()).lower()
    print(cleaned_string)
    return cleaned_string == cleaned_string[::-1]


s = "malayalamm"
print(is_palindrome(s)) 



