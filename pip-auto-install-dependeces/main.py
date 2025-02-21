# any of your projects that require specific libraries to be installed
import sys
import importlib
import numpy as np
import pandas as pd
import requests

def check_imports():
    """Ensure all required libraries are imported correctly."""
    required_libs = ["numpy", "pandas", "requests"]
    for lib in required_libs:
        if importlib.util.find_spec(lib) is None:
            print(f"Error: {lib} is not installed. Ensure dependencies are correctly installed.")
            sys.exit(1)

if __name__ == "__main__":
    check_imports()
    print("All dependencies are installed. Running main application...")

    # Example logic to use installed libraries
    data = np.array([[1, 2, 3], [4, 5, 6]])
    df = pd.DataFrame(data, columns=["A", "B", "C"])
    
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    json_data = response.json()

    print("DataFrame Example:\n", df)
    print("API Response Example:\n", json_data)

    print("Application started successfully!")
