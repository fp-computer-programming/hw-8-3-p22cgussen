# Charlie Gussen: CCG 12/9/21

def sum_odds(numbs):
    odd = 0
    x = 0
    while x < len(numbs):
        if int(numbs[x]) % 2 != 0:
            odd += x
            x += 1
        else:
            x += 1
    return odd

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)
