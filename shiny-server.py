from shiny import App, render, ui

# Define the UI
app_ui = ui.page_fluid(
    ui.h2("Hello, World!"),
)

# Define the server logic
def server(input, output, session):
    pass  # No server logic needed for Hello World

# Create the Shiny app
app = App(app_ui, server)
