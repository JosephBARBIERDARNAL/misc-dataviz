from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt


class Layout:
    def __init__(self, rows=1, columns=1, elements=None):
        self.rows = rows
        self.columns = columns
        self.elements = elements if elements is not None else []

    def __add__(self, other):
        """Horizontal combination: place self and other side by side."""
        new_rows = max(self.rows, other.rows)
        new_columns = self.columns + other.columns
        new_elements = []

        # Adjust self's elements to center vertically
        v_offset_self = (new_rows - self.rows) // 2
        for elem in self.elements:
            new_elem = {
                "row": elem["row"] + v_offset_self,
                "column": elem["column"],
                "row_span": elem["row_span"],
                "column_span": elem["column_span"],
            }
            new_elements.append(new_elem)

        # Adjust other's elements to fit new_rows and shift columns
        v_offset_other = (new_rows - other.rows) // 2
        for elem in other.elements:
            new_elem = {
                "row": elem["row"] + v_offset_other,
                "column": elem["column"] + self.columns,
                "row_span": new_rows,  # Span all available rows
                "column_span": elem["column_span"],
            }
            new_elements.append(new_elem)

        return Layout(new_rows, new_columns, new_elements)

    def __truediv__(self, other):
        """Vertical combination: place self above other."""
        new_rows = self.rows + other.rows
        new_columns = max(self.columns, other.columns)
        new_elements = []

        # Adjust self's elements to center horizontally
        h_offset_self = (new_columns - self.columns) // 2
        for elem in self.elements:
            new_elem = {
                "row": elem["row"],
                "column": elem["column"] + h_offset_self,
                "row_span": elem["row_span"],
                "column_span": elem["column_span"],
            }
            new_elements.append(new_elem)

        # Adjust other's elements to fit new_columns and shift rows
        h_offset_other = (new_columns - other.columns) // 2
        for elem in other.elements:
            new_elem = {
                "row": elem["row"] + self.rows,
                "column": elem["column"] + h_offset_other,
                "row_span": elem["row_span"],
                "column_span": new_columns,  # Span all available columns
            }
            new_elements.append(new_elem)

        return Layout(new_rows, new_columns, new_elements)

    def create_figure(self, **kwargs):
        """Generates the figure and axes using matplotlib's GridSpec."""
        fig = plt.figure(**kwargs)
        gs = GridSpec(self.rows, self.columns, figure=fig)
        axes = []
        for elem in self.elements:
            ax = fig.add_subplot(
                gs[
                    elem["row"] : elem["row"] + elem["row_span"],
                    elem["column"] : elem["column"] + elem["column_span"],
                ]
            )
            axes.append(ax)
        return fig, axes


def Ax():
    """Creates a single Axes layout."""
    return Layout(1, 1, [{"row": 0, "column": 0, "row_span": 1, "column_span": 1}])


if __name__ == "__main__":
    # Create individual axes layouts
    a = Ax()
    b = Ax()
    c = Ax()

    # Arrange axes: (a + b) on top, c below spanning both columns
    layout = (a + b) / a

    # Generate the figure and axes
    fig, axes = layout.create_figure(figsize=(8, 6))

    # Plot on each axes
    import numpy as np

    x = np.linspace(0, 10, 100)
    axes[0].plot(x, np.sin(x))
    axes[1].plot(x, np.cos(x))
    axes[2].plot(x, np.tan(x))

    # Adjust layout and display
    plt.tight_layout()
    plt.show()
