maps=[1,2,3,
      4,5,6,
      7,8,9]
win_comb=((0,1,2),
          (3,4,5),
          (6,7,8),
          (0,3,6),
          (1,4,7),
          (2,5,8),
          (0,4,8),
          (2,4,6))
def print_maps():
    print('_'*21)
    for i in range(3):
        print(' | ',maps[0+i*3],' | ',maps[1+i*3],' | ',maps[2+i*3],' | ')
    print('-'*21)


def input_game(a):
    fl=True
    while fl:
        try:
            if a == 'X':
                ind=int(input('Введите номер клетки для Х: '))
            else:
                ind = int(input('Введите номер клетки для O: '))
        except:
            print('Некорректный ввод!!!')

            continue
        if ind>0 and ind<10:
            maps[ind-1]=a
            fl=False
        else:
            print('Число должно быть от 1 до 9!!!')

def win_game():
    win=''
    for line in win_comb:
        if maps[line[0]]==maps[line[1]]==maps[line[2]]:
            win=maps[line[0]]
            return win
    return win

def main():
    player1=False
    numm_hod=0
    while True:
        player1=not player1
        print_maps()
        if player1:
            a='X'
        else:
            a='O'
        input_game(a)
        numm_hod+=1
        if numm_hod<3:
            continue
        win_lose=win_game()
        if win_lose =='':

            if numm_hod>=9:
                print_maps()
                print('Ничья!')
                quit()
            else:
                continue
        print_maps()
        print(f'Победил {win_lose}!')
        break

main()
