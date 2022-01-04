//
// Created by Slend on 1/2/2022.
//
#include "Board.h"

namespace core::models
{
	std::vector<std::vector < uint16_t>> Board::initWinningIndicesSets_(uint16_t sideLength, uint16_t totalSquares)
	{
		std::vector<std::vector < uint16_t>> hSets;	// represents list of lists of horizontal indices
		hSets.reserve(sideLength);
		
		// get all lists of horizontal indices
		std::vector<uint16_t> hSet;
		
		for (uint16_t index = 0; index < totalSquares; index++)
		{
			hSet.push_back(index);
			if (hSet.size() == sideLength)
			{
				hSets.push_back(hSet);
				hSet.clear();
			}
		}

		std::vector<std::vector < uint16_t>> vSets;	// represents list of lists of vertical indices
		vSets.reserve(sideLength);
		
		// get all lists of vertical indices
		std::vector<uint16_t> vSet;
		
		for (uint16_t index = 0; index < sideLength; index++)
			for (const auto &hSetTemp: hSets)
			{
				vSet.push_back(hSetTemp[index]);
				if (vSet.size() == sideLength)
				{
					vSets.push_back(vSet);
					vSet.clear();
				}
			}

		std::vector<std::vector < uint16_t>> dSets;	// represents list of lists of diagonal indices
		dSets.reserve(sideLength);
		
		// get all lists of diagonal indices
		std::vector<uint16_t> dSet;
		
		for (uint64_t index = 0; index < hSets.size(); index++)
		{
			auto &hSetTemp = hSets[index];
			dSet.push_back(hSetTemp[index]);
		}

		dSets.push_back(dSet);
		dSet.clear();

		for (uint64_t index = 0; index < hSets.size(); index++)
		{
			auto &hSetTemp = hSets[index];
			dSet.push_back(hSetTemp[hSet.size() - (index + 1)]);
		}

		dSets.push_back(dSet);

		std::vector<std::vector < uint16_t>> wSets;	// represents list of lists of all indices
		wSets.reserve(hSets.size() + vSets.size() + dSets.size());
		
		// add all the lists of indices to the winning indices sets
		for (auto &hSetTemp : hSets) wSets.push_back(hSetTemp);
		for (auto &vSetTemp : vSets) wSets.push_back(vSetTemp);
		for (auto &dSetTemp : dSets) wSets.push_back(dSetTemp);

		return wSets;
	}

	Board::Board(): sideLength_(3), totalSquares_(9)
	{
		this->boardSquares_.reserve(9);
		this->boardSquares_[0] = new BoardSquare(0, false, nullptr);
		this->boardSquares_[1] = new BoardSquare(1, false, nullptr);
		this->boardSquares_[2] = new BoardSquare(2, false, nullptr);
		this->boardSquares_[3] = new BoardSquare(3, false, nullptr);
		this->boardSquares_[4] = new BoardSquare(4, false, nullptr);
		this->boardSquares_[5] = new BoardSquare(5, false, nullptr);
		this->boardSquares_[6] = new BoardSquare(6, false, nullptr);
		this->boardSquares_[7] = new BoardSquare(7, false, nullptr);
		this->boardSquares_[8] = new BoardSquare(8, false, nullptr);
		this->winningIndicesSets_ = {
		    { 0, 1, 2 },
			{ 3, 4, 5 },
			{ 6, 7, 8 },
			//
			{ 0, 3, 6 },
			{ 1, 4, 7 },
			{ 2, 5, 8 },
			//
			{ 0, 4, 8 },
			{ 2, 4, 6 }
		};
	}

	Board::Board(uint16_t sideLength) : sideLength_(sideLength), totalSquares_(static_cast<uint16_t> (pow(this->sideLength_, 2)))
	{
		for (uint16_t index = 0; index < this->totalSquares_; index++)
			this->boardSquares_[index] = new BoardSquare(index, false, nullptr);
		this->winningIndicesSets_ = initWinningIndicesSets_(this->sideLength_, this->totalSquares_);
	}

	Board::~Board()
	{
		std::vector<BoardSquare*>::iterator iter;
		for (iter = this->boardSquares_.begin(); iter != this->boardSquares_.end(); iter++)
		{
			delete * iter;
			iter = this->boardSquares_.erase(iter);
		}
	}

	std::vector<BoardSquare*> Board::getBoardSquares() const
	{
		return this->boardSquares_;
	}

	std::vector<std::vector < uint16_t>> Board::getWinningIndicesSets() const
	{
		return this->winningIndicesSets_;
	}

	uint16_t Board::getSideLength() const
	{
		return this->sideLength_;
	}

	uint16_t Board::getTotalSquares() const
	{
		return this->totalSquares_;
	}

	std::string Board::toJSONString() const
	{
		std::stringstream ss;
		ss << "{"
		"\"sideLength\": " << this->sideLength_ << ","
		"\"totalSquares\": " << this->totalSquares_ << ","
		"\"boardSquares\": {";
		for (const BoardSquare *bs: boardSquares_)
			ss << "\"BoardSquare@index=" << bs->getIndex() << "\": " << bs->toJSONString() << ",";
		ss << "}";
		return ss.str();
	}
}	// namespace core::models
