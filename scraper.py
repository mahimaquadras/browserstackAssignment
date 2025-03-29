import os
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from googletrans import Translator
from collections import Counter

def setup_driver():
    options = Options()
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def handle_popup(driver):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))).click()
        print("Pop-up closed.")
    except:
        print("No pop-up found.")

def validateLanguage(driver):
    try:
        html_element = driver.find_element("tag name", "html")
        lang_attribute = html_element.get_attribute("lang")

        if lang_attribute == "es-ES":
            print("The lang attribute is correctly set to es-ES.")
        else:
            print(f"Lang attribute is not 'es-ES'.")

    except:
        print("No pop-up found.")

def navigate_to_opinion(driver):
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Opinión"))).click()
        print("Navigated to Opinion section.")
    except:
        print("Opinion section not found.")
        driver.quit()
        exit()

def translate_title(title):
    translator = Translator()
    return translator.translate(title, src="es", dest="en").text.lower()

def scrape_articles(driver, num_articles=5):
    
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article")))
    articles = driver.find_elements(By.CSS_SELECTOR, "article")[:num_articles]
    
    os.makedirs("images", exist_ok=True)
    translated_titles = []
    
    for index, article in enumerate(articles):
        try:
            # Extract title and content
            title = article.find_element(By.TAG_NAME, "h2").text.strip().lower()
            content = article.find_element(By.TAG_NAME, "p").text.strip() if article.find_elements(By.TAG_NAME, "p") else "No content available."
            translated_title = translate_title(title)
            translated_titles.append(translated_title)

            # Extract image if available
            img_elements = article.find_elements(By.TAG_NAME, "img")
            image_status = "No image found."
            if img_elements:
                img_url = img_elements[0].get_attribute("src")
                img_data = requests.get(img_url).content
                with open(f"images/article_{index + 1}.jpg", "wb") as img_file:
                    img_file.write(img_data)
                image_status = f"Image saved for '{title}'"

            # Print extracted data
            print(f"\nArticle {index + 1}")
            print(f"Title (Spanish): {title}")
            print(f"Content: {content[:200]}...") 
            print(f"Title (English): {translated_title}")
            print(image_status) 

        except Exception as e:
            print(f"Error processing article {index + 1}: {e}")

    return translated_titles

def count_repeated_words(titles):
    
    word_counter = Counter()
    for title in titles:
        for word in re.findall(r'\b\w+\b', title):
            word_counter[word] += 1

    repeated_words = {word: count for word, count in word_counter.items() if count > 2}

    print("\nRepeated Words in Translated Titles:")
    if repeated_words:
        for word, count in repeated_words.items():
            print(f"{word}: {count} times")
    else:
        print("No words repeated more than twice.")

def main():
    driver = setup_driver()
    driver.get("https://elpais.com/")

    handle_popup(driver)
    validateLanguage(driver)
    navigate_to_opinion(driver)
    translated_titles = scrape_articles(driver, num_articles=5)
    count_repeated_words(translated_titles)

    driver.quit()
    print("\nScraping complete!")

if __name__ == "__main__":
    main()
