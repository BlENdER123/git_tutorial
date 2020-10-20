from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.livejournal.com/rsearch?tags=%D0%BC%D0%B0%D1%81%D0%BE%D0%BD%D1%8B&searchArea=post")
    
    link = driver.find_element_by_class_name("rsearch-note__caption")
    print(link.text)

main()