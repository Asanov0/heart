s = "kazak"
def palindrom(s):
    if len(s) <=1: 
        return "Да палиндром"
    if s[0] != s[-1]:
        return "Не палиндром"
    return palindrom(s[1: -1])

print(palindrom(len(s)))