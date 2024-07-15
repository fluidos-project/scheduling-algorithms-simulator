
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def get_text_color(background_color):
    r, g, b, _ = background_color
    luminosity = 0.299 * r + 0.587 * g + 0.114 * b
    return 'black' if (luminosity > 0.5) else 'white'


def highlight_selected_cell(ax, nodes, timeslots, table, selected_node_id, selected_timeslot_id):
    """Mettre en valeur la cellule sélectionnée dans le tableau."""
    for i, node in enumerate(nodes):
        for j, timeslot in enumerate(timeslots):
            if node.id == selected_node_id and timeslot.id == selected_timeslot_id:
                cell = table[i + 1, j]
                cell.set_edgecolor('blue')
                cell.set_linewidth(5)


def showPlot(nodes, timeslots, totalEmissionPerNode, selectedNode, selectedTimeslot):
    cmap = mcolors.LinearSegmentedColormap.from_list('green_yellow_red_black',
                                                     ['green', 'yellow', 'orange', 'brown', 'black'], N=256)

    fig_width = max(8, len(timeslots) * 2)
    fig_height = max(6, len(nodes) * 2)

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Masquer les axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)

    table = ax.table(cellText=totalEmissionPerNode,
                     rowLabels=[f'Node {node.id} \n embodied: {node.embodiedCarbon} gCo2' for node in nodes],
                     colLabels=[f'TS {timeslot.id}' for timeslot in timeslots],
                     cellLoc='center', loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    cell_width = 1
    cell_height = 5
    table.scale(cell_width, cell_height)

    for i in range(len(nodes)):
        for j in range(len(timeslots)):
            value = totalEmissionPerNode[i, j]
            if value != np.nan:
                normalized_value = (value - 0) / (2000) # 2000 looks like the maximum possible value
                color = cmap(normalized_value)
                cell = table[i + 1, j]  # +1 because first line is headers
                cell.set_facecolor(color)
                cell.set_text_props(color=get_text_color(color))

    highlight_selected_cell(ax, nodes, timeslots, table, selectedNode, selectedTimeslot)
    plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8)

    plt.title('Total carbon emission of the pod to schedule per node and timeslot (gCO2)')
    plt.show()
