import marimo

__generated_with = "0.7.0"
app = marimo.App(width="full")


@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import re
    return mo, np, plt, re


@app.cell
def __():
    with open ('/home/il/dateng/dateng_4/coordinates.txt', 'r') as file:
        lines = file.readlines()
    n_lines = len(lines)
    n_lines
    return file, lines, n_lines


@app.cell
def __(lines, re):
    line_format = r'(\{[^\{\}]*\})'
    entire_dataset = []

    for i1, line in enumerate(lines):
        matches = re.findall(line_format, line)
        n_matches = len(matches)

        superset = []

        for j1, match in enumerate(matches):

            subset = {}

            coords = match.strip('{}').split()
            subset['x'] = [int(coord.split(',')[0]) for coord in coords]
            subset['y'] = [int(coord.split(',')[1]) for coord in coords]

            superset.append(subset)

        entire_dataset.append(superset)
    return (
        coords,
        entire_dataset,
        i1,
        j1,
        line,
        line_format,
        match,
        matches,
        n_matches,
        subset,
        superset,
    )


@app.cell
def __(entire_dataset, mo):
    superset_selector = mo.ui.slider(1, len(entire_dataset), label='select superset')
    superset_selector
    return superset_selector,


@app.cell
def __(entire_dataset, mo, superset_selector):
    superset_idx = superset_selector.value - 1
    subsets_in_superset = len(entire_dataset[superset_idx])
    subset_selector = mo.ui.slider(1, subsets_in_superset, label = 'Select subset')
    subset_selector
    return subset_selector, subsets_in_superset, superset_idx


@app.cell
def __(entire_dataset, plt, subset_selector, superset_idx):
    subset_idx = subset_selector.value - 1
    x = entire_dataset[superset_idx][(subset_idx)]['x']
    y = entire_dataset[superset_idx][(subset_idx)]['y']
    plt.scatter(x,y)
    plt.show()
    return subset_idx, x, y


@app.cell
def __(entire_dataset, plt, superset_idx):
    superset_single = entire_dataset[superset_idx]
    for p, subset_this_super in enumerate(superset_single):
        plt.scatter(subset_this_super['x'], subset_this_super['y'])
    plt.show()
    return p, subset_this_super, superset_single


@app.cell
def __(entire_dataset, plt):
    from matplotlib.patches import Rectangle
    plt.figure(figsize=(30,5))
    def give_bb(X , Y, margin = 0.05):
        x_min = min(X)
        x_max = max(X)
        y_min = min(Y)
        y_max = max(Y)

        x_length = (x_max - x_min)*(1+margin*2)
        y_length = (y_max - y_min)*(1+margin*2)

        x_anchor = x_min - margin * x_length
        y_anchor = y_min - margin * y_length

        return x_anchor, y_anchor, x_length, y_length

    import matplotlib
    cmap = matplotlib.cm.get_cmap('tab20c')
    colors = [cmap(i3) for i3 in range(20)]

    for i2, superset2 in enumerate(entire_dataset):
        super_x = []
        super_y = []
        colorgroup = i2%5
        for j2, subset2 in enumerate(superset2):
            sub_x = subset2['x'] 
            sub_y = subset2['y']
            
            subset_color_idx = colorgroup*4 + j2 +1
            subset_color = colors[subset_color_idx]
            plt.scatter(sub_x, sub_y, color=subset_color)

            x_anchor, y_anchor, x_length, y_length = give_bb(sub_x, sub_y)

            rectangle = Rectangle((x_anchor, y_anchor), x_length, y_length, edgecolor=subset_color, facecolor='none')
            plt.gca().add_patch(rectangle)
            
            super_x.extend(sub_x)
            super_y.extend(sub_y)

        superset_color_idx = colorgroup*4
        superset_color = colors[superset_color_idx]
        x_anchor, y_anchor, x_length, y_length = give_bb(super_x, super_y, margin = 0.15)

        rectangle = Rectangle((x_anchor, y_anchor), x_length, y_length, edgecolor=superset_color, facecolor='none')
        plt.gca().add_patch(rectangle)
        

    plt.show()

    return (
        Rectangle,
        cmap,
        colorgroup,
        colors,
        give_bb,
        i2,
        j2,
        matplotlib,
        rectangle,
        sub_x,
        sub_y,
        subset2,
        subset_color,
        subset_color_idx,
        super_x,
        super_y,
        superset2,
        superset_color,
        superset_color_idx,
        x_anchor,
        x_length,
        y_anchor,
        y_length,
    )


if __name__ == "__main__":
    app.run()
