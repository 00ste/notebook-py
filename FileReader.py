class FileReader:
    def read_note_file(filename: str):
        obj = {
            "profile": {
                "name": "default",
                "page_width": 1280,
                "page_height": 720,
                "background_color": "#FFFFFF",
                "pen_profiles": [
                    {
                        "color": "#000000",
                        "width": 2,
                        "alpha": 1.0
                    },
                    {
                        "color": "#FF0000",
                        "width": 2,
                        "alpha": 1.0
                    },
                    {
                        "color": "#0000FF",
                        "width": 2,
                        "alpha": 1.0
                    },
                    {
                        "color": "#FF00FF",
                        "width": 2,
                        "alpha": 1.0
                    },
                    {
                        "color": "#FFFF00",
                        "width": 10,
                        "alpha": 0.3
                    },
                    {
                        "color": "#00FF00",
                        "width": 10,
                        "alpha": 0.3
                    },
                    {
                        "color": "#00FFFF",
                        "width": 10,
                        "alpha": 0.3
                    },
                    {
                        "color": "#FF00FF",
                        "width": 10,
                        "alpha": 1.0
                    }
                ]
            },
            "session": {
                "page": 0,
                "x_offset": 0,
                "y_offset": 0
            },
            "pages" : [
                {
                    "tags": [],
                    "strokes": [ {
                            "pen": 0,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }, {
                            "pen": 0,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }, {
                            "pen": 1,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }, {
                            "pen": 1,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }
                    ]
                },
                {
                    "tags": [],
                    "strokes": [ {
                            "pen": 0,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }, {
                            "pen": 0,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }, {
                            "pen": 1,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }, {
                            "pen": 1,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }
                    ]
                },
                {
                    "tags": [],
                    "strokes": [ {
                            "pen": 0,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }, {
                            "pen": 0,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }, {
                            "pen": 1,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }, {
                            "pen": 1,
                            "points": [
                                [10, 10], [10, 20], [20, 30], [100, 30]
                            ]
                        }
                    ]
                }
            ]
        }
        return obj

    def read_config_file(filename: str):
        obj = {
            "client": {
                "display_width": 1200,
                "display_height": 800,
                "light_profile": "default_light",
                "dark_profile" : "default_dark",
                "contrast_profile": "default_contrast",
                "keybinds": {
                    "pan_left" : ["H"],
                    "pan_down" : ["J"],
                    "pan_up" : ["K"],
                    "pan_right": ["L"],
                    "select_tool": ["S"],
                    "pen_tool": ["P"],
                    "move_tool": ["M"],
                    "text_tool": ["T"],
                    "shape_tool" : ["A"],
                    "next_page": ["CTRL\\+L"],
                    "prev_page": ["CTRL\\+P"], 
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
                    "undo": ["CTRL\\+Z"],
                    "redo": ["CTRL\\+Y"],
                    "save": ["CTRL\\+S"],
                    "exit": ["CTRL\\+Q"],
                    "show_debug_screen": ["TAB"]
                }
            },
            "default_profile": {
                "page_width": 1280,
                "page_height": 720,
                "background_color": "#fbfcef",
                "pen_profiles": [
                    {
                        "color": "#000000",
                        "width": 2,
                        "alpha": 1.0
                    },
                    {
                        "color": "#FF0000",
                        "width": 2,
                        "alpha": 1.0
                    },
                    {
                        "color": "#0000FF",
                        "width": 2,
                        "alpha": 1.0
                    },
                    {
                        "color": "#FF00FF",
                        "width": 2,
                        "alpha": 1.0
                    },
                    {
                        "color": "#FFFF00",
                        "width": 10,
                        "alpha": 0.3
                    },
                    {
                        "color": "#00FF00",
                        "width": 10,
                        "alpha": 0.3
                    },
                    {
                        "color": "#00FFFF",
                        "width": 10,
                        "alpha": 0.3
                    },
                    {
                        "color": "#FF00FF",
                        "width": 10,
                        "alpha": 1.0
                    }
                ]
            }
        }
        return obj



