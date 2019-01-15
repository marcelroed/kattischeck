X = int(input())
# True if male
people = [(i == "M") for i in input()]
people.reverse()
firstlen = len(people)
women = 0
men = 0

def dist(men, women):
    return abs(men - women)

def lacking(men, women):
    return men < women

while True:
    if len(people) == 0:
        break
    if dist(men, women) == X:
        lack = lacking(men, women)
        if people[-1] == lack:
            if lack: men += 1
            else: women += 1
            people.pop()
        elif len(people) >= 2 and people[-2] == lack:
            if lack: men += 1
            else: women += 1
            people.pop(-2)
        else:
            break
    else:
        if people.pop(): men += 1
        else: women += 1

print(firstlen - len(people))
