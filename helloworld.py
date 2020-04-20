# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

phone_book = {}
q = int(input())
for i in range(0, q):
    str = input()
    name, num = str.split()
    phone_book[name] = num
    for i in range(0, 100000):
        query = input()
        if (input != '\n'):
            if (phone_book.has_key(query)):
                print(phone_book.query + '=' + phone_book[query])
        else:
            break




