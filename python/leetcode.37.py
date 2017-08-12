class Solution(object):
    def read_problem(self, bd):
        nn = []
        for l in bd:
            nn.extend(map(lambda ch: 0 if ch == '.' else int(ch), l))
        return nn

    def lc_index(self, line, col):
        return line * 9 + col

    def index_lc(self, index):
        return int(index / 9), index % 9

    def get_box(self, index):
        '''
            box_id:
            0|1|2
            3|4|5
            6|7|8
        '''
        box_left_top = [0, 3, 6, 27, 30, 33, 54, 57, 60]
        l, c = self.index_lc(index)
        ldelta = int(l / 3) * 3
        cdelta = int(c / 3) 
        box_id = ldelta + cdelta
        start_id =  box_left_top[box_id]
        return [start_id, start_id+1, start_id+2, start_id+9, start_id+10, start_id+11, start_id+18, start_id+19, start_id+20]

    def get_line(self, index):
        start_id = int(index / 9) * 9
        return map(lambda x: x+start_id, range(9))

    def get_col(self, index):
        start_id = index % 9
        return map(lambda x: x*9+start_id, range(9))

    def get_value(self, index_list, board):
        return map(lambda x: board[x], index_list)

    def possible_ans(self, index, board):
        box = self.get_value(self.get_box(index), board)
        line = self.get_value(self.get_line(index), board)
        col = self.get_value(self.get_col(index), board)
        return list(set([1,2,3,4,5,6,7,8,9]) - set(filter(lambda x: x!=0, set(box+col+line))))

    def back_solver(self, board):
        res = []
        def solve_iter(board, blank):
            if len(blank) > 0:
                pa = self.possible_ans(blank[0], list(board))
                if len(pa) > 0:
                    for a in pa:
                        board[blank[0]] = a
                        solve_iter(list(board), blank[1:])
                        board[blank[0]] = 0
                else:
                    return
            else:
                res = list(board)
                self.res = res
                return

        blank = []
        for i, vi in zip(range(81), board):
            if vi == 0:
                blank.append(i)
        if len(blank) > 0:
            solve_iter(list(board), blank)
            # print self.res
            return self.res
        else:
            return board

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        newbd = self.read_problem(board)
        ans = self.back_solver(newbd)
        k = 0
        for i in xrange(9):
            ss = ""
            for j in xrange(9):
                ss += str(ans[k])
                k += 1
            board[i] = ss