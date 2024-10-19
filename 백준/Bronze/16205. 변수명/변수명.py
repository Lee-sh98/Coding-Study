import sys

def camel_split(word):
    result = []
    tmp = ""
    for w in word:
        if w.isupper():
            result.append(tmp.lower())
            tmp = ""
        tmp += w

    if tmp:
        result.append(tmp.lower())
    return result

def snake_split(word):
    return word.split('_')

def pascal_split(word):
    result = []
    tmp = ""
    for w in word:
        if w.isupper() and tmp:
            result.append(tmp.lower())
            tmp = ""
        tmp += w

    if tmp:
        result.append(tmp.lower())
    return result

n, variable = sys.stdin.readline().split()
params = []
match int(n):
    case 1:
        params = camel_split(variable)
    case 2:
        params = snake_split(variable)
    case 3:
        params = pascal_split(variable)

first, *subsequent = params
print("".join([first]+list(map(str.title, subsequent))))
print("_".join(params))
print("".join(map(str.title, params)))
