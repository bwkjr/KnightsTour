import matplotlib.pyplot as plt

# Define the chess board size
N = 8

# Initialize the chess board
board = [[-1 for i in range(N)] for j in range(N)]

# Define the moves of the knight
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]

# Function to check if the move is valid
def is_valid_move(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if board[x][y] != -1:
        return False
    return True

# Function to solve the Knight's Tour problem using backtracking
def solve_knights_tour(x, y, move_number):
    if move_number == N * N:
        return True
    for move in moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if is_valid_move(new_x, new_y):
            board[new_x][new_y] = move_number
            if solve_knights_tour(new_x, new_y, move_number + 1):
                return True
            board[new_x][new_y] = -1
    return False

# Function to visualize the Knight's Tour
def visualize_knights_tour():
    plt.figure(figsize=(8, 8))
    for i in range(N):
        for j in range(N):
            plt.text(j + 0.5, N - i - 0.5, str(board[i][j]),
                     fontsize=20, ha='center', va='center', color='red')
            if (i + j) % 2 == 0:
                plt.gca().add_patch(plt.Rectangle((j, N - i - 1), 1, 1,
                                                  color='white'))
            else:
                plt.gca().add_patch(plt.Rectangle((j, N - i - 1), 1, 1,
                                                  color='black'))
    plt.xlim([0, N])
    plt.ylim([0, N])
    plt.xticks([])
    plt.yticks([])
    plt.show()

# Solve the Knight's Tour problem starting from the top-left corner
board[0][0] = 0
if solve_knights_tour(0, 0, 1):
    visualize_knights_tour()
else:
    print("No solution exists")

