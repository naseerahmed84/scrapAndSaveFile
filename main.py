from selenium import webdriver
from datetime import datetime as dt
import time
def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output
def write_file(text):
    """write input text into a text file"""
    # created a file name called filename which is unique instance of time
    filename = f"{dt.now().strftime('%Y-%m-%d-%H-%M-%S')}.text"
    # 'w' means writeMode inside a variable called file and then passed the text to be stored
    with open(filename,'w') as file:
        file.write(text)
def main():
  driver = get_drvier()
  while True:
      time.sleep(2)
      element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
      text = str(clean_text(element.text))
      write_file(text)

print(main())