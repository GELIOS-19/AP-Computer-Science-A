#include <iostream>
#include <vector>
#include <map>

#define PI 3.141592

class c_direction
{

public:
	
	static const c_direction null;
	static const c_direction north;
	static const c_direction south;
	static const c_direction east;
	static const c_direction west;

	int x_prefix;
	int y_prefix;

	c_direction(int x_prefix, int y_prefix)
	{
		this->x_prefix = x_prefix;
		this->y_prefix = y_prefix;
	}

	bool operator ==(const c_direction& subject) const
	{
		return x_prefix == subject.x_prefix && y_prefix == subject.y_prefix;
	}
};

c_direction const c_direction::null = c_direction(0, 0);
c_direction const c_direction::north = c_direction(0, 1);
c_direction const c_direction::south = c_direction(0, -1);
c_direction const c_direction::east = c_direction(1, 0);
c_direction const c_direction::west = c_direction(-1, 0);

struct c_vector_component
{
	double magnitude;
	c_direction direction;

	double represent_as_double() const
	{
		if (direction == c_direction::north || direction == c_direction::south)
			return magnitude * direction.y_prefix;
		else if (direction == c_direction::east || direction == c_direction::west)
			return magnitude * direction.x_prefix;
		return 0;
	}

	static c_vector_component represent_as_vector_component(const c_vector_component& subject)
	{

	}
};

int main(int argc, const char* argv[])
{
	std::cout << "Hello World" << std::endl;
	return 0;
}
s
