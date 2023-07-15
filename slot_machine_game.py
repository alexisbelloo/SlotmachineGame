import random

# max and min amounts
maxLines = 3
maxBet = 100
minBet = 1

# slot structure
rows = 3
cols = 3

# dictionary to count symbols
symbolCount = {
    "A": 6,
    "B": 5,
    "C": 9,
    "D": 4
}

# multipliers for winnings
symbolValues = {
    "A": 4,
    "B": 3,
    "C": 5,
    "D": 2
}

# method to check winnings and determine values
def checkWinnings(columns, lines, bet, values):
    # checks for every symbol in each line
    winnings = 0
    winningLines = []
    # checks every row user bets on
    for line in range(lines):
        # symbol we check in first column of current row
        symbol = columns[0][line]
        # loop through each column to check if they all match
        for column in columns:
            # checks to see if symbol is the same
            symbolCheck = column[line]
            if symbol != symbolCheck:
                break
        # if we didn't break out for loop
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)
    return winnings, winningLines

# slot machine method that uses symbols for bets
def slotMachineSpins(rows, cols, symbols):
    # list to store symbols
    allSymbols = []
    # nested for loop that adds symbols based on numbers
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)
    columns = []
    # nested for loop that adds values attached to symbols
    for _ in range(cols):
        column = []
        # our current selection
        currSymbols = allSymbols[:]
        # loop through num of values we generate, equal to num of rows
        for _ in range(rows):
            # random value from list
            value = random.choice(allSymbols)
            # remove value to prevent repeats
            currSymbols.remove(value)
            # add to column
            column.append(value)
        # add column to total columns list
        columns.append(column)
    return columns

def printSlot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i  != len(columns) - 1:
                print(column[row], "|", end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    # loop to trigger method
    while True:
        # input takes in amount by user
        amount = input("How much would you like to deposit?: $")
        # conditional to check if input is a valid digit
        if amount.isdigit():
            # converts input from string to int
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a valid number.")
    return amount

def get_num_of_lines():
    # loop to trigger method
    while True:
        # input takes in amount by user
        lines = input("Enter the number of lines to bet on (1-" + str(maxLines) + "): " )
        # conditional to check if input is a valid digit
        if lines.isdigit():
            # converts input from string to int
            lines = int(lines)
            if lines > 0 and lines <= maxLines:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a valid number.")
    return lines

# method for bet placing
def get_bet():
     # loop to trigger method
    while True:
        # input takes in amount by user
        amount = input("How much would you like to bet on each line?: $" )
        # conditional to check if input is a valid digit
        if amount.isdigit():
            # converts input from string to int
            amount = int(amount)
            if amount > minBet and amount <= maxBet:
                break
            else:
                print(f"Amount must be between {minBet} - {maxBet}.")
        else:
            print("Please enter a valid number.")
    return amount

# game itself
def spins(bal):
    # num of lines user wants to bet on
    lines = get_num_of_lines()
    # loop that helps constraint from entering a larger bet than bal
    while True:
        bet = get_bet()
        # total amount user is betting on
        total = bet * lines

        if total > bal:
            print(f"You do not have enough to bet that amount. Your current balance is: {bal}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total bet is equal to: ${total}.")

    slots = slotMachineSpins(rows, cols, symbolCount)
    printSlot(slots)
    winnings, winningLines = checkWinnings(slots, lines, bet, symbolValues)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winningLines)
    return winnings - total

# main method to use all methods of program
def main():
    # amount user deposits into account
    bal = deposit()
    while True:
        print(f"Current balance is ${bal}.")
        spin = input("Press enter to play (q to quit).")
        if spin == "q":
            break
        bal += spins(bal)
    print(f"You left with ${bal}.")

main()