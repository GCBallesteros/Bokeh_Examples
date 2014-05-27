import numpy as np
from bokeh.plotting import *
from bokeh.objects import Range1d


def polar(theta, r):
    max_radius = max(r)

    # Coordinates in cartesian coordinates normalized
    x = r * np.cos(angles) / max_radius
    y = r * np.sin(angles) / max_radius

    # Create the figure and hold it
    figure(plot_width=370,
           plot_height=370)
    hold()

    # Plot the line and set ranges and eliminate the cartesian grid
    plot = line(x, y, color="teal", line_width=2, title=None)
    plot.x_range = Range1d(start=-0.3, end=1+0.1)
    plot.y_range = Range1d(start=-0.3, end=1+0.1)
    plot.outline_line_color = None
    grid().grid_line_color = None

    # Draw the radial coordinates grid
    radius = [0.2, 0.4, 0.6, 0.8]
    zeros = np.zeros(4)
    plot = annular_wedge(zeros, zeros, zeros, radius, 0, np.pi/2,
                         fill_color=None, line_color="gray",
                         line_dash="4 4", line_widht=0.5)
    plot = annular_wedge([0.0], [0.0], [0.], [1.01], 0, np.pi/2,
                         fill_color=None, line_color="#37435E",
                         line_widht=1.5)

    #Draw angular grid
    n_spokes = 4
    angles_spokes = np.linspace(min_angle, max_angle, n_spokes)
    ray([0, 0, 0], [0, 0, 0], [209, 209, 209],
        angles_spokes[1:-1],
        line_color="gray",
        line_width=0.5,
        line_dash="4 4")

    # Angle Labels
    x_labels = 1.01 * np.cos(angles_spokes)
    y_labels = 1.01 * np.sin(angles_spokes)

    text(x_labels, y_labels, ['90', '60', '30', '0'],
         angle=-np.pi/2+angles_spokes,
         text_font_size="12pt", text_align="center", text_baseline="bottom",
         text_color="gray")

    # Radial Labels
    x_labels = np.ones(6) * -0.04
    y_labels = np.linspace(0, 1, 6)
    number_labels = ["%.1f" % s for s in y_labels * max_radius]
    text(x_labels, y_labels, number_labels,
         angle=np.zeros(6),
         text_font_size="9pt", text_align="right", text_baseline="middle",
         text_color="gray")
    # ray([-0.07], [0], [207], np.pi/2, line_color="gray")
    # for lab in range(6):
    #     ray([-0.07], [y_labels[lab]], [7], [0], line_color="gray")

    # Final touches
    yaxis().bounds = (0, 0)
    xaxis().bounds = (0, 0)

if __name__ == '__main__':
    output_file("polar.html")
    min_angle = 0
    max_angle = np.pi/2
    angles = np.linspace(min_angle, max_angle, 180)
    r = 2*np.cos(2*angles)**2
    polar(angles, r)

    show()
