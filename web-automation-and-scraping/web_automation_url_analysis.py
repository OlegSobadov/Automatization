# Web Automation and URL Analysis
# ----------------------
#
# This script automates web browsing tasks such as entering URLs, interacting with the address bar, and navigating to the next URL.
# It also saves visited URLs to a JSON file for further analysis.
#

import os
import time
from datetime import date
import webbrowser
import pyautogui
import pyperclip
import requests
from bs4 import BeautifulSoup
import json


def addr_bar():
    """
    Simulate the key press for opening the address bar.
    Presses the Ctrl + L key combination.
    """
    pyautogui.keyDown('ctrl')
    pyautogui.press('l')
    pyautogui.keyUp('ctrl')


def nav_next_url():
    """
    Simulate the key press for navigating to the next URL.
    Presses the Ctrl + Tab key combination.
    """
    pyautogui.keyDown('ctrl')
    pyautogui.press('tab')
    pyautogui.keyUp('ctrl')


def save_into_buffer():
    """
    Simulate the key press for copying the address bar value to the clipboard.
    Presses the Ctrl + C key combination.
    """
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')


def get_page_header_text(url):
    """
    Retrieve the header text from the provided URL.
    Returns the text if found, or None if not found.
    
    Parameters:
    - url (str): The URL to retrieve the header text from.
    
    Returns:
    - str or None: The header text if found, or None if not found.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    header_item = soup.find('header')

    if header_item:
        header_text = header_item.get_text(strip=True)
        return header_text
    else:
        return None


# Simulate Alt + F4 to close the web browser
# pyautogui.hotkey('alt', 'f4')