

def alphabet(string):
    nospace = "".join(string.split())  # delete spaces
    letters = list(nospace.lower())  # first lowers the capital letters and then separate the characters in the string
    sort = sorted(letters)
    counts = {}
    letter = []
    for i in sort:
        counts[i] = counts.get(i, 0) + 1
    return counts


print(alphabet("ThiS is String with Upper and lower case Letters"))