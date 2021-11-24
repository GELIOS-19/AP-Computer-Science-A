#pragma once

#include <map>

class euclidean_vector2d
{
public:
  // Even numbers represent negative directions
  enum directions { north = 1, south = 2, east = 3, west = 4 };

  struct vector_component
  {
    float magnitude;
    directions direction;
  };

  float magnitude;
  float rotation_angle;
  directions axis_direction;
  directions rotation_direction;

  euclidean_vector2d(
    float magnitude,
    float angle_of_rotation,
    directions direction_of_axis,
    directions direction_of_angle_of_rotation);
  std::map<const char*, vector_component> find_vector_components() const;
  euclidean_vector2d operator +(const euclidean_vector2d& additional_vector) const;

  // Converts a valid 'std::string' into its 'directions' counterpart
  static directions convert_string_to_directions(std::string direction_string)
  {
    if (direction_string == "north")
      return north;
    if (direction_string == "south")
      return south;
    if (direction_string == "east")
      return east;
    if (direction_string == "west")
      return west;

    return directions{};
  }

  // Converts 'directions' to 'std::string'
  static std::string convert_directions_to_string(const directions direction)
  {
    if (direction == north)
      return "north";
    if (direction == south)
      return "south";
    if (direction == east)
      return "east";
    if (direction == west)
      return "west";
    return "";
  }

  // Method adds compatibility with 'std::cout'
  friend std::ostream& operator <<(std::ostream& stream, const directions direction)
  {
    const std::string direction_string = convert_directions_to_string(direction);
    stream << direction_string;
    return stream;
  }
};
