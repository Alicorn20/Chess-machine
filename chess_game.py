import chess

# Constants
UNICODE_PIECES = {
    'P': '♙', 'p': '♟',
    'R': '♖', 'r': '♜',
    'N': '♘', 'n': '♞',
    'B': '♗', 'b': '♝',
    'Q': '♕', 'q': '♛',
    'K': '♔', 'k': '♚',
    '.': '·'
}

# Easter egg message (personalizzabile)
EASTER_EGG_MESSAGE = " NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS  NIGGERS "

# Board display functions
def print_board(board):
    print("\n  a b c d e f g h")
    print("  ----------------")
    for rank in range(8, 0, -1):
        row = f"{rank}|"
        for file in range(8):
            square = chess.square(file, rank - 1)
            piece = board.piece_at(square)
            row += f" {UNICODE_PIECES[piece.symbol()] if piece else UNICODE_PIECES['.']}"
        print(row + f" |{rank}")
    print("  ----------------")
    print("  a b c d e f g h\n")

# AI logic
def get_best_move(board, depth=3):
    best_move = None
    best_value = float('-inf')

    for move in board.legal_moves:
        board.push(move)
        move_value = minimax_alpha_beta(board, depth-1, float('-inf'), float('inf'), False)
        board.pop()

        if move_value > best_value:
            best_value = move_value
            best_move = move

    return best_move

def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth-1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth-1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def evaluate_board(board):
    piece_values = {
        chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
        chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 100
    }
    value = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_value = piece_values.get(piece.piece_type, 0)
            value += piece_value if piece.color == chess.WHITE else -piece_value

    value += positional_evaluation(board)
    return value

def positional_evaluation(board):
    center_control = 0
    center_squares = [chess.E4, chess.E5, chess.D4, chess.D5]
    for square in center_squares:
        piece = board.piece_at(square)
        if piece and piece.color == chess.WHITE:
            center_control += 1
        elif piece and piece.color == chess.BLACK:
            center_control -= 1
    return center_control

# Game modes
def play_human_vs_ai():
    print("\nStarting new game...")
    board = chess.Board()
    print_board(board)

    while not board.is_game_over():
        move = input("Enter your move (e.g. e2e4) or 'exit' to quit: ")
        if move.lower() in ["exit", "quit"]:
            print("Game ended.")
            return
        
        try:
            board.push(chess.Move.from_uci(move))
        except ValueError:
            print("Invalid move, try again.")
            continue

        print_board(board)

        if board.is_game_over():
            break

        print("Computer is thinking...")
        best_move = get_best_move(board)
        board.push(best_move)
        print(f"Computer moved: {best_move.uci()}")
        print_board(board)

    print("Game over!")
    print("Result:", board.result())

def play_with_hints():
    print("\nStarting game with hints...")
    board = chess.Board()
    print_board(board)

    while not board.is_game_over():
        move = input("Enter your move or 'hint' for suggestion: ")
        if move.lower() in ["exit", "quit"]:
            print("Game ended.")
            return
        if move.lower() == "hint":
            suggestion = get_best_move(board)
            print(f"Computer suggestion: {suggestion.uci()}")
            continue
        
        try:
            board.push(chess.Move.from_uci(move))
        except ValueError:
            print("Invalid move, try again.")
            continue

        print_board(board)

        if board.is_game_over():
            break

        print("Computer is thinking...")
        best_move = get_best_move(board)
        board.push(best_move)
        print(f"Computer moved: {best_move.uci()}")
        print_board(board)

    print("Game over!")
    print("Result:", board.result())

def play_ai_vs_ai():
    print("\nStarting AI vs AI game...")
    board = chess.Board()
    depth = 3

    while not board.is_game_over():
        print_board(board)
        print("Computer 1 is thinking...")
        move1 = get_best_move(board, depth)
        board.push(move1)
        print(f"Computer 1 moved: {move1.uci()}")
        print_board(board)

        if board.is_game_over():
            break

        print("Computer 2 is thinking...")
        move2 = get_best_move(board, depth)
        board.push(move2)
        print(f"Computer 2 moved: {move2.uci()}")
        print_board(board)

    print("Game over!")
    print("Result:", board.result())

# Main menu
def main_menu():
    print("\nWelcome to Chess Game!")
    print("1. Human vs Computer")
    print("2. Game with Hints")
    print("3. Computer vs Computer")
    
    choice = input("Select mode (1-3): ")

    if choice == "1":
        play_human_vs_ai()
    elif choice == "2":
        play_with_hints()
    elif choice == "3":
        play_ai_vs_ai()
    elif choice.lower() == "palle":  # Easter egg
        while True:  # Ciclo infinito
            print(EASTER_EGG_MESSAGE)
    else:
        print("Invalid choice. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()
