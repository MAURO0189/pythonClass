class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.hits = 0
        self.positions = []  # Lista para almacenar las posiciones ocupadas por el barco

    def place_ship(self, start_row, start_col, direction, board):
        positions = []
        if direction == "H":
            if start_col + self.size > len(board[0]):  # Corrección en el límite
                return False
            for i in range(self.size):
                if board[start_row][start_col + i] != " ":
                    return False
                positions.append((start_row, start_col + i))
        elif direction == "V":
            if start_row + self.size > len(board):  # Corrección en el límite
                return False
            for i in range(self.size):
                if board[start_row + i][start_col] != " ":
                    return False
                positions.append((start_row + i, start_col))
        else:
            return False

        for pos in positions:
            board[pos[0]][pos[1]] = self.name[0]  # Marcar la posición en el tablero
        self.positions = positions
        return True
    
    def hit(self):
        self.hits += 1
        return self.hits == self.size


class Destroyer(Ship):
    def __init__(self):
        super().__init__("Destroyer", 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine", 3)

class Battleship(Ship):
    def __init__(self):
        super().__init__("Battleship", 4)


class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.hits = [[" " for _ in range(10)] for _ in range(10)]

    def print_board(self, board):
        for row in board:
            print(" ".join(row))
        print()

    def place_ships(self):
        ships = [Destroyer(), Submarine(), Battleship()]
        for ship in ships:
            while True:
                print(f"{self.name}, coloca tu {ship.name} de tamaño {ship.size}.")
                self.print_board(self.board)
                try:
                    start_row = int(input("Fila inicial (0-9): "))
                    start_col = int(input("Columna inicial (0-9): "))
                    direction = input("Dirección (H para horizontal, V para vertical): ").upper()
                    if ship.place_ship(start_row, start_col, direction, self.board):
                        self.ships.append(ship)
                        break
                    else:
                        print("Posición inválida. Intenta de nuevo.")
                except ValueError:
                    print("Entrada no válida. Intenta de nuevo.")

    def attack(self, opponent):
        while True:
            print(f"{self.name}, es tu turno de atacar.")
            try:
                row = int(input("Fila (0-9): "))
                col = int(input("Columna (0-9): "))

                if 0 <= row < 10 and 0 <= col < 10:
                    if opponent.board[row][col] == ' ':
                        print("Agua.")
                        self.hits[row][col] = 'A'
                        opponent.board[row][col] = 'A'
                        break
                    elif opponent.board[row][col] not in ('A', 'T'):
                        print("¡Impacto!")
                        self.hits[row][col] = 'T'
                        for ship in opponent.ships:
                            if (row, col) in ship.positions:
                                if ship.hit():
                                    print(f"¡Hundiste el {ship.name}!")
                                break
                        opponent.board[row][col] = 'T'
                        break
                    else:
                        print("Ya atacaste aquí. Intenta de nuevo.")
                else:
                    print("Posición no válida. Intenta de nuevo.")
            except ValueError:
                print("Entrada no válida. Intenta de nuevo.")

    def all_ships_sunk(self):
        return all(ship.hits == ship.size for ship in self.ships)


class BattleshipGame:
    def __init__(self):
        self.player1 = Player("Jugador 1")
        self.player2 = Player("Jugador 2")

    def play(self):
        print("Bienvenido al juego de Batalla Naval.")
        print("Jugador 1 coloca sus barcos.")
        self.player1.place_ships()
        print("Jugador 2 coloca sus barcos.")
        self.player2.place_ships()

        current_player = self.player1
        opponent = self.player2

        while True:
            current_player.attack(opponent)
            if opponent.all_ships_sunk():
                print(f"¡{current_player.name} ha ganado el juego!")
                break
            current_player, opponent = opponent, current_player


# Iniciar el juego
game = BattleshipGame()
game.play()
             
            




                                    
