"""Execute every notebook cell and save outputs in place. Run from project root."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent
path = root/'Food_Delivery_Time_KDD.ipynb'
notebook = nbformat.read(path, as_version=4)
NotebookClient(notebook, timeout=1200, kernel_name='python3',
               resources={'metadata': {'path':str(root)}}).execute()
nbformat.write(notebook,path)
print(f'Executed and saved: {path.name}')
