import time

class Game:
    def __init__(self):
        self.initialize_game()
    #caro cấp 3 rỗng
    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # X đi trước
        self.player_turn = 'X'

    #xuất ra màn hình
    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    #Xác định xem bước đi có hợp lệ hay không
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    def is_end(self):
        #Nếu chiều dọc đủ
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and self.current_state[0][i] == self.current_state[1][i] and self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]
        #Nếu đường ngang đủ
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'
        #Đường chéo từ trái sang phải đủ
            if (self.current_state[0][0] != '.' and self.current_state[0][0] == self.current_state[1][1] and self.current_state[0][0] == self.current_state[2][2]):
                return self.current_state[0][0]
        #Đường chéo từ phải sang trái đủ
        if (self.current_state[0][2] != '.' and self.current_state[0][2] == self.current_state[1][1] and self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]
        #Nếu bảng caro full
        for i in range(0, 3):
            for j in range(0, 3):
                #Tìm thấy vị trí trống và tiếp tục trò chơi
                if (self.current_state[i][j] == '.'):
                    return None
        #Hòa
        return '.'

    def max(self):
        #-1 - thua
        #0  - hòa
        #1  - thắng
        #Đặt maxv = -2 để tìm trường hợp lớn nhất
        maxv = -2
        px = None
        py = None
        result = self.is_end()
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    #Đến lượt chơi của (O) thì gọi hàm min
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    #sửa lại giá trị maxv
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    #Trả lại vị trí rỗng, không đánh
                    self.current_state[i][j] = '.'
        return (maxv, px, py)
    
    def min(self):
        #-1 - thắng
        #0  - hòa
        #1  - thua
        #Đặt biến minv = 2 để tìm ra trường hợp nhỏ nhất
        minv = 2
        qx = None
        qy = None
        result = self.is_end()
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'
        return (minv, qx, qy)

    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_end()
            #In ra màn hình thông báo chiến thắng
            if self.result != None:
                if self.result == 'X':
                    print('X đã chiến thắng!')
                elif self.result == 'O':
                    print('O đã chiến thắng!')
                elif self.result == '.':
                    print("Trò chơi này đã hòa!")
                self.initialize_game()
                return
            #Lượt của mình (X)
            if self.player_turn == 'X':
                while True:
                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print('Bạn nên đi tại: dòng = {}, cột = {}'.format(qx, qy))
                    print("Đến lượt đi của bạn: ")
                    px = int(input('Nhập dòng: '))
                    py = int(input('Nhập cột: '))
                    (qx, qy) = (px, py)
                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('Nước đi không hợp lệ! Vui lòng thử lại.')
            #Lượt chơi của máy (O)
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'

#thực thi
def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()