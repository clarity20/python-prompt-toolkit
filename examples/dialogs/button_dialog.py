#!/usr/bin/env python
"""
Example of button dialog window.
"""
#MMMM Hack for easier testing: import from local repo instead of python3 installation
import os
import sys
sys.path.insert(0, ".." + os.sep + "..")
from prompt_toolkit.shortcuts import button_dialog


def main():
    result = button_dialog(
        title="Button dialog example",
        text="Are you sure?",
        buttons=[("Yes", True), ("No", False), ("Maybe...", None)],
    ).run()

    print(f"Result = {result}")

    result = button_dialog(
        title="Button dialog example",
        text="Are you sure?",
        buttons=[("Yes", True), ("N&o", False), ("Maybe...", None)],
        force_hotkeys=True
    ).run()

    print(f"Result = {result}")


if __name__ == "__main__":
    main()
