# notebook-py

A lightweight application for hand-written notes.

# Building and installing

WIP...

# Configuration

The directory structure of the configuration folder must be the following:

```
config
├── client.json
└── themes
    ├── theme1.json
    ├── theme2.json
    ...
```

## Client configuration

The client configuration file contains information about the default window size, the profile and themes to be used and the keyboard shortcuts.

An example of a client configuration file is the following:

```json
{
    "display-width": 1200,
    "display-height": 800,

    "default_theme_light": "default_light",
    "default_theme_dark": "default_dark",

    "default_page_width": 1280,
    "default_page_height": 720,

    "keybinds": {
        "pan_left": ["H"],
        "pan_down": ["J"],
        "pan_up": ["K"],
        "pan_right": ["L"],
        "next_page": ["CTRL L"],
        "prev_page": ["CTRL P"],
        "select_pen_0": ["1"],
        "select_pen_1": ["2"],
        "select_pen_2": ["3"],
        "select_pen_3": ["4"],
        "select_pen_4": ["5"],
        "select_pen_5": ["6"],
        "select_pen_6": ["7"],
        "select_pen_7": ["8"],
        "select_pen_8": ["9"],
        "select_pen_9": ["0"],
        "undo": ["CTRL Z"],
        "redo": ["CTRL Y"],
        "save": ["CTRL S"],
        "exit": ["CTRL Q"],
        "show_debug_screen": ["TAB"]
    }
}
```

## Themes

Themes determine the colour of the page and the colour and witdh of the pens. Themes are associated with the client (with lower priority) and with the page (with higher priority). The client themes will be associated with every new notebook.

An example of theme files is the following:

```json
{
    "page_color": "0xFBFCEF",
    "pens": [
        {
            "color": "0x000000",
            "width": 2,
            "alpha": 1.0
        },
        {
            "color": "0xFF0000",
            "width": 2,
            "alpha": 1.0
        },
        {
            "color": "0x0000FF",
            "width": 2,
            "alpha": 1.0
        },
        {
            "color": "0xFF00FF",
            "width": 2,
            "alpha": 1.0
        },
        {
            "color": "0xFFFF00",
            "width": 25,
            "alpha": 0.3
        },
        {
            "color": "0x00FF00",
            "width": 25,
            "alpha": 0.3
        },
        {
            "color": "0x00FFFF",
            "width": 25,
            "alpha": 0.3
        },
        {
            "color": "0xFF00FF",
            "width": 25,
            "alpha": 0.3
        }
    ]
}
```

# Notebook files

Notebook as saved as `.nbpy` files, which are ultimately `json` files. Each notebook file will contain data about configuration, session, bookmarks, and most importantly the list of pages along with their contents (strokes, shapes, text blocks, image blocks, etc...).

## Bookmarks

The user can insert bookmarks to specify comments or to quickly find important sections and keep the notebook organised.

## Example `.nbpy` file

```json
{
    "theme_light": "theme_default_light",
    "theme_dark": "theme_default_dark",
    "page_width": 1280,
    "page_height": 700,
    "bookmarks": {
        "bookmark1": {
            "page": 1,
            "x": 100,
            "y": 300
        },
        "bookmark2": {
            "page": 0,
            "x": 600,
            "y": 300
        },
    },
    "pages": [
        {
            "strokes": [
                [0010010005000000, 0010020005000000],
                [0010010005000000, 0010020005000000],
                [0010010005000000, 0010020005000000]
            ]
        },
        {
            "strokes": [
                [0010010005000000, 0010020005000000],
                [0010010005000000, 0010020005000000],
                [0010010005000000, 0010020005000000]
            ]
        },
    ]
}
```