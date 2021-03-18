from fpdf import FPDF
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.bible.optina.ru/new:mf:01:01")
class_name = "wrapper"
div = driver.find_element_by_class_name(class_name)
print(div.text)

pdf = FPDF()
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 14)

pdf.add_page()
pdf.cell(5.0,0.5,div.text)
pdf.output('test.pdf','F')

driver.quit()