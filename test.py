

from fpdf import FPDF
from bs4 import BeautifulSoup
import urllib3,re

req = urllib3.PoolManager()
res = req.request('GET', "http://www.bible.optina.ru")
s_soup = BeautifulSoup(res.data, 'html.parser')

menu_links = s_soup.find_all(href=re.compile("(?=.*new:)(?=.*:start)") )


pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)

def stix(src):
	pdf.set_font('DejaVu', '', 22)
	pdf.cell(200, 30, txt=src, ln=1, align="C")

def title(src):
	pdf.set_font('DejaVu', '', 16)
	pdf.cell(200, 10, txt=src, ln=1, align="C")

def paragraph(src):
	pdf.set_font('DejaVu', '', 12)
	pdf.multi_cell(190.0, 5.0, txt = src, border = 0, align= 'J', fill=False)
	


for item in menu_links:
	menu_link = "http://bible.optina.ru"+item["href"]
	res = req.request('GET', menu_link)
	soup = BeautifulSoup(res.data, 'html.parser')
	elems = soup.find_all("a", {"class":"wikilink1"})
	# print(elems)
	

	for j in elems:
		link = "http://bible.optina.ru"+j["href"]
		print(link+"\n")
		res = req.request('GET', link)
		soup = BeautifulSoup(res.data, 'html.parser')
		# title = soup.find("h2", {"class":"sectionedit2"})
		content = soup.find_all("div", {"class":"level2"})
		# print(content)
		h1 = soup.find("h1", {"class":"sectionedit1"})

		# print(h1)
		stix(h1.get_text())
		for elem in content:
			# print(elem.find_previous().get_text())

			h2 = elem.find_previous().get_text()
			p = elem.get_text()
			
			title(h2)
			paragraph(p)
			# pdf.add_page()
		# pdf.set_title(title_text)

# pdf.cell(200, 10, txt=text1.get_text(), ln=1, align="C")
#pdf.multi_cell(190.0, 5.0, txt = title_text, border = 0, align= 'J', fill=False)
pdf.output("sample_demo.pdf")