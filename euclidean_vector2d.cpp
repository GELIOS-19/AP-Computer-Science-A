#include "Board.h"

namespace core::models {

Board::Board()
  : m_SideLength(3) {
  for (int32_t idx = 0; idx < 9; idx++)
    m_BoardSquares.push_back(new BoardSquare(idx, false, nullptr));
}

Board::Board(const uint16_t side_length)
  : m_SideLength(side_length) {
  for (int32_t idx = 0; idx < pow(m_SideLength, 2); idx++)
    m_BoardSquares.push_back(new BoardSquare(idx, false, nullptr));
}

Board::~Board() {
  for (auto it = m_BoardSquares.begin(); it != m_BoardSquares.end(); ++it) {
    delete *it;
    it = m_BoardSquares.erase(it);
  }
}

uint16_t Board::GetSideLength() const {
  return m_SideLength;
}

std::vector<BoardSquare *> Board::GetBoardSquares() const {
  return m_BoardSquares;
}

std::string Board::JSONString() const {
  std::stringstream string_stream;

  string_stream << "{"
      "\"side_length\":" << m_SideLength << ","
      "\"board_squares\": [";

  for (const auto &board_square : m_BoardSquares)
    string_stream << board_square->JSONString() << ",";

  string_stream << "],}";

  return string_stream.str();
}

std::vector<std::vector<uint16_t>> Board::GenerateWinIndices_() const {
  // get list of lists of horizontal indices
  std::vector<std::vector<uint16_t>> horiz_ll; // represents list of lists of horizontal indices
  horiz_ll.reserve(m_SideLength);
  std::vector<uint16_t> horiz_l; // represents list of horizontal indices
  for (uint16_t idx = 0; idx < pow(m_SideLength, 2); idx++) {
    horiz_l.push_back(idx);
    if (horiz_l.size() == m_SideLength) {
      horiz_ll.push_back(horiz_l);
      horiz_l.clear();
    }
  }

  // get list of lists of vertical indices
  std::vector<std::vector<uint16_t>> vert_ll; // represents list of lists of vertical indices
  vert_ll.reserve(m_SideLength);
  std::vector<uint16_t> vert_l; // represents list of vertical indices
  for (uint16_t idx = 0; idx < m_SideLength; idx++)
    for (const auto &horiz_l_temp : horiz_ll) {
      vert_l.push_back(horiz_l_temp[idx]);
      if (vert_l.size() == m_SideLength) {
        vert_ll.push_back(vert_l);
        vert_l.clear();
      }
    }

  // get list of lists of diagonal indices
  std::vector<std::vector<uint16_t>> diag_ll; // represents list of lists of diagonal indices
  diag_ll.reserve(m_SideLength);
  std::vector<uint16_t> diag_l; // represents list of diagonal indices
  for (uint64_t idx = 0; idx < horiz_ll.size(); idx++) {
    auto &horiz_l_temp = horiz_ll[idx];
    diag_l.push_back(horiz_l_temp[idx]);
  }
  diag_ll.push_back(diag_l);
  diag_l.clear();
  for (uint64_t idx = 0; idx < horiz_ll.size(); idx++) {
    auto &horiz_l_temp = horiz_ll[idx];
    diag_l.push_back(horiz_l_temp[horiz_l.size() - (idx + 1)]);
  }
  diag_ll.push_back(diag_l);

  // add all the lists of indices to the winning indices list
  std::vector<std::vector<uint16_t>> win_ll; // represents list of lists of all indices
  win_ll.reserve(horiz_ll.size() + vert_ll.size() + diag_ll.size());
  for (auto &horiz_l_temp : horiz_ll)
    win_ll.push_back(horiz_l_temp);
  for (auto &vert_l_temp : vert_ll)
    win_ll.push_back(vert_l_temp);
  for (auto &diag_l_temp : diag_ll)
    win_ll.push_back(diag_l_temp);

  return win_ll;
}

} // namespace core::models
