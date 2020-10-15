

def add_vectors(vector1, vector2):
    list1 = [0] * len(vector1)
    for i in range(len(vector1)):
        list1[i] = vector1[i] + vector2[i]
    return(list1)


print(add_vectors([1, 1], [1, 1]) == [2, 2])
print(add_vectors([1, 2], [1, 4]) == [2, 6])
print(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


def scalar_mult(scalar, vector):
    list2 = [0] * len(vector)
    for i in range(len(vector)):
        list2[i] = vector[i]*scalar
    return list2


print(scalar_mult(5, [1, 2]) == [5, 10])
print(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
print(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])


def dot_product(vec1, vec2):
    number = 0
    for i in range(len(vec1)):
        number += vec1[i]*vec2[i]
    return number


print(dot_product([1, 1], [1, 1]) == 2)
print(dot_product([1, 2], [1, 4]) == 9)
print(dot_product([1, 2, 1], [1, 4, 3]) == 12)


def cross_product(vec1, vec2):
    number2 = vec1[0]*vec2[1] - vec1[1]-vec2[0] + vec1[1]*vec2[2] - vec1[2]*vec2[1] + vec1[0]*vec2[2] - vec1[2]*vec2[0]
    return number2


print(cross_product([1, 2, 3], [2, 3, 4]) == -4)


# 9
song = "The    rain       in  Spain"
" ".join(song.split())

# 10


def replace(s, old, new):
    while old in s:
        s = s.replace(old, new)
    return s


print(replace("Mississippi", "i", "I") == "MIssIssIppI")
song = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(song, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
print(replace(song, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

