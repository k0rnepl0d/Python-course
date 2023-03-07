a = 5
b = 6

result = 5 == 6
print(result)
print(a != 6)
print(a > b)
print(a < b)

bool1 = True
bool2 = False

print(bool1 == bool2)

age = 22
weight = 58

result = age > 21 and weight == 58
print(result)

age = 22
isMarried = False

result = age > 21 or isMarried
print(result)

age = 22
isMarried = False
print(not age > 21)
print(not isMarried)
print(not 4)
print(not 0)

message = 'hello world'
hello = 'hello'
print(hello in message)

gold = 'gold'
print(gold in message)

language = 'english'
if language == 'english':
    print('Hello')
print('End')

language = 'english'
if language == 'english':
    print('Hello')
    print('End')

language = 'russian'
if language == 'english':
    print('Hello')
else:
    print('Привет')
print('End')

language = 'german'
if language == 'english':
    print('Hello')
    print('World')
elif language == 'german':
    print('Hello')
    print('Welt')
else:
    print('Привет')
    print('мир')

language = 'english'
daytime = 'morning'
if language == 'english':
    print('English')
    if daytime == 'morning':
        print('Good morning')
    else:
        print('Good evening')
