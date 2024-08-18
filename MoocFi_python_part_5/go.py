def who_won(game_board: list):
  player_1 = 0
  player_2 = 0
  for i in game_board:
    for j in i:
      if j == 1:
        player_1 += 1
      elif j == 2:
        player_2 += 1
  if player_1 > player_2:
    return("Player 1 won")
  elif player_2 > player_1:
    return("Player 2 won")
  else:
    return(player_1, player_2)

game = [1,2,2,2], [2,1,1,1], [0,2,1,1]
print(who_won(game))