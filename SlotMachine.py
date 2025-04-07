import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Symbols with count and value
symbol_counts = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Please enter a valid positive number.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        print("Invalid number of lines.")

def get_bet():
    while True:
        amount = input(f"Enter bet per line (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        print("Invalid bet amount.")

def spin_slots(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            symbol = random.choice(current_symbols)
            current_symbols.remove(symbol)
            column.append(symbol)
        columns.append(column)
    return columns

def print_slots(columns):
    for row in range(ROWS):
        row_symbols = [columns[col][row] for col in range(COLS)]
        print(" | ".join(row_symbols))

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(symbol == columns[col][line] for col in range(1, COLS)):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def main():
    balance = deposit()

    while True:
        print(f"\nCurrent balance: ${balance}")
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Not enough balance to bet ${total_bet}.")
            continue

        balance -= total_bet
        print(f"\nSpinning... Betting ${bet} on {lines} lines.")

        slots = spin_slots(ROWS, COLS, symbol_counts)
        print_slots(slots)

        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
        balance += winnings

        print(f"\nYou won ${winnings}!")
        if winning_lines:
            print(f"Winning lines: {', '.join(map(str, winning_lines))}")
        else:
            print("No winning lines this round.")

        if balance <= 0:
            print("You ran out of money! Game over.")
            break

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            print(f"Thanks for playing! You left with ${balance}.")
            break

# Run the game
if __name__ == "__main__":
    main()
# This code implements a simple slot machine game with a betting system.
# Players can deposit money, choose the number of lines to bet on, and the bet amount.
# The game randomly generates a slot machine result and calculates winnings based on the symbols.
# The game continues until the player runs out of money or chooses to stop playing.
# The game uses a dictionary to define the symbols, their counts, and values.   