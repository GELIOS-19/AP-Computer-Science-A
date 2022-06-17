class Player:

  def __init__(self, symbol):
    self.symbol = symbol

  @staticmethod
  def get_opponent_symbol(player):
    if player.symbol == "X":
      return "O"
    elif player.symbol == "O":
      return "X"
    else:
      return None

  @property
  def state(self):
    return {"symbol": self.symbol}


class Cell:

  def __init__(self, number, player=None):
    self.number = number
    self.player = player
    self.__is_valid = True

  def invalidate(self):
    self.__is_valid = False

  def is_available(self):
    return self.player is None and self.__is_valid

  @property
  def state(self):
    return {
        "number": self.number,
        "player": self.player.state if self.player else None,
        "is_available": self.is_available(),
    }


class Board:

  def __init__(self, number, side_length=3):
    self.number = number
    self.side_length = side_length
    self.cells = [Cell(i) for i in range(side_length**2)]

  def __str__(self):
    string = ""
    for cell in self.cells:
      string += (
          "[" +
          (cell.player.symbol if cell.contains_player() else str(cell.number)) +
          "]")
      if (cell.number + 1) % self.side_length == 0:
        string += "\n"
    return string

  def contains_winning_pattern(self, player):
    pass

  @property
  def state(self):
    return {
        "number": self.number,
        "side_length": self.side_length,
        "cells": [cell.state for cell in self.cells],
    }


class Game:

  def __init__(self, number_of_boards=3):
    self.__boards = [
        Board(i, number_of_boards) for i in range(number_of_boards**2)
    ]
    self.__players = (Player("X"), Player("O"))

    self.number_of_boards = number_of_boards
    self.playable_boards = [{board.number: board} for board in self.__boards]
    self.playable_boards_keys = list(self.playable_boards.keys())

    # By default, the first player is X and the second player is O
    self.__current_player = self.__players[0]
    self.__opponent_player = self.__players[1]

  def __str__(self):
    string = ""
    for board in self.boards:
      string += str(board.number) + "\n" + board.__str__() + "\n"
    return string

  def __place_player_mark(self, board_number, cell_number, player):
    board = self.playable_boards[board_number]
    cell = board.cells[cell_number]
    cell.player = player
    if board.contains_winning_pattern(player):
      for board in self.playable_boards.values():
        board.cells[cell_number].invalidate()
  
  def __reset_playable_boards(self):
    pass

  def make_turn(self, board_number, cell_number):
    precondition_1 = board_number in self.playable_boards.keys()
    precondition_2 = (False if not precondition_1 else 0 <= cell_number <=
                      self.playable_boards[board_number].side_length**2)
    precondition_3 = (
        False if not precondition_1 else
        self.playable_boards[board_number].cells[cell_number].is_available())

    if not precondition_1 and not precondition_2 and not precondition_3:
      return False

    self.__place_player_mark(self, board_number, cell_number,
                            self.__current_player)
    self.__reset_playable_boards()

    pass

  @property
  def state(self):
    return {
        "number_of_boards": self.number_of_boards,
        "player_one": self.player_one.state,
        "player_two": self.player_two.state,
        "playable_boards": [board.state for board in self.playable_boards],
    }


if __name__ == "__main__":
  game = Game()
  print(game.state)
