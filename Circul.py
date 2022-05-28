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

ACCEL_DUE_TO_GRAV = 9.81


def main():
    # Format data
    y = np.array(
        [(m / 1000) * ACCEL_DUE_TO_GRAV for m in mass_vs_spring_length.keys()]
    )
    x = np.array(
        [
            (l / 100) - (natural_spring_length / 100)
            for l in mass_vs_spring_length.values()
        ]
    )

    # create the plot
    plot = plt.figure(dpi=1200, figsize=(10, 5))
    subplot = plot.add_subplot(1, 1, 1)
    subplot.scatter(x, y)

    # label the axes
    subplot.set_xlabel("Displacement (m)")
    subplot.set_ylabel("Force (N)")
    subplot.set_title("Force vs. Displacement")

    # label each point on the plot with its coordinates
    anns = []
    for x_coord, y_coord in zip(x, y):
        anns.append(
            subplot.annotate(
                f"({x_coord:.2} m, {y_coord:.2} N)",
                xy=(x_coord + (3 / 1000), y_coord - (25 / 1000))
            )
        )
    # save without trend line
    plt.savefig("without_trend_line.png")

    # remove annotations
    for ann in anns:
        ann.remove()

    # create best fit line
    m, b = np.polyfit(x, y, 1)
    print(m, b)
    subplot.plot(x, m * x + b, '-', color='red')
    # save with trend line
    plt.savefig("with_trend_line.png")


if __name__ == '__main__':
    main()
