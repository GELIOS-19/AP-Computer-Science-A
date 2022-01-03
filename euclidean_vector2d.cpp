//
// Created by Slend on 1/2/2022.
//

#include "Board.h"

namespace core::models {

Board::Board()
	: sideLength_(3), totalSquares_(9) {
	// initialize board squares
	for (uint16_t index = 0; index < this->totalSquares_; index++) {
		this->boardSquares_[index] = new BoardSquare(index, false, nullptr);
	}

	// initialize winning indices sets for 3x3 board
	this->winningIndicesSets_ = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, // horizontal indices lists
								 {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, // vertical indices lists
								 {0, 4, 8}, {2, 4, 6}}; // diagonal indices lists
}

Board::Board(uint16_t sideLength)
	: sideLength_(sideLength), totalSquares_(static_cast<uint16_t>(pow(this->sideLength_, 2))) {

	// initialize board squares
	for (uint16_t index = 0; index < this->totalSquares_; index++) {
		this->boardSquares_[index] = new BoardSquare(index, false, nullptr);
	}

	// initialize winning indices sets
	std::vector<std::vector<uint16_t>> horizontalIndicesSets; // represents list of lists of horizontal indices
	std::vector<std::vector<uint16_t>> verticalIndicesSets; // represents list of lists of vertical indices
	std::vector<std::vector<uint16_t>> diagonalIndicesSets; // represents list of lists of diagonal indices

	// reserve memory
	horizontalIndicesSets.reserve(this->sideLength_);
	verticalIndicesSets.reserve(this->sideLength_);
	diagonalIndicesSets.reserve(this->sideLength_);

	// get all lists of horizontal indices
	std::vector<uint16_t> horizontalIndicesSet;

	for (uint16_t index = 0; index < this->totalSquares_; index++) {
		horizontalIndicesSet.push_back(index);
		if (horizontalIndicesSet.size() == this->sideLength_) {
			horizontalIndicesSets.push_back(horizontalIndicesSet);
			horizontalIndicesSet.clear();
		}
	}

	// get all lists of vertical indices
	std::vector<uint16_t> verticalIndicesSet;

	for (uint16_t index = 0; index < this->sideLength_; index++) {
		for (const auto &horizontalIndicesSet_ : horizontalIndicesSets) {
			verticalIndicesSet.push_back(horizontalIndicesSet_[index]);
			if (verticalIndicesSet.size() == this->sideLength_) {
				verticalIndicesSets.push_back(verticalIndicesSet);
				verticalIndicesSet.clear();
			}
		}
	}

	// get all lists of diagonal indices
	std::vector<uint16_t> diagonalIndicesSet;

	for (uint64_t index = 0; index < horizontalIndicesSets.size(); index++) {
		auto &horizontalIndicesSet_ = horizontalIndicesSets[index];
		diagonalIndicesSet.push_back(horizontalIndicesSet_[index]);
	}

	diagonalIndicesSets.push_back(diagonalIndicesSet);
	diagonalIndicesSet.clear();

	for (uint64_t index = 0; index < horizontalIndicesSets.size(); index++) {
		auto &horizontalIndicesSet_ = horizontalIndicesSets[index];
		diagonalIndicesSet.push_back(horizontalIndicesSet_[horizontalIndicesSet.size() - (index + 1)]);
	}

	diagonalIndicesSets.push_back(diagonalIndicesSet);

	// add all the lists of indices to the winning indices sets
	for (auto &horizontalIndicesSet_ : horizontalIndicesSets) {
		this->winningIndicesSets_.push_back(horizontalIndicesSet_);
	}

	for (auto &verticalIndicesSet_ : verticalIndicesSets) {
		this->winningIndicesSets_.push_back(verticalIndicesSet_);
	}

	for (auto &diagonalIndicesSet_ : diagonalIndicesSets) {
		this->winningIndicesSets_.push_back(diagonalIndicesSet_);
	}
}

Board::~Board() {
	std::vector<BoardSquare *>::iterator iter;
	for (iter = this->boardSquares_.begin(); iter != this->boardSquares_.end(); iter++) {
		delete *iter;
		iter = this->boardSquares_.erase(iter);
	}
}

std::vector<BoardSquare *> Board::getBoardSquares() const {
	return this->boardSquares_;
}

std::vector<std::vector<uint16_t>> Board::getWinningIndicesSets() const {
	return this->winningIndicesSets_;
}

} // namespace core::models
