from urllib.request import urlopen
from bs4 import BeautifulSoup
# -----------------------------------------------------------------
# "politics"

# html = urlopen('https://ria.ru/politics/').read()
# soup = BeautifulSoup(html, 'html.parser')
# title = soup.title.string
# div = soup.find('div', attrs={'class':'b-list'})
# f = []
# for row in div.find_all('div'):
# 	cols = row.find_all('a')
# 	if cols:
# 		f.append(cols)
# for i in range(len(f)):
# 	try:
# 		link = f[i][0]['href']
# 		print("link: {}".format(link))
# 	except:
# 		pass
# 	try:	
# 		title = f[i][0].contents[1].contents[0].string
# 		print("title: {}".format(title))
# 	except:
# 		pass
# 	try:
# 		image = f[i][0].contents[0].contents[0].contents[0]['src']
# 		print("image: {}".format(image))
# 	except:
# 		pass
# ------------------------------------------------------------------------

# --------------------------------------------------------------------------
# "sports"
# html = urlopen('https://rsport.ria.ru/football/').read()
# soup = BeautifulSoup(html, 'html.parser')
# div = soup.find('ul', attrs={'class':'b-list__list'})
# f = []
# t = []
# for row in div.find_all('div', attrs={'class':'b-list__item-img'}):
# 	cols = row.find_all('a')
# 	if cols:
# 		f.append(cols)
# for wor in div.find_all('div', attrs={'class':'b-list__item-body'}):
# 	titl = wor.find_all('h2', attrs={'class':'b-list__item-title'})
# 	if titl:
# 		t.append(titl)

# for i in range(len(t)):
# 	try:
# 		link = f[i][0]['href']
# 		print("link: {}".format(link))
# 	except:
# 		pass
# 	try:	
# 		title = t[i][0].string
# 		print("title: {}".format(title))
# 	except:
# 		pass
# 	try:
# 		image = f[i][0].contents[0]['src']
# 		print("image: {}".format(image))
# 	except:
# 		pass
# ---------------------------------------------------------------------------


# @shared_task
	# def get_sports_from_ria_ru
	# 	html = urlopen('https://rsport.ria.ru/football/').read()
	# 	soup = BeautifulSoup(html, 'html.parser')
	# 	div = soup.find('ul', attrs={'class':'b-list__list'})
	# 	z = []
	# 	t = []
	# 	for row in div.find_all('div', attrs={'class':'b-list__item-img'}):
	# 		cols = row.find_all('a')
	# 		if cols:
	# 			f.append(z)
	# 	for wor in div.find_all('div', attrs={'class':'b-list__item-body'}):
	# 		titl = wor.find_all('h2', attrs={'class':'b-list__item-title'})
	# 		if titl:
	# 			t.append(titl)

	# 	for i in range(len(t)):
	# 		linksport = None
	# 		titlesport = None
	# 		imagesport = None

	# 		try:
	# 			linksport = z[i][0]['href']
	# 		except:
	# 			pass
	# 		try:	
	# 			titlesport = t[i][0].string
	# 		except:
	# 			pass
	# 		try:
	# 			imagesport = z[i][0].contents[0]['src']
	# 		except:
	# 			pass

	# 		if linksport and titlesport and imagesport:
	# 			if not Sport.objects.filter(titlesport=titlesport).exists():
	# 				Sport.objects.create(link=z'https://ria.ru{linksport}', titlesport=titlesport, imagesport=imagesport, sourcesport='Ria.ru')

# ------------------------------------------------------------------------------------------------------------
# 'world'

# html = urlopen('https://ria.ru/world/').read()
# soup = BeautifulSoup(html, 'html.parser')
# title = soup.title.string
# div = soup.find('div', attrs={'class':'b-list'})
# f = []
# for row in div.find_all('div'):
# 	cols = row.find_all('a')
# 	if cols:
# 		f.append(cols)
# for i in range(len(f)):
# 	try:
# 		link = f[i][0]['href']
# 		print("link: {}".format(link))
# 	except:
# 		pass
# 	try:	
# 		title = f[i][0].contents[1].contents[0].string
# 		print("title: {}".format(title))
# 	except:
# 		pass
# 	try:
# 		image = f[i][0].contents[0].contents[0].contents[0]['src']
# 		print("image: {}".format(image))
# 	except:
# 		pass

#---------------------------------------------------------------------------------------------------



# 'insident'

# html = urlopen(https://ria.ru/incidents/).read()
# soup = BeautifulSoup(html, 'html.parser')
# title = soup.title.string
# div = soup.find('div', attrs={'class':'b-list'})
# f = []
# for row in div.find_all('div'):
# 	cols = row.find_all('a')
# 	if cols:
# 		f.append(cols)
# for i in range(len(f)):
# 	try:
# 		link = f[i][0]['href']
# 		print("link: {}".format(link))
# 	except:
# 		pass
# 	try:	
# 		title = f[i][0].contents[1].contents[0].string
# 		print("title: {}".format(title))
# 	except:
# 		pass
# 	try:
# 		image = f[i][0].contents[0].contents[0].contents[0]['src']
# 		print("image: {}".format(image))
# 	except:
# 		pass

















