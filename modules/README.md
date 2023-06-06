
# Auto Import Modules

Auto Import Modules is a utility script that dynamically imports specified modules based on a list of module names read from a text file. It checks if the modules are non-standard and adds them to the global variables.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Module Import](#module-import)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ````bash
    git clone https://github.com/OlegSobadov/Automatization.git
    ````
2. Navigate to the project directory:
    ````bash
    cd modules
    ````
3. Install the required dependencies:

    ````bash
    pip install -r requirements.txt -U
    ````

## Usage

1. Create a text file named `autoimports.txt` in the same directory as the script.
2. Add the module names, each on a separate line, to the `autoimports.txt` file. For example:
    ````bash
    re
    math
    os
    ````
3. Add the script to your project. 
    <br>For example:

    ````bash
    python example_usage_autoimports.py
    ````

The script will dynamically import the modules listed in `autoimports.txt` and add them to the global variables.

## Module Import

The `autoimports.py` script consists of the following functions:

- `import_module(module_name)`: Dynamically imports a module and adds it to the caller's globals.
- `is_nonstandard_module(module)`: Checks if a module is considered non-standard.
- `warn_nonstandard_module_usage(module)`: Issues a deprecation warning for non-standard module usage.
- `auto_import_modules()`: Auto-imports the specified modules and updates the globals dictionary.

The script reads the module names from the `autoimports.txt` file, dynamically imports each module, checks if it is non-standard, and adds it to the globals dictionary.

## Contributions
Contributions are welcome! If you have any suggestions, improvements, or new features to add, please follow these steps:

1. Fork the repository.

2. Create a new branch:
    ````bash
    git checkout -b feature/new-feature
    ````
3. Make your changes and commit them:


    ````bash
    git commit -m "Add new feature"
    ````
4. Push your changes to your forked repository:

    ````bash
    git push origin feature/new-feature
    ````
5. Open a pull request in this repository with a detailed description of your changes.


## Contact

If you have any questions or suggestions, feel free to reach out to me:

- Email: ubuntuwebserver@gmail.com
- LinkedIn: [ubuntu](https://www.linkedin.com/in/ubuntu/)

Happy coding!
Feel free to customize the content, add more automatization scripts, and update the contact information as per your requirements.


## License

This project is licensed under the [MIT License](LICENSE).
You can customize this template by replacing the placeholders (Auto Import Modules, Installation, Usage, etc.) with the relevant information for your project. Additionally, you can add more sections or modify the structure to provide additional details or instructions specific to your project.

Make sure to provide clear instructions on how to use the script, how to define the module names in the autoimports.txt file, and any other relevant information.


