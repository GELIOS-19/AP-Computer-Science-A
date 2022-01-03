//
// Created by Slend on 1/2/2022.
//

#include "Board.h"

namespace core::models {

  Board::Board() : sideLength_(3), totalSquares_(9) {
    // initialize board squares
    for (uint16_t index = 0; index < this->totalSquares_; index++) {
      this->boardSquares_[index] = new BoardSquare(index, false, nullptr);
    }

    // initialize winning indices sets for 3x3 board
    this->winningIndicesSets_ = {
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},  // horizontal indices lists
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},  // vertical indices lists
        {0, 4, 8}, {2, 4, 6}};            // diagonal indices lists
  }

  Board::Board(uint16_t sideLength)
      : sideLength_(sideLength),
        totalSquares_(static_cast<uint16_t>(pow(this->sideLength_, 2))) {
    // initialize board squares
    for (uint16_t index = 0; index < this->totalSquares_; index++) {
      this->boardSquares_[index] = new BoardSquare(index, false, nullptr);
    }

    // initialize winning indices sets
    std::vector<std::vector<uint16_t>>
        hSets;  // represents list of lists of horizontal indices
    std::vector<std::vector<uint16_t>>
        vSets;  // represents list of lists of vertical indices
    std::vector<std::vector<uint16_t>>
        dSets;  // represents list of lists of diagonal indices

    // get all lists of horizontal indices
    std::vector<uint16_t> hSet;

    for (uint16_t index = 0; index < this->totalSquares_; index++) {
      hSet.push_back(index);
      if (hSet.size() == this->sideLength_) {
        hSets.push_back(hSet);
        hSet.clear();
      }
    }

    // get all lists of vertical indices
    std::vector<uint16_t> vSet;

    for (uint16_t index = 0; index < this->sideLength_; index++) {
      for (const auto &hSet_ : hSets) {
        vSet.push_back(hSet_[index]);
        if (vSet.size() == this->sideLength_) {
          vSets.push_back(vSet);
          vSet.clear();
        }
      }
    }

    // get all lists of diagonal indices
    std::vector<uint16_t> dSet;

    for (uint64_t index = 0; index < hSets.size(); index++) {
      auto &hSet_ = hSets[index];
      dSet.push_back(hSet_[index]);
    }

    dSets.push_back(dSet);
    dSet.clear();

    for (uint64_t index = 0; index < hSets.size(); index++) {
      auto &hSet_ = hSets[index];
      dSet.push_back(hSet_[hSet.size() - (index + 1)]);
    }

    dSets.push_back(dSet);

    // add all the lists of indices to the winning indices sets
    for (auto &hSet_ : hSets) {
      this->winningIndicesSets_.push_back(hSet_);
    }

    for (auto &vSet_ : vSets) {
      this->winningIndicesSets_.push_back(vSet_);
    }

    for (auto &dSet_ : dSets) {
      this->winningIndicesSets_.push_back(dSet_);
    }
  }

}  // namespace core::models
