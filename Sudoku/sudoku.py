"""
Only handles 9x9 sudokus. with a few changes if can accomodate othe rvariations.
Matrix Y contains 729 options/possibilities for each cell.
Matrix X contains 324 items/constrains Pij=ROWCOL_ij , Row_ik, Col_jk , Box_xk
	where i:row, j:column, k:number, x:box
Y=[(i,j,k)] =[(typeof_constrain, indexesof_constrain) *4 constrains] --4 contrains for each cell
X[(typeof_constrain, indexesof_constrain)] = [(i,j,k) *9] --before grid reduction

Empty grid for a little help placing the clues
grid = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

"""

from itertools import product
import time

N=9
# Extremely hard matrix -- 31.25ms to execute algorithm X
# grid from https://sudoku.com/evil/
grid = [
      [8, 4, 0, 0, 0, 6, 1, 0, 0],
      [0, 0, 7, 8, 0, 0, 0, 0, 0],
      [0, 0, 3, 0, 0, 0, 0, 0, 4],
      [7, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 0, 9, 0],
      [1, 8, 0, 9, 0, 0, 0, 0, 2],
      [0, 0, 0, 0, 5, 0, 6, 0, 0],
      [9, 2, 0, 3, 0, 0, 0, 0, 1],
      [0, 0, 4, 0, 0, 0, 0, 0, 0]]

# Initial Y matrix
Y={}
for i,j,k in product(range(N), range(N), range(1,N+1)):
	x = 3*(i//3) + (j//3) 
	Y[(i,j,k)]=[("P_ij", i,j),
			("R_ik", i,k),
			("C_jk", j,k),
			("B_xk", x,k)]

# Initial X matrix
X = ( {('P_ij', *pos):[] for pos in product(range(N), range(N))} |
	{('R_ik', *pos):[] for pos in product(range(N), range(1,N+1))} |
	{('C_jk', *pos):[] for pos in product(range(N), range(1,N+1))} |
	{('B_xk', *pos):[] for pos in product(range(N), range(1,N+1))}  )

# Populate X with options
for key, values in Y.items():
	for value in values:
		X[value].append(key)

# Reduce cover matrix by placing the clues 
popped_options=[]
for i, row in enumerate(grid):
	for j, k in enumerate(row):
		if k != 0:
			for value in Y[(i,j,k)]:
				for option in X[value]:
					Y.pop(option,None)
					popped_options.append(option)
				del X[value]

# Re-populate X by removing deleted options from items
for option in popped_options:
	for item, values in X.items():
		if option in values:
			X[item].remove(option)

# Algorithm X
def solve(T, S, sol=[]):
    if not T:
        # the first time T=={}
        return sol # for this return you can return nothing
    else:
        c = min(T, key=lambda c: len(T[c]))
        for r in T[c]:
            sol.append(r)

            selected_rows = {x for c in S[r] for x in T[c]}
            selected_cols = S[r]

            # reduce matrix T
            for col in selected_cols:
                T.pop(col)
            for key in T:
                for row in selected_rows:
                    if row in T[key]:
                        T[key].remove(row)

            solve(T, S, sol)
            # If T ever reaches {} you return to start
            # 	without reaching code for deselect.
            # So T=={} for all the previous calls and reach the start 
            if not T:
                return sol
            
            # Deselect
            for col in selected_cols:
                T[col] = []
            for row in selected_rows:
                for key in T:
                    if key in S[row]:
                        T[key].append(row)

            del sol[-1]

# Call algorithm X 
start = time.time()
solution = solve(T=X, S=Y)
print("- %s sec -" % (time.time() - start))

# Complete grid with solution and print it
for sol in solution:
    grid[sol[0]][sol[1]] = sol[2]

for row in grid:
    print(row,end='\n')

