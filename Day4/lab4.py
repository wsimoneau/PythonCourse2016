#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
	

from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os


web_address='https://polisci.wustl.edu/faculty/specialization' #Assigns the website of interest to an object
web_page = urllib2.urlopen(web_address) #Opens the webpage object


soup = BeautifulSoup(web_page.read(), 'html.parser')
soup.prettify()

mysection=soup.find_all('strong')

names = []
for individual in mysection:
	names.append(individual.get_text())

subfields=soup.find_all('h3') #Get a list of all subfields

for subfield in subfields:
	for sibling in subfield.next_siblings:# iterate over the siblings of the current subfield
	if sibling in subfields:
		break # if the sibling is one of the subfields, the inner loop is broken
	else:
		print sibling
	
my_a_tab = 	soup.find_all('a')
		
for my_a_tab in mysection:
	print(my_a_tab.get('href'))
	
	
