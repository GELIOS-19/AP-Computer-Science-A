//
// Created by Slend on 1/2/2022.
//

#include "Board.h"

namespace core::models {

Board::Board() : sideLength_(3) {
  // initialize total squares
  this->totalSquares_ = 9;

  // initialize board squares
  for (uint16_t index = 0; index < this->totalSquares_; index++)
    this->boardSquares_[index] = new BoardSquare(index, false, nullptr);

  // initialize winning indices sets
  this->winningIndicesSets_ = {{0, 1, 2},
                               {3, 4, 5},
                               {6, 7, 8},
                               {0, 3, 6},
                               {1, 4, 7},
                               {2, 5, 8},
                               {0, 4, 8},
                               {2, 4, 6}};
}

Board::Board(uint16_t sideLength) : sideLength_(sideLength) {
  // initialize total squares
  this->totalSquares_ = static_cast<uint16_t>(pow(this->sideLength_, 2));

  // initialize board squares
  for (uint16_t index = 0; index < this->totalSquares_; index++)
    this->boardSquares_[index] = new BoardSquare(index, false, nullptr);

  // initialize winning indices sets
  std::vector<std::vector<uint16_t>> horizontalIndicesSet;
  std::vector<std::vector<uint16_t>> verticalIndicesSet;
  std::vector<std::vector<uint16_t>> diagonalIndicesSet;
}

} // namespace core::models
