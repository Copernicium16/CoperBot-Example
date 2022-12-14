import math

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

def sin_1(degree):
    if  degree % 180 == 0:
        sine=0
    else:
        rad=(math.pi*degree)/180
        sine=math.sin(rad)
    return sine

def cos_1(degree):
    rad=(math.pi*degree)/180
    cos=round(math.cos(rad), 3)
    if cos == 0:
        cos=0
        return cos
    else:
        return cos
    
def caesar_c(text, s):
    code_u1 = ""
    code_u2 = ""
    code_l1 = ""
    code_l2 = ""
    for i in range(s, len(upper)):
        code_u1 += upper[i]
        i += 1
    for i in range(s):
        code_u2 += upper[i]
        i += 1
    code_u = code_u1 + code_u2
    for i in range(s, len(lower)):
        code_l1 += lower[i]
        i += 1
    for i in range(s):
        code_l2 += lower[i]
        i += 1
    result = ""
    code_l = code_l1 + code_l2
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            char_dex = upper.index(char)
            result += code_u[char_dex]
        elif (char.islower()):
            char_dex = lower.index(char)
            result += code_l[char_dex]
        else:
            result = "Encode or decode word only..."
            break
    return(result)

def caesar_chiper(text, s):
    if s >= 0:
        shift = s % 26
    else:
        shift = s % -26
    return(caesar_c(text, shift))
