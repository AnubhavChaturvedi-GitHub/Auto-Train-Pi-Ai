import random
import time

from selenium.webdriver.common.keys import Keys
from Head.Mouth import *
from Head.Mouth3 import speak

chrome_options = Options()
chrome_options.add_argument("--headless")
# Set up the WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://pi.ai/onboarding")
time.sleep(1)

# Click the first button using XPath
button_1 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/button')
button_1.click()

# Wait for the page to load or perform any necessary actions
time.sleep(0.5)

# Click the second button using XPath
button_2 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/button')
button_2.click()

# Wait for the page to load or perform any necessary actions
time.sleep(0.5)

# Click the fourth button using XPath
button_4 = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div[1]/div[2]/button[1]')
button_4.click()

# Wait for the page to load or perform any necessary actions
time.sleep(2)

# Locate the textarea using its XPath
textarea = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea')
def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict

qa_file_path = r"C:\Users\vlogp\Desktop\JARVIS 4.0\Data\brain_data\qna_dat.txt"
qa_dict = load_qa_data(qa_file_path)

def save_qa_data(file_path, qa_dict):
    with open(file_path, "w", encoding="utf-8") as f:
        for q, a in qa_dict.items():
            f.write(f"{q}:{a}\n")


def chat(text):
    # Type your desired text into the textarea
    textarea.send_keys(text)

    # Simulate pressing the Enter key
    textarea.send_keys(Keys.ENTER)

    # Wait for the page to load or perform any necessary actions
    time.sleep(2)

    # Click the button using its XPath
    button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button')
    button.click()

    # ... (previous code)

    # Wait for the page to load or perform any necessary actions
    time.sleep(2)

    # Retrieve the text from the specified XPath
    response_xpath = '//*[@id="__next"]/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/span'
    response_element = driver.find_element(By.XPATH, response_xpath)
    response_text = response_element.text

    # Print or use the response text as needed

    print(response_text)
    qa_dict[text] = response_text  # Store in qa_dict
    save_qa_data(qa_file_path, qa_dict)





while True:
    x = ["hello", "hey there", "bye", "good day", "hi", "greetings", "howdy", "salutations", "hola", "good morning",
         "good afternoon", "good evening", "see you later", "farewell", "take care", "until we meet again", "adios",
         "so long", "cheerio", "what's up", "sup", "yo", "hiya", "how's it going", "hi there", "nice to meet you",
         "ciao", "arrivederci", "au revoir", "peace out", "later", "till next time", "have a good one",
         "goodbye for now", "catch you later", "keep in touch", "best regards", "warm regards", "take it easy",
         "hello", "hey there", "bye", "good day", "how are you", "what's new", "what's happening", "how's everything",
         "what's going on", "how's life", "good to see you", "nice to see you", "welcome back", "long time no see",
         "glad you're here", "see you soon", "until next time", "looking forward to our next meeting", "stay well",
         "be safe", "hello", "hey there", "bye", "good day", "hello", "hey there", "bye", "good day", "how are you",
         "what's new", "what's happening", "how's everything", "what's going on", "how's life", "good to see you",
         "nice to see you", "welcome back", "long time no see", "glad you're here", "see you soon",
         "until next time", "looking forward to our next meeting", "stay well", "be safe", "hey buddy", "hi friend",
         "greetings and salutations", "wassup", "what's crackin'", "how's everything going", "fare thee well",
         "peace and blessings", "have a great day", "enjoy your day", "have a fantastic time", "keep smiling",
         "spread positivity", "take it one day at a time", "sending good vibes", "stay positive",
         "hello to all my subscribers", "thanks for the support", "appreciate each one of you",
         "stay tuned for more"]
    x = random.choice(x)
    chat(x)