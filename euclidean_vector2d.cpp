#include <map>
#include <vector>
#include <cmath>
#include <iostream>

#define PI 3.141592

class directions {
public:
    static const directions north;
    static const directions south;
    static const directions east;
    static const directions west;
    static const directions null;

    int x_direction_constant;
    int y_direction_constant;

    directions() {}

    directions(const int x_direction_constant, const int y_direction_constant) {
        this->x_direction_constant = x_direction_constant;
        this->y_direction_constant = y_direction_constant;
    }

    bool operator ==(const directions& direction) const {
        return x_direction_constant == direction.x_direction_constant && y_direction_constant == direction.y_direction_constant;
    }
};

directions const directions::north = directions(0, 1);
directions const directions::south = directions(0, -1);
directions const directions::east = directions(1, 0);
directions const directions::west = directions(-1, 0);
directions const directions::null = directions(0, 0);

struct vector_component {
    double magnitude;
    directions direction;

    double find_quantity() const {
        if (direction.x_direction_constant != 0)
            return magnitude * direction.x_direction_constant;
        if (direction.y_direction_constant != 0)
            return magnitude * direction.y_direction_constant;
    }

    static vector_component find_vector_component_from_quantity(const double quantity, const std::vector<directions>& ignored_directions) {
        const double magnitude = std::abs(quantity);
        auto direction = directions::null;

        if (std::count(ignored_directions.begin(), ignored_directions.end(), directions::north) || std::count(ignored_directions.begin(), ignored_directions.end(), directions::south)) {
            if (quantity > 0)
                direction = directions::east;
            else if (quantity < 0)
                direction = directions::west;
        }
        else if (std::count(ignored_directions.begin(), ignored_directions.end(), directions::east) || std::count(ignored_directions.begin(), ignored_directions.end(), directions::west)) {
            if (quantity > 0)
                direction = directions::north;
            else if (quantity < 0)
                direction = directions::south;
        }

        return vector_component{ magnitude, direction };
    }

    // Can only add two vector components on the same axis (north-south and east-west)
    vector_component operator +(const vector_component& addend) {
        const double quantity = find_quantity();
        const double addend_quantity = addend.find_quantity();

        const double resultant_quantity = quantity + addend_quantity;
        directions resultant_direction = directions::null;

        if ((direction == directions::north || direction == directions::south) && (addend.direction == directions::north || addend.direction == directions::south))
            resultant_direction = !std::signbit(resultant_quantity) ? directions::north : directions::south;
        else if ((direction == directions::north || direction == directions::south) && (addend.direction == directions::north || addend.direction == directions::south))
            resultant_direction = !std::signbit(resultant_quantity) ? directions::east : directions::west;

        magnitude = std::abs(resultant_quantity);
        direction = resultant_direction;

        return *this;
    }
};

class vector2 {
public:
    double magnitude;
    double angle;
    directions direction;
    directions angle_direction;

    vector2(const double magnitude, const double angle, const directions& direction, const directions& angle_direction) {
        this->magnitude = magnitude;
        this->angle = angle;
        this->direction = direction;
        this->angle_direction = angle_direction;
    }

    std::map<std::string, vector_component> find_vector_components() const {
        vector_component x_vector_component = {};
        vector_component y_vector_component = {};

        if (direction == directions::north || direction == directions::south) {
            x_vector_component.magnitude = magnitude * std::sin(angle * PI / 180);
            x_vector_component.direction = angle_direction;
            y_vector_component.magnitude = magnitude * std::cos(angle * PI / 180);
            y_vector_component.direction = direction;
        }
        else if (direction == directions::east || direction == directions::west) {
            x_vector_component.magnitude = magnitude * std::cos(angle * PI / 180);
            x_vector_component.direction = direction;
            y_vector_component.magnitude = magnitude * std::sin(angle * PI / 180);
            y_vector_component.direction = angle_direction;
        }

        return std::map<std::string, vector_component>{ {"x", x_vector_component}, { "y", y_vector_component }};
    }

    vector2 operator +(const vector2& addend) {
        auto vector_components = find_vector_components();
        const auto addend_vector_components = addend.find_vector_components();

        const auto resultant_vector_components = std::map<std::string, vector_component>{ {"x", vector_components["x"] + addend_vector_components.at("x")}, {"y", vector_components["y"] + addend_vector_components.at("x")} };

        magnitude = std::sqrt(std::pow(resultant_vector_components.at("x").magnitude, 2) + std::pow(resultant_vector_components.at("x").magnitude, 2));
        angle = std::atan(resultant_vector_components.at("x").magnitude / resultant_vector_components.at("y").magnitude) * 180 / PI;
        direction = resultant_vector_components.at("y").direction;
        angle_direction = resultant_vector_components.at("x").direction;

        return *this;
    }
};

int main(int argc, const char* argv[]) {
    auto vec_a = vector2(500, 70, directions::east, directions::north);
    const auto vec_b = vector2(72, 15, directions::east, directions::south);
    const auto vec_c = vec_a + vec_b;

    std::cout << vec_c.magnitude << std::endl;
    std::cout << vec_c.angle << std::endl;
    std::cout << vec_c.direction.x_direction_constant << " " << vec_c.direction.y_direction_constant << std::endl;
    std::cout << vec_c.angle_direction.x_direction_constant << " " << vec_c.angle_direction.y_direction_constant << std::endl;
}
