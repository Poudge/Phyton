

s1 = "SOSSOS"
s2 = "SERSETSOR"


def countErrors(s):
    array = []
    count = 0
    for i in range(3, len(s)+1, 3):
        array.append(s[i-3:i])

    #print(array)

    for word in array:
        if word[0] != "S":
            count += 1
        if word[1] != "0":
            count += 1
        if word[2] != "S":
            count += 1

    print(count)

countErrors(s1)
countErrors(s2)
