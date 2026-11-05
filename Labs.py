class Item:
    def __init__(self, name, size, survival_point):
            self.name = name
            self.size = size
            self.sp = survival_point

def dp_invetory(items, capacity, hp, Write):
    dp = [[] for _ in range(len(items))]
    for i in dp:
        for _ in range(len(items)):
                 i.append([0, 0, ''])
    dp[0][0][0] = hp
    dp[0][0][1] = capacity
    for j in range(1, len(items)):
        for i in range(j+1):
            if i == 0: # могу только взять 
                 if dp[i][j-1][1] - items[j-1].size >= 0: # могу взять и есть откуда
                    dp[i][j][0] = dp[i][j-1][0] + items[j-1].sp
                    dp[i][j][1] = dp[i][j-1][1] - items[j-1].size
                    dp[i][j][2] = dp[i][j-1][2] + items[j-1].name
                 else:
                    dp[i][j] = [0, 0, 'over'] # переход невозможен
            else:
                if i != j+1: # есть откуда сделать переход (по горизонтали)
                    if (dp[i][j-1][1] - items[j-1].size >= 0): # могу взять (переход по горизонтали)
                        if (dp[i][j-1][0] + items[j-1].sp >= dp[i-1][j-1][0] - items[j-1].sp) or dp[i][j-1][2] != 'over': #выгоднее взять
                            dp[i][j][0] = dp[i][j-1][0] + items[j-1].sp
                            dp[i][j][1] = dp[i][j-1][1] - items[j-1].size
                            dp[i][j][2] = dp[i][j-1][2] + items[j-1].name
                        else: # брать невыгодно
                            if dp[i-1][j-1][2] != 'over':
                                dp[i][j][0] = dp[i-1][j-1][0] - items[j-1].sp
                                dp[i][j][1] = dp[i-1][j-1][1]
                                dp[i][j][2] = dp[i-1][j-1][2]
                            else:
                                dp[i][j] = [0, 0, 'over'] 
                    else: # взять не могу так как нету места => могу только не взять
                        if dp[i-1][j-1][2] != 'over':
                            dp[i][j][0] = dp[i-1][j-1][0] - items[j-1].sp
                            dp[i][j][1] = dp[i-1][j-1][1]
                            dp[i][j][2] = dp[i-1][j-1][2]
                        else:
                            dp[i][j] = [0, 0, 'over']

    res = [dp[i][len(items)-1] for i in range(len(items))]
    ans = [0]
    for i in res:
        if i[0] > 0:
            if i[0] > ans[0]:
                ans = i
    if Write:
        list = dp
        for i in range(len(items)):
            for j in range(len(items)):
                if j != 0:
                    print('\t' + str(list[i][j][0]), end=' ')
                    if j == len(items)-1:
                        print('\t' + str(list[i][j][0]) + ' ' + str(list[i][j][1]) + ' ' + list[i][j][2] , end=' ')
                else:
                    print((list[i][j][0]), end=' ')
            print()
    return ans

if __name__ == '__main__':
    items = [
    Item("i", 1, 5),
    Item("r", 3, 25),
    Item("p", 2, 15),
    Item("a", 2, 15),
    Item("m", 2, 20),
    Item("k", 1, 15),
    Item("x", 3, 20),
    Item("t", 1, 25),
    Item("f", 1, 15),
    Item("d", 1, 10),
    Item("s", 2, 20),
    Item("c", 2, 20),]

    capacity = 9 
    hp = 15
    inventory = ['' for _ in range(capacity)]

    #БЕРЕМ ИНГОЛЯТОР
    ing_capacity = items[0].size
    ing_sp = items[0].sp
    capacity -= ing_capacity
    hp += ing_sp
    i = 0
    inventory[i] = items[0].name
    items.remove(items[0]) #так как нам обязательно нужен инголятор то просто добавим его параметры изначально, а его из списка удалим

    ans = dp_invetory(items, capacity, hp, True)

    print('\n', 'Подходящий вариант из таблицы', ans, '\n')

    for item in items:
        if item.name in ans[2]:
            for _ in range(item.size):
                i += 1
                inventory[i] = item.name
    line = 3
    for x in range(3):
        for j in inventory:
            if inventory.count(j) == 3-x:
                for y in j:
                    print(f'[{y}]', end=' ')
                    line -= 1
            if line == 0:
                line = 3 
                print()
                continue