import os
from pathlib import Path
import logging

project_name = "src"

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exceptions/__init__.py",
    f"{project_name}/loading/__init__.py",
    f"{project_name}/indexing/__init__.py",
    f"{project_name}/quering/__init__.py",
    f"{project_name}/storing/__init__.py",
    "notebook/experiments.ipynb",
    "test.py",
    "app.py"
]

for file_path in list_of_files:
    file_path = Path(file_path)

    file_dir, file_name = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, 'w') as f:
            pass
    else:
        print(f"file is already at: {file_path}")