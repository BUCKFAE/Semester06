"""Demonstration Program showing how many possible moves a chess pawn has"""

def calculate_possible_moves(size: int) -> int:
    """Calculates how many possible moves a chess pawn has on a n x n board"""

    # To small for any moves
    if size < 3:
        return 0

    if size == 3:
        # Two move from each field (but the middle one)
        return 16

    # 4 Corners
    corners = sum([4 * corner for corner in [2, 3, 3, 4]])

    # Border of the board
    border_length = max(0, size - 4)
    borders = sum([4 * border * border_length for border in [4, 6]])

    # Inner part of the board
    inner_length = max(0, size - 4)
    inner = 8 * inner_length * inner_length

    return corners + borders + inner

print('\n'.join(str(calculate_possible_moves(size)) for size in range(0, 10)))
