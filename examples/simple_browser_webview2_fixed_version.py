import os
from pathlib import Path
import webview

"""
This example demonstrates how to create a webview window.
"""

if __name__ == '__main__':
    # Create a standard webview window
    exe_dir = Path(os.getcwd()).parent / "webview2"
    window = webview.create_window('Simple browser', 'https://pywebview.flowrl.com/hello')
    webview.start(exe_dir=str(exe_dir))
    