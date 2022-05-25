def palindrom(s):
    return s == s[::-1]

#s = input('word : ')
#print(palindrom(s))


def annagrama(s1, s2):

    if len(s1) != len(s2):
        return False

    s1 = s1.lower()
    s2 = s2.lower()

    #'яна' 'аня' => ['а', 'н', 'я'] , ['я', 'н', 'а']

    arr1 = s1.split('')
    arr2 = s2.split('')

    arr1.sort()
    arr2.sort()

    return arr1 == arr2
print(annagrama("аня", "яна"))
