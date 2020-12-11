board = [[".", "6", ".", ".", "7", ".", "6", ".", "3"],
         [".", "2", ".", ".", ".", ".", ".", ".", "7"],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", ".", ".", ".", ".", "7", ".", ".", "."],
         [".", "9", "4", ".", ".", ".", "8", ".", "."],
         [".", ".", ".", "2", ".", ".", ".", ".", "."],
         [".", ".", ".", "6", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]


def ValidSudoku(board):
    row = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    column = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    box = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    row_dict = {}
    col_dict = {}
    for i in range(len(board)):
        for x in range(len(board[i])):
            box_index = int(i / 3) * 3 + int(x / 3)
            if board[i][x] in row[i].keys() or board[i][x] in column[x].keys() or board[i][x] in box[box_index].keys():
                return False

            else:
                if board[i][x] != ".":
                    row_dict[board[i][x]] = 1
                    row[i] = row_dict

                    temp_dict = column[x]
                    temp_dict[board[i][x]] = 1
                    column[x] = temp_dict

                    temp_dict = box[int(box_index)]
                    temp_dict[board[i][x]] = 1
                    box[int(box_index)] = temp_dict
        row_dict = {}

    return True


print("Board is: ...", ValidSudoku(board))
