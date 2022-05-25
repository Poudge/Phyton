def palindrom(s):
    s == s.lower()
    if s == s[::-1]:
        print("палиндром")
    else:
        print('нет')


palindrom('око')
palindrom('анна')
palindrom('дед')
palindrom('вася')
