

try:
    print(x)

except:
    print('An error has occured')


try:
    f = open('test.txt')
    print('try f is open')
    f.write('sample message...')
except:
    print('Something went wrong')
finally:
    f.close()
    print('finally f object is closed')
