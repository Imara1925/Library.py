#V00701925 Imara Onunaku
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"


def is_alpha(word) -> bool:
    for letter in word:
        if letter not in ASCII_LOWERCASE and letter not in ASCII_UPPERCASE:
            return False
    return True

def is_digit(s) -> bool:
    for number in s:
        if number not in DECIMAL_DIGITS:
            return False
    return True

def to_lower(s) -> str:
  result = ""
  for char in s:
        if char in ASCII_UPPERCASE:
            index = ASCII_UPPERCASE.index(char)
            result += ASCII_LOWERCASE[index]
        else:
            result += char
        return result


def to_upper(s) -> str:
    result= ""
    for char in s:
        if char in ASCII_LOWERCASE:
            index = ASCII_LOWERCASE.index(char)
            result += ASCII_UPPERCASE[index]
        else:
            result += char
    return result


def find_chr(s, char):
    for i in range(len(s)):
        if s[i] == char:
            return i
        return -1

def find_str(s, substr):
    for i in range(len(s) - len(substr) +1):
        if s[i:i+len(substr)] == substr:
         return i
    return -1

def replace_chr(s, old, new):
        if old == "":
            return new + new.join(s) + new
        else:
            return s.replace(old, new)


def replace_str(s, old, new):
    result = s
    start = 0
    while start < len(s): 
         index = find_str(s[start:], old)
         if index == -1:
             break
         result = result[:index + start] + new + result[index + start + len(old):]
         start = index + len(new)
         s = result
    return result
