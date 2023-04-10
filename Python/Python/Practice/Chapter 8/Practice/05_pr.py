def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Krishna is a good     "
n = remove_and_split(this, "Krishna")
print(n)