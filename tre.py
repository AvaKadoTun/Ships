import random, math
class Ship:
    def __init__(self, x,y, width, size):
        self.x = x
        self.y = y
        self.width= width

        self.size= size

class Board:
    def __init__(self):
        self.ships=[1,1,1,1,2,2,3]
        self.board=[['O' for j in range(6)] for i in range(6)]
        self.hit = 'X'
        self.miss = 'T'
        self.lose = 5
        self.botshipshot = list(map(int,[str(i)+str(j) for j in range(1,7) for i in range(1,7)]))

    def draw(self):
        i=0
        print('  1 2 3 4 5 6')
        for row in self.board:
            i +=1
            print(i, end=' ')
            for elem in row:
                print(elem, end=' ')
            print()


    def add(self, ship):
        if ship.size == 'Вниз':
            for i in range(ship.width):
                self.board[ship.y-1+i][ship.x-1] = 'K'
        elif ship.size == 'Вправо':
            for i in range(ship.width):
                self.board[ship.y-1][ship.x-1+i] = 'K'

    def shot(self):
        remuv = True
        while remuv:
            remuv = False
            x = int(input('Введите значениех x выстрела'))
            y = int(input('Введите значениех y выстрела'))
            if self.board[y-1][x-1] == 'K':
                self.board[y - 1][x - 1] = self.hit
                self.lose += 1
            elif self.board[y-1][x-1] == 'O':
                self.board[y - 1][x - 1] = self.miss
            else:
                print ('В это место вы уже стреляли')
                remuv = True

    def botshot(self):
        n = random.choice(self.botshipshot)
        x = n // 10
        y = n % 10
        self.botshipshot.remove(n)
        if self.board[y-1][x-1] == 'K':
            self.board[y - 1][x - 1] = self.hit
            self.lose = self.lose +1
        elif self.board[y-1][x-1] == 'O':
            self.board[y - 1][x - 1] = self.miss
        else:
            print ('В это место вы уже стреляли')

    def bacik(self):
        i = 0
        for ship in self.ships:

            print('Расставлено ',i,' кораблей')
            width = ship
            print(f'Введите координату x для {ship} палубного коробля ')
            x = int(input())
            print(f'Введите координату y для {ship} палубного коробля ')
            y = int(input())
            print(f'Введите сторону: Вниз или Вправо для {ship} палубного коробля ')
            size = input()
            self.ships[i] = Ship(x,y,width,size)
            i += 1

    def bacikbot(self):
            self.ships[0] = Ship(1,1,1,'Вниз')
            self.ships[1] = Ship(1, 6, 1, 'Вниз')
            self.ships[2] = Ship(6, 1, 1, 'Вниз')
            self.ships[3] = Ship(6, 6, 1, 'Вниз')
            self.ships[4] = Ship(3, 1, 2, 'Вправо')
            self.ships[5] = Ship(3, 6, 2, 'Вправо')
            self.ships[6] = Ship(1, 4, 3, 'Вправо')





Player = Board()

II=Board()
II.bacikbot()

Player.bacik()
for ship in II.ships:
    II.add(ship)
for ship in Player.ships:
    Player.add(ship)
Player.draw()
II.draw()

while (II.lose < 11) or (Player.lose < 11):
    II.shot()
    Player.botshot()
    Player.draw()
    II.draw()
print('Игра закончилась')










