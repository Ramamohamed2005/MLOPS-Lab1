import pandas as pd
import tkinter as tk
from tkinter import filedialog

def read_csv():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv")]
    )

    if file_path:
        data = pd.read_csv(file_path)
        print(data.head(3))
    else:
        print("No file selected.")

read_csv()