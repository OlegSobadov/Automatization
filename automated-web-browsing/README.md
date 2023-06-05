
# Automated Web Browsing
This project aims to automate web browsing tasks using Python. It provides a script that allows you to visit multiple URLs, interact with web pages, and save the visited URLs to a file.

## Table of scripts

| # | Title | Language | Contact|
|---|-------|----------|--------|
| 1 | [multiply URLS](multiply_urls.py) | [Python](#configuration) | [Contact](#contact)|
| ... | ... | ... |

## Features
1. Simulates keyboard shortcuts to navigate web pages:
    - Presses 'Enter' to visit a URL
    - Presses 'Ctrl+L' to select the address bar
    - Presses 'Ctrl+Tab' to navigate to the next URL
    - Presses 'Ctrl+C' to save the address to the buffer

2. Uses the pyautogui library for GUI automation
3. Utilizes the pyperclip library to access the clipboard and retrieve the current URL
4. Supports customization of the number of URLs to visit and the timeout between visits
5. Implements logging to track the progress and activities during web browsing
6. Saves the visited URLs to a file for future reference

## Prerequisites
1. Make sure you have the following installed:
    Python (version 3.11 or later)<br>
    Required libraries: pyautogui, pyperclip, and logging

2. Install the libraries using pip:
    ````bash
    pip install pyautogui pyperclip
    ````

## Usage
1. Clone this repository:

    ````bash
    git clone https://github.com/your-username/automated-web-browsing.git
    ````
2. Navigate to the project directory:
    ````bash
    cd automated-web-browsing
    ````

3. Run the script:
    ````python
    python main.py
    ````

## Configuration
You can customize the behavior of the script using command line arguments:
````css
-c or --count: Specify the number of URLs to visit (default: 2)
-i or --input-file: Specify the file path to save the visited URLs (default: 'data/new_urls.txt')
-t or --timeout: Specify the timeout between visits in seconds (default: 2)
````
### Example usage:

````python
python main.py -c 5 -i visited_urls.txt -t 3
````

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