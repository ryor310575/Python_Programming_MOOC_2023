# Write your solution here
def who_won(game_board: list)->int:
    winner=0
    g1_counter=0
    g2_counter=0
    g1=1
    g2=2
    for row in game_board:
        for col in row:
            if col == g1:
                g1_counter += 1
            elif  col == g2:
                g2_counter += 1
    if g1_counter == g2_counter:
        winner=0
    elif g1_counter > g2_counter:
        winner=1
    else:
        winner=2
    return winner

if __name__ == "__main__":
    go = [[2, 1, 0, 0, 2, 0, 2, 0, 0],[0, 0, 0, 1, 1, 0, 2, 0, 0],[0, 2, 0, 1, 0, 0, 2, 0, 2],[0, 2, 2, 0, 0, 1, 0, 1, 0],[0, 1, 0, 1, 1, 0, 2, 2, 0],[1, 0, 1, 0, 2, 0, 2, 0, 2],[0, 0, 1, 1, 0, 2, 2, 0, 2],[0, 2, 1, 2, 0, 0, 2, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0, 2]]
    print(who_won(go))