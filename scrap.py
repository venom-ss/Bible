from selenium import webdriver
#from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.bible.optina.ru/new:mf:01:01")
div = driver.find_element_by_class_name("wrapper")
print(div.text)
driver.quit()