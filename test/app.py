from shiny_codemirror_input import codemirror_input
from shiny.express import ui, render, input
from shiny import reactive

ui.page_opts(
    title = "Retrieve LastName and Salary of each employee", 
    fillable=True
)

codemirror_input("cm")

ui.input_task_button("btn", "button")


@render.text
def _():
    return input.cm()
