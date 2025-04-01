# Web Scraper for Spanish News Articles

## Overview
This project is a Python-based web scraper that extracts article titles, content, and images from the "Opinión" section of the Spanish news website [El País](https://elpais.com/). It also translates article titles from Spanish to English, saves images locally, and analyzes the most frequently used words in the translated titles.

## Features
- **Automated Web Scraping:** Uses Selenium WebDriver to navigate the website.
- **Pop-up Handling:** Closes cookie consent pop-ups automatically.
- **Language Validation:** Ensures the webpage is in Spanish (`es-ES`).
- **Article Extraction:** Scrapes titles, summaries, and images from articles.
- **Translation:** Converts Spanish titles to English using Google Translate.
- **Image Downloading:** Saves article images to a local directory.
- **Word Frequency Analysis:** Identifies commonly repeated words in translated titles.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Google Chrome (latest version)
- Chrome WebDriver (automatically managed via `webdriver_manager`)

## Installation
Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/mahimaquadras/browserstackAssignment.git
cd browserstackAssignment
```

### Install Required Dependencies
You can install the necessary dependencies manually:
```bash
pip install selenium webdriver-manager requests googletrans==4.0.0-rc1
```
Alternatively, create a `requirements.txt` file with the following content:
```
selenium
webdriver-manager
requests
googletrans==4.0.0-rc1
```
Then install all dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
To run the script, execute the following command:
```bash
python scraper.py
```

## Running the Script on BrowserStack
If you want to run the script on BrowserStack, use the following command:
```bash
browserstack-sdk python scraper.py
```

## Expected Output
- **Terminal Output:**
  - Extracted article titles and summaries (in Spanish and English).
  - List of frequently repeated words in translated titles.
- **Saved Files:**
  - Article images will be stored in the `images/` directory.

---
