import chess
import time

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

# Easter egg message (vuoto)
EASTER_EGG_MESSAGE = ""

# Board display functions
def print_board(board):
    print("\n  " + " ".join("abcdefgh"))  # Intestazione delle colonne
    print("  " + "-" * 17)  # Linea separatrice
    for rank in range(8, 0, -1):  # Da 8 a 1
        row = f"{rank}|"
        for file in range(8):  # Da a a h
            square = chess.square(file, rank - 1)
            piece = board.piece_at(square)
            # Usiamo una formattazione fissa per allineare i pezzi
            row += f" {UNICODE_PIECES[piece.symbol()] if piece else UNICODE_PIECES['.']} |"
        print(row)
        print("  " + "-" * 17)  # Linea separatrice tra le righe
    print("  " + " ".join("abcdefgh") + "\n")  # Intestazione delle colonne

# AI logic
def get_best_move(board, depth=3):
    # Tabella delle trasposizioni
    transposition_table = {}

    best_move = None
    best_value = float('-inf')

    # Ricerca iterativa approfondita
    for current_depth in range(1, depth + 1):
        for move in board.legal_moves:
            board.push(move)
            move_value = minimax_alpha_beta(board, current_depth - 1, float('-inf'), float('inf'), False, transposition_table)
            board.pop()

            if move_value > best_value:
                best_value = move_value
                best_move = move

    return best_move

def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player, transposition_table):
    # Controllo della tabella delle trasposizioni
    fen = board.fen()
    if fen in transposition_table:
        return transposition_table[fen]

    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        # Euristica delle mosse killer e della storia
        moves = sorted(board.legal_moves, key=lambda move: move_ordering(move))
        for move in moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth-1, alpha, beta, False, transposition_table)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        # Memorizzazione nella tabella delle trasposizioni
        transposition_table[fen] = max_eval
        return max_eval
    else:
        min_eval = float('inf')
        # Euristica delle mosse killer e della storia
        moves = sorted(board.legal_moves, key=lambda move: move_ordering(move))
        for move in moves:
            board.push(move)
            eval = minimax_alpha_beta(board, depth-1, alpha, beta, True, transposition_table)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        # Memorizzazione nella tabella delle trasposizioni
        transposition_table[fen] = min_eval
        return min_eval

def move_ordering(move):
    # Implementa l'euristica delle mosse killer e della storia
    return 0 # Da implementare

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

            # Mobilità dei pezzi
            value += mobility(board, piece, square)

            # Controllo di colonne e diagonali
            value += control(board, piece, square)

    # Sicurezza del re
    value += king_safety(board)

    # Struttura dei pedoni e sviluppo dei pezzi
    value += positional_evaluation(board)

    return value

def mobility(board, piece, square):
    # Calcola il numero di mosse legali per il pezzo
    return len(list(board.legal_moves))

def control(board, piece, square):
    # Calcola il controllo di colonne e diagonali
    control_value = 0
    for move in board.legal_moves:
        if move.from_square == square:
            if move.to_square // 8 == square // 8 or move.to_square % 8 == square % 8: # Controllo di colonne e righe
                control_value += 0.1
            if abs(move.to_square // 8 - square // 8) == abs(move.to_square % 8 - square // 8): # Controllo di diagonali
                control_value += 0.1
    return control_value

def king_safety(board):
    # Valuta la sicurezza del re
    white_king_square = board.king(chess.WHITE)
    black_king_square = board.king(chess.BLACK)
    white_king_safety = len(list(board.attacks(white_king_square)))
    black_king_safety = len(list(board.attacks(black_king_square)))
    return black_king_safety - white_king_safety

def positional_evaluation(board):
    center_control = 0
    center_squares = [chess.E4, chess.E5, chess.D4, chess.D5]
    for square in center_squares:
        piece = board.piece_at(square)
        if piece and piece.color == chess.WHITE:
            center_control += 1
        elif piece and piece.color == chess.BLACK:
            center_control -= 1

    # Struttura dei pedoni (esempio semplificato)
    pawn_structure = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.PAWN:
            if piece.color == chess.WHITE and square // 8 > 3: # Pedoni bianchi avanzati
                pawn_structure += 0.1
            elif piece.color == chess.BLACK and square // 8 < 4: # Pedoni neri avanzati
                pawn_structure -= 0.1

    # Sviluppo dei pezzi (esempio semplificato)
    development = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type in [chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN]:
            if piece.color == chess.WHITE and square // 8 < 5: # Pezzi bianchi sviluppati
                development += 0.1
            elif piece.color == chess.BLACK and square // 8 > 2: # Pezzi neri sviluppati
                development -= 0.1

    return center_control + pawn_structure + development

# Game modes
def play_human_vs_ai():
    print("\nStarting new game...")
    while True:
        color
