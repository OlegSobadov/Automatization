import importlib.util
import os
import sys
import subprocess

# List of required packages
REQUIRED_LIBS = ["numpy", "pandas", "requests"]  # Add your actual dependencies

def install_package(package):
    """Check if a package is installed, and install it if necessary."""
    if importlib.util.find_spec(package) is None:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
            sys.exit(1)
    else:
        print(f"{package} is already installed.")

def ensure_dependencies():
    """Ensure all required dependencies are installed."""
    for lib in REQUIRED_LIBS:
        install_package(lib)

if __name__ == "__main__":
    ensure_dependencies()
    
    # Your main application logic starts here
    # running all libraries after installing to ensure they are installed correctly
    try:
        import numpy as np
        import pandas as pd
        import requests
        
        os.environ['TRUST_REMOTE_CODE'] = 'True'
        print("All dependencies are installed. Running main application...")
        print("Application started successfully!")
    except BaseException as e:
        print(f"Exception found during import: {e}")
