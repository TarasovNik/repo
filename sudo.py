import pickle
import random
import copy

x1=[]
x2=[]
n = 3
board=[]

def print_board(bo):
    # печать таблицы
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


"ГЕНЕРАЦИЯ СУДОКУ"

# создание начальной таблицы 9*9
table = [[((i * n + i // n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]


def transpose(bo):
    # перестановка строк со столбцами
    bo = list(map(list, zip(*bo)))
    return bo


def raws_small(bo):
    # перестановка строк в пределах одной зоны
    k = random.randint(0, 2)
    k_qub = k * 3
    d = k // 3
    p = bo[k_qub:(k_qub + 2)]
    p_copy = copy.copy(p)
    while p == p_copy:
        random.shuffle(p)
    for i in range(k_qub, k_qub + 2):
        bo[i] = p[d]
        d += 1
    return bo


def columns_small(bo):
    # перестановка столбцов в пределах зоны
    return transpose(raws_small(transpose(bo)))


def raws_area(bo):
    # перестановка зон строк
    k = random.randint(0, 2)
    p = random.randint(0, 2)
    while p == k:
        p = random.randint(0, 2)
    p_qub = p * 3
    k_qub = k * 3
    for n in range(3):
        bo[(k_qub + n)], bo[(p_qub + n)] = bo[(p_qub + n)], bo[(k_qub + n)]
    return bo


def columns_area(bo):
    # перестановка зон столбцов
    return transpose(raws_area(transpose(bo)))


def mix_sudo(bo):
    # перетасовка стандартного судоку всеми способами
    x = []
    for n in range(random.randint(5, 10)):
        x = raws_area(columns_small(columns_area(columns_small(transpose(bo)))))
    return x


def sudo_gen(bo):
    # генерация судоку
    global x1
    global x2
    while x1 == x2:
        # проверка на единственное решение
        k, n = random.randint(0, 8), random.randint(0, 8)
        bo[k][n] = 0
        prosolve(copy.deepcopy(bo))
        antisolve(copy.deepcopy(bo))
    return bo


"РЕШЕНИЕ СУДОКУ"


def prosolve(bo):
    # решение судоку перебором от 1 до 9
    find = find_empty(bo)
    global x1
    x1=bo
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if prosolve(bo):
                return True
            bo[row][col] = 0
    return False


def antisolve(bo):
    # решение судоку перебором от 9 до 1
    find = find_empty(bo)
    global x2
    x2=bo
    if not find:
        return True
    else:
        row, col = find
    for i in range(9, 0, -1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if antisolve(bo):
                return True
            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    # проверка строки
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # проверка колонки
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # проверка 3*3
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def find_empty(bo):
    # поиск нулевого значения
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


####################### генерация, запись в файл, чтение, решение #########################

print('_'*10)
print('Генерация судоку')
print('_'*10)
print('Файл записан')
with open('data.pickle', 'wb') as f:
    pickle.dump(sudo_gen(mix_sudo(table)), f)
print('_'*10)



try:
    with open('data.pickle', 'rb') as f:
        board = pickle.load(f)
except Exception as e:
    print(e)
else:
    print('Судоку прочитан')
    print('_'*10)
    print_board(board)
    if prosolve(board):
        print('_'*10)
        print("Судоку решено!")
        print('_'*10)
        print_board(x1)
    else:
        print('У судоку нет решения')






