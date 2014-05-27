import numpy as np
from bokeh.plotting import *
from bokeh.objects import Range1d


def polar(theta1, r1, theta2, r2):
    max_radius = max([max(r1), max(r2)])
    gap_plots = 0.2/2.
    color_grid = "gray"
    color_angle_labels = "gray"
    color_radial_labels = "gray"
    right_plot_title = "TM"
    left_plot_title = "TE"

    # Coordinates in cartesian coordinates normalized for r1
    x1 = r1 * np.cos(angles) / max_radius + gap_plots
    y1 = r1 * np.sin(angles) / max_radius

    # Coordinates in cartesian coordinates normalized for r2
    x2 = -r2 * np.cos(angles) / max_radius - gap_plots
    y2 = r2 * np.sin(angles) / max_radius

    # Create the figure and hold it
    figure(plot_width=500,
           plot_height=300)
    hold()

    # Plot the line and set ranges and eliminate the cartesian grid
    plot = line(x1, y1, color="teal", line_width=2, title=None)
    plot.x_range = Range1d(start=-0.2 - 1, end=1+0.2)
    plot.y_range = Range1d(start=0-0.1, end=1+0.148)

    line(x2, y2, color="teal", line_width=2, title=None)

    plot.outline_line_color = None
    grid().grid_line_color = None

    # Draw the radial coordinates grid for right plot
    radius = [0.2, 0.4, 0.6, 0.8]
    zeros = np.zeros(4)
    plot = annular_wedge(zeros+gap_plots, zeros, zeros, radius, 0, np.pi/2,
                         fill_color=None, line_color=color_grid,
                         line_dash="4 4", line_widht=0.5)
    plot = annular_wedge([gap_plots], [0.0], [0.], [1.005], 0, np.pi/2,
                         fill_color=None, line_color="#37435E",
                         line_widht=1.5)

    # Draw the radial coordinates grid for left plot
    radius = [0.2, 0.4, 0.6, 0.8]
    zeros = np.zeros(4)
    plot = annular_wedge(zeros-gap_plots, zeros, zeros, radius, np.pi/2, np.pi,
                         fill_color=None, line_color=color_grid,
                         line_dash="4 4", line_widht=0.5)
    plot = annular_wedge([-gap_plots], [0.0], [0.], [1.005], np.pi/2, np.pi,
                         fill_color=None, line_color="#37435E",
                         line_widht=1.5)

    #Draw angular grid right plot
    l_spoke = np.ones(3) * 175
    x_spoke = np.ones(3) * gap_plots
    y_spoke = np.zeros(3)
    n_spokes = 4
    angles_spokes = np.linspace(min_angle, max_angle, n_spokes)
    ray(x_spoke, y_spoke, l_spoke,
        angles_spokes[1:-1],
        line_color=color_grid,
        line_width=0.5,
        line_dash="4 4")

    #Draw angular grid left plot
    l_spoke = np.ones(3) * 175
    x_spoke = -np.ones(3) * gap_plots
    y_spoke = np.zeros(3)
    n_spokes = 4
    angles_spokes = np.linspace(min_angle, max_angle, n_spokes)
    ray(x_spoke, y_spoke, l_spoke,
        angles_spokes[1:-1]+np.pi/2.,
        line_color=color_grid,
        line_width=0.5,
        line_dash="4 4")

    # Angle Labels Right Plot
    x_labels = 1.01 * np.cos(angles_spokes) + gap_plots
    y_labels = 1.01 * np.sin(angles_spokes)

    text(x_labels, y_labels, ['90', '60', '30', '0'],
         angle=-np.pi/2+angles_spokes,
         text_font_size="12pt", text_align="center", text_baseline="bottom",
         text_color=color_angle_labels)

    # Angle Labels Right Plot
    x_labels = -(1.01 * np.cos(angles_spokes) + gap_plots)
    y_labels = 1.01 * np.sin(angles_spokes)

    text(x_labels, y_labels, ['90', '60', '30', '0'],
         angle=+np.pi/2-angles_spokes,
         text_font_size="12pt", text_align="center", text_baseline="bottom",
         text_color=color_angle_labels)

    # Radial Labels  plot
    x_labels = np.ones(6) * 0
    y_labels = np.linspace(0, 1, 6)
    number_labels = ["%.1f" % s for s in y_labels * max_radius]
    text(x_labels, y_labels, number_labels,
         angle=np.zeros(6),
         text_font_size="9pt", text_align="center", text_baseline="middle",
         text_color=color_radial_labels)
    # ray([-0.07], [0], [207], np.pi/2, line_color="gray")
    # for lab in range(6):
    #     ray([-0.07], [y_labels[lab]], [7], [0], line_color="gray")

    # Lable the plots
    text([1 + gap_plots-0.1], [1-0.1], right_plot_title, angle=0.,
         text_color="#37435E",
         text_align="center")
    text([-1 - gap_plots+0.1], [1-0.1], left_plot_title, angle=0.,
         text_color="#37435E",
         text_align="center")
    # Final touches
    yaxis().bounds = (0, 0)
    xaxis().bounds = (0, 0)

if __name__ == '__main__':
    output_file("polar.html")
    min_angle = 0
    max_angle = np.pi/2
    angles = np.linspace(min_angle, max_angle, 180)
    r = 2*np.cos(2*angles)**2
    polar(angles, r, angles, r)

    show()
