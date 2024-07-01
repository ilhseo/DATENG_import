import marimo

__generated_with = "0.6.22"
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

    for i, line in enumerate(lines):
        matches = re.findall(line_format, line)
        n_matches = len(matches)

        superset = []

        for j, match in enumerate(matches):

            subset = {}

            coords = match.strip('{}').split()
            subset['x'] = [int(coord.split(',')[0]) for coord in coords]
            subset['y'] = [int(coord.split(',')[1]) for coord in coords]

            superset.append(subset)

        entire_dataset.append(superset)
    return (
        coords,
        entire_dataset,
        i,
        j,
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
    return subset_idx, x, y


@app.cell
def __(entire_dataset, plt, superset_idx):
    superset_single = entire_dataset[superset_idx]
    for p, subset_this_super in enumerate(superset_single):
        plt.scatter(subset_this_super['x'], subset_this_super['y'])
    plt.show()
    return p, subset_this_super, superset_single


if __name__ == "__main__":
    app.run()
