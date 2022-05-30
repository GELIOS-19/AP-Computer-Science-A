import matplotlib.pyplot as plt
import numpy as np

mass_vs_spring_length = {
    25: 7.6,
    50: 9.5,
    100: 13,
    150: 16.6,
    200: 19.7,
    250: 23.2,
}

natural_spring_length = 6.3

ACCELERATION_DUE_TO_GRAVITY = 9.81


def main():
    # Format data
    y_axis = np.array([(mass / 1000) * ACCELERATION_DUE_TO_GRAVITY
                       for mass in mass_vs_spring_length.keys()])
    x_axis = np.array([(spring_length / 100) - (natural_spring_length / 100)
                       for spring_length in mass_vs_spring_length.values()])

    # create the plot
    plot = plt.figure(dpi=284, figsize=(10, 5))
    subplot = plot.add_subplot(1, 1, 1)
    subplot.scatter(x_axis, y_axis)

    # label the axes
    subplot.set_title("Force vs. Displacement")
    subplot.set_xlabel("Displacement (m)")
    subplot.set_ylabel("Force (N)")

    # label each point on the plot with its coordinates
    annotations = []
    for x_coordinate, y_coordinate in zip(x_axis, y_axis):
        annotations.append(
            subplot.annotate(f"({x_coordinate:.2} m, {y_coordinate:.2} N)",
                             xy=(x_coordinate + (3 / 1000),
                                 y_coordinate - (25 / 1000))))
    # save without trend line
    plt.savefig("without_trend_line.png")

    # remove annotations
    for annotation in annotations:
        annotation.remove()

    # create best fit line
    slope, y_intercept = np.polyfit(x_axis, y_axis, 1)
    print(slope, y_intercept)
    subplot.plot(x_axis, slope * x_axis + y_intercept, '-', color='red')
    # save with trend line
    plt.savefig("with_trend_line.png")


if __name__ == '__main__':
    main()
