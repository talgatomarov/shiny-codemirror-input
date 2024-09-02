from htmltools import Tag, HTMLDependency
from pathlib import PurePath
from shiny.module import resolve_id

codemirror_input_deps = HTMLDependency(
    "codemirror-input",
    "0.1.0",
    source = {
        "package": "shiny_codemirror_input",
        "subdir": str(PurePath(__file__).parent / "distjs"),
    },
    script = {"src": "index.js", "type": "module"}
)

def codemirror_input(id):
    tag = Tag(
        "div",
        codemirror_input_deps,
        id=resolve_id(id)
    )

    tag.add_class("codemirror-input")

    return tag 