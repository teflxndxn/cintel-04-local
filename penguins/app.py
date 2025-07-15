# Additional Python Notes
# ------------------------
# Capitalization matters in Python. Python is case-sensitive: min and Min are different.
# Spelling matters in Python. You must match the spelling of functions and variables exactly.
# Indentation matters in Python. Indentation is used to define code blocks and must be consistent.

# Functions
# ---------
# Functions are used to group code together and make it more readable and reusable.
# We define custom functions that can be called later in the code.
# Functions are blocks of logic that can take inputs, perform work, and return outputs.

# Defining Functions
# ------------------
# Define a function using the def keyword, followed by the function name, parentheses, and a colon. 
# The function name should describe what the function does.
# In the parentheses, specify the inputs needed as arguments the function takes.

# The function filtered_data() takes no arguments.
# The function between(min, max) takes two arguments, a minimum and maximum value.
# Arguments can be positional or keyword arguments, labeled with a parameter name.

# The function body is indented (consistently!) after the colon. 
# Use the return keyword to return a value from a function.

# Calling Functions
# -----------------
# Call a function by using its name followed by parentheses and any required arguments.

# Decorators
# ----------
# Use the @ symbol to decorate a function with a decorator.
# Decorators are a concise way of calling a function on a function.
# We don't typically write decorators, but we often use them.

import plotly.express as px
from shiny import App, ui, render, reactive, req
from shinywidgets import output_widget, render_widget
import seaborn as sns
from palmerpenguins import load_penguins

penguins_df = load_penguins()

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.h2("Sidebar"),
            ui.input_selectize(
                "selected_attribute",
                "Choose attribute",
                ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
            ),
            ui.input_numeric(
                "plotly_bin_count",
                "Plotly Histogram Bins",
                10
            ),
            ui.input_slider(
                "seaborn_bin_count",
                "Seaborn Histogram Bins",
                5, 50, 20
            ),
            ui.input_checkbox_group(
                "selected_species_list",
                "Filter Species",
                ["Adelie", "Gentoo", "Chinstrap"],
                selected=["Adelie", "Gentoo", "Chinstrap"],
                inline=True
            ),
            ui.hr(),
            ui.a(
                "GitHub",
                href="https://github.com/teflxndxn/cintel-02-data",
                target="_blank"
            ),
            open="open"
        ),
        ui.layout_columns(
            ui.output_data_frame("penguin_data_table"),
            ui.output_data_frame("penguin_data_grid")
        ),
        ui.layout_columns(
            output_widget("plotly_histogram"),
            ui.output_plot("seaborn_histogram"),
            ui.card(
                ui.card_header("Plotly Scatterplot: Species"),
                output_widget("plotly_scatterplot"),
                full_screen=True
            )
        )
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_data():
        # Ensure the user selected at least one species
        req(input.selected_species_list())
        
        # Filter the DataFrame to only include selected species
        return penguins_df[penguins_df["species"].isin(input.selected_species_list())]

    @render.data_frame
    def penguin_data_table():
        return filtered_data()

    @render.data_frame
    def penguin_data_grid():
        return filtered_data()

    @render_widget
    def plotly_histogram():
        col = input.selected_attribute()
        bins = input.plotly_bin_count()
        if not bins:
            bins = 10
        fig = px.histogram(
            filtered_data(),
            x=col,
            nbins=int(bins),
            color="species",
            title=f"Plotly Histogram of {col}"
        )
        return fig

    @render.plot
    def seaborn_histogram():
        col = input.selected_attribute()
        bins = input.seaborn_bin_count()
        if not bins:
            bins = 20
        sns.histplot(
            data=filtered_data(),
            x=col,
            bins=int(bins),
            hue="species"
        )

    @render_widget
    def plotly_scatterplot():
        fig = px.scatter(
            filtered_data(),
            x="bill_length_mm",
            y="flipper_length_mm",
            color="species",
            symbol="species",
            hover_data=["species", "island"],
            labels={
                "bill_length_mm": "Bill Length (mm)",
                "flipper_length_mm": "Flipper Length (mm)"
            },
            title="Bill Length vs Flipper Length by Species"
        )
        return fig

app = App(app_ui, server)
