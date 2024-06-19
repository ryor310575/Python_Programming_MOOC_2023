# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str)->bool:
    positions_status=True
    if x>2 or y>2 or x<0 or y<0:
        positions_status=False
    else:
        if game_board[y][x]=="":
            game_board[y][x]=piece
        else:
            positions_status=False
    return positions_status

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)