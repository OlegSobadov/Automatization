import argparse
import pyautogui
import pyperclip
import time
import logging


def select_address_bar():
    """
    Selects the address bar in the web browser.

    Presses 'Ctrl+L' to activate the address bar for user input.
    """
    pyautogui.keyDown('ctrl')
    pyautogui.press('l')
    pyautogui.keyUp('ctrl')

def navigate_to_next_url():
    """
    Navigates to the next URL in the web browser.

    Presses 'Ctrl+Tab' to switch to the next tab or URL.
    """
    pyautogui.keyDown('ctrl')
    pyautogui.press('tab')
    pyautogui.keyUp('ctrl')

def save_address_to_buffer():
    """
    Saves the current address to the buffer.

    Presses 'Ctrl+C' to copy the current address to the clipboard buffer.
    """
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def get_current_url():
    """
    Retrieves the current URL from the clipboard.

    Returns:
        str: The current URL in the clipboard.
    """
    return pyperclip.paste()

def visit_urls(count):
    """
    Visits multiple URLs in the web browser.

    Args:
        count (int): The number of URLs to visit.

    Returns:
        list: A list of visited URLs.

    Raises:
        ValueError: If count is less than or equal to zero.
    """
    if count <= 0:
        raise ValueError("Invalid count. Count must be greater than zero.")

    visited_urls = []
    logging.info('Visiting URLs...')
    for _ in range(count):
        visit_url()
        current_url = get_current_url()
        visited_urls.append(current_url)
        navigate_to_next_url()
    logging.info('URL visit completed.')
    return visited_urls

def visit_url():
    """
    Visits a single URL in the web browser.

    Presses 'Enter' to visit the URL, selects the address bar, and saves the address to the buffer.
    """
    time.sleep(2)
    pyautogui.press('enter')
    select_address_bar()
    logging.info('Selected address bar')
    save_address_to_buffer()
    time.sleep(1)  # Wait to save value to buffer
    logging.info('Saved address bar to buffer')

def save_urls_to_file(urls, output_file):
    """
    Saves the visited URLs to a file.

    Args:
        urls (list): List of visited URLs.
        output_file (str): The file path to save the URLs.
    """
    with open(output_file, 'w') as file:
        file.writelines(urls)

def setup_logging():
    """
    Sets up logging configuration.

    Configures the log level, format, and handlers for logging.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('automation.log'),
            logging.StreamHandler()
        ]
    )

def main():
    """
    The main function of the Automated Web Browsing project.

    Parses command line arguments, sets up logging, visits URLs, saves the visited URLs to a file, and logs the progress.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Automated web browsing')
    parser.add_argument('-c', '--count', type=int, default=2, help='Number of URLs to visit')
    parser.add_argument('-i', '--input-file', type=str, default='data/new_urls.txt', help='Path to save visited URLs')
    parser.add_argument('-t', '--timeout', type=int, default=2, help='Timeout between visits in seconds')
    args = parser.parse_args()

    # Set up logging
    setup_logging()

    try:
        # Visit URLs
        visited_urls = visit_urls(args.count)

        # Save visited URLs to file
        save_urls_to_file(visited_urls, args.input_file)

        logging.info('Visited URLs successfully saved to file: %s', args.input_file)
    except Exception as e:
        logging.error('An error occurred: %s', str(e))

if __name__ == '__main__':
    main()
