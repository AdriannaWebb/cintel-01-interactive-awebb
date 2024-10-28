import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# add page options for the overall app
ui.page_opts(title="PyShiny App with Plot", fillable=True)

#create sidebar w/ sidebar input
with ui.sidebar():
    # Add a slider for specifying the number of bins in the histogram.
    # ui.input_slider has 5 arguments:
    # 1. A string id ("selected_number_of_bins") that uniquely identifies this input.
    # 2. A string label ("Number of Bins") displayed alongside the slider.
    # 3. An integer for the minimum number of bins (0).
    # 4. An integer for the maximum number of bins (100).
    # 5. An integer for the initial value (20).
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    # Define the number of points to generate
    count_of_points: int = 437
    np.random.seed(19680801)  # Set a seed for reproducibility

    # Generate random data
    random_data_array = 100 + 15 * np.random.randn(count_of_points)

    # Create the histogram using the selected number of bins
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)

    # Change the plot style
    plt.style.use('seaborn-darkgrid')  
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color='teal', alpha=0.7)



