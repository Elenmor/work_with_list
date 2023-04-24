from itertools import compress

def test_list_cicle():
  a = [1, 4, 2, 3, 5, 8, 10, 11, 4, 6, 7]
  b=[elem for elem in a if elem < 6]
  print(b)
  assert [1, 4, 2, 3, 4]

  #print(*[a for a in [1, 4, 2, 3, 5, 8, 10, 11, 4, 6, 7] if a < 6])
  #print([elem for elem in a if elem < 6])

def test_list_filter():
    a = [1, 4, 2, 3, 5, 8, 10, 11, 4, 6, 7]
    print(*filter(lambda x: x < 6, a))


def test_list_comprehensions():
    a = [1, 4, 2, 3, 5, 8, 10, 11, 4, 6, 7]
    print(*compress(a, map(lambda x: x < 6, a)))

def test_palindrome():

    a = input('madam')
    if str(a) == str(a)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

        #Не смогла с числом
