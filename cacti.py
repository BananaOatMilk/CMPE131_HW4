from typing import List

def cacti_number(plot: List[List[int]]) -> int:
   
 
    if not isinstance(plot, list) or len(plot) == 0:
        raise TypeError("Input must be a non-empty 2-D list")
    if not all(isinstance(row, list) for row in plot):
        raise TypeError("Input must be a 2-D list (list of lists)")
    cols = len(plot[0])
    if cols == 0 or any(len(row) != cols for row in plot):
        raise TypeError("All rows must have the same positive length")
    for row in plot:
        for v in row:
            if isinstance(v, bool) or not isinstance(v, int) or v not in (0, 1):
                raise TypeError("Grid values must be integers 0 or 1")

    # work on a copy so we don't modify the caller's list
    grid = [row[:] for row in plot]
    rows = len(grid)

    # checks if we can place a cactus at (r, c) given current grid
    def can_place(r: int, c: int) -> bool:
        if grid[r][c] != 0:
            return False
        # Check 4-neighbors only (up, down, left, right)
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                return False
        return True

    added = 0
    # greedy sweep: top→bottom, left→right, place whenever legal.
    for r in range(rows):
        for c in range(cols):
            if can_place(r, c):
                grid[r][c] = 1
                added += 1

    return added
