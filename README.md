# CodeMirror Input Bindings for Shiny

## Overview
This repository provides a CoreMirror 6 input binding for Shiny applications, enabling advanced code editing features within the Shiny interface. This was developed for my side project where I needed users to input SQL queries. As a result, it currently support only SQL mode and does not allow for customization.

If you are interested in a more generic implementation, please open an issue to let me know.

## Installation

```bash
pip install git+https://github.com/talgatomarov/shiny-codemirror-input
```

## Usage Example

```python
from shiny_codemirror_input import codemirror_input
from shiny.express import render, input

codemirror_input("cm")

@render.text
def _():
    return input.cm()
```
