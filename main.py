# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])  #Struktūra


def are_matching(left, right):
  return (left + right) in [
    "()", "[]", "{}"
  ]  #pārvbauda vai atveroša un aizverošā iekava sakrīt (atkriež true/false)


def find_mismatch(text):
  opening_brackets_stack = []  #definēta tukša struktura
  for i, next in enumerate(
      text  #cikls, paņem tekstu pa burtiem, ieliek masīvā (gan numuru un simbolu)
  ):

    if next in "([{":
      opening_brackets_stack.append(Bracket(next, i + 1))  #skaitīs uz priekšu

    if next in ")]}":
      if not opening_brackets_stack or not are_matching(
          opening_brackets_stack[-1].char,
          next):  #vai ir elementi un vai ir sakrītoši simboli
        return i + 1
      opening_brackets_stack.pop()  #izdzēšs

  if opening_brackets_stack:  # vai ir tukšs?
    #ja nav tukšs, tad ir pārbaude
    return opening_brackets_stack[-1].position
  return "Success"


def main():

  print("ievadīt no tastatūras ar Uppercase (I) vai atvērt no faila (F)?")
  i = input()

  if i == "I":
    print("ievadīt string no tastatūras: ")
    text = input()
    if len(text) >= 100000:
      print("teksts no tastatūras par garu: ")
      return
    mismatch = find_mismatch(text)
    print(mismatch)
    return
  if i == "F":
    print("ievadīt faila nosaukumu: ")
    i = input()
    text = open(i, "r")

    for line in text:
      print("faila sastāvs: ", line)


    mismatch = find_mismatch(line)
    if len(line) >= 100000:
      print("teksts no faila par garu: ")
      return
    print(mismatch)
    text.close()
    return

  else:
    print("nav pareizi ievadīts (I vai F)")
    return


if __name__ == "__main__":
  main()
