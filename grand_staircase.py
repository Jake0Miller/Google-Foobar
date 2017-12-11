def answer(n_bricks):
  # each column represents the number of bricks
  # each row represents the height of the tallest step in a staircase
  # everything above row 2 is meaningless
  # everything above the diagonal represents possible staircases, cumulatively, downward
  # everything on or below diagonal represents staircases possible by adding onto smaller staircases
  combos = [[0 for rows in range(n_bricks+1)] for cols in range(n_bricks)]
  combos[0][0] = 1
  
  # iterate over tallest step in staircase design
  for tallest in range(1,n_bricks):
    
    # iterate over number of bricks available for design
    for bricks in range(0,n_bricks+1):
      
      # start with number of shorter staircases possible with same n_bricks
      combos[tallest][bricks] = combos[tallest-1][bricks]
      
      # if bricks available >= height of tallest step
      # create a new tallest step
      # then add the number of smaller staircases possible with remaining bricks
      if bricks >= tallest:
        combos[tallest][bricks] += combos[tallest-1][bricks-tallest]
        
  return combos[n_bricks-1][n_bricks]