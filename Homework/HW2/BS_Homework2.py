#Go to https://petitions.whitehouse.gov/petitions
#Go to the petition page for each petition
#Create a csv file with the following information for each petition:
# Title
# Published Date
# Issues
# Number of signatures


from bs4 import BeautifulSoup
import urllib2
import csv
import re



web_address='https://petitions.whitehouse.gov/petitions' # Assigns the website of interest to an object
web_page = urllib2.urlopen(web_address) #Uses urllib to open the object that was created
soup = BeautifulSoup(web_page.read())# Parses the website and creates a parsed website
soup.prettify() 

titles = []
publisheddate = []
Issues = []
NoS = []
extensions = []
petitions = []


names=soup.find_all('h3')# since each of the titles are the only text in h3, I am creating an object of all h3 and extracting the text

for i in range(3, 22): # I am creating a for loop to extract the text from each h3.  
	titles.append(names[i].get_text()) # These are then populating a list created for titles
	extensions.append(names[i].find('a')['href'])
	
	
for singlepage in extensions: # Run a loop to extract the individual page of each petition
	petition_address = 'https://petitions.whitehouse.gov%s' % singlepage #assign each individual page will be assigned an object to apply the Beautiful Soup. Once a loop is run this object is over written with the next petition
	petition_page = urllib2.urlopen(petition_address) # The indivudual page is read
	petition_soup = BeautifulSoup(petition_page.read(), "html.parser") # The object is turned to soup
	petitions.append(petition_soup.find("h4", {"class" : "petition-attribution"}).get_text()) # The line on each petition page is added to a list. Where the date will be sorted out.
	
for i in range(0,len(petitions)): # This loop will add the date to the created object published date
	publisheddate.append(petitions[i][19:len(petitions[i])] # Since the format on each page is the same we have each string from the 19th character to the end.  This will extract the date as text
	
	
sigs=soup.find_all("span", {"class" : "signatures-number"})# In the main page "signatures-number is unique to the signatures received. So I created an object with all of these strings.

for i in range(0,len(sigs)): # Since sigs is the string for each number of signatures we need to extract the text, which is the numbers.
	NoS.append((sigs[i].get_text()))
	

kids = soup.find_all('div', {'class' :'field-items'}) # Create an object for all strings on the main page with this classification
for i in range(1, len(kids)): # since the first iteration is not an issue, but an introductory comment, we start on the second item and iterate through the end
	Issues.append((kids[i].get_text())) # Since the only text in this string are the issues we extract just that text


# I am trying to get a better version of the above below, although I am unsure how to do it.
# I know that I need a dictionary to assign each description to each petition. Below is what I have tried


# I have tries the below, but the issue I have is that I cannot get the append part of the loop to add different number of issues to each petition
# I would like to create an empty dictionary and create a new group for each iteration, and add the 'h6' to the proper group, but I am stuck
#  issue_kids = []	
# for i in range(0,len(issue_kids)):	
	# issue_kids.append(kids[i].find_all('h6'))
		
# The below I could not get to work, I kept on receiving this error

#Traceback (most recent call last):
 # File "<stdin>", line 1, in <module>
  #File "/usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7/csv.py", line 141, in writeheader
   # self.writerow(header)
  #File "/usr/local/Cellar/python/2.7.12/Frameworks/Python.framework/Versions/2.7/lib/python2.7/csv.py", line 152, in writerow
    #return self.writer.writerow(self._dict_to_list(rowdict))
#ValueError: I/O operation on closed file

# The information on stack was not helpful.  And I have checked the below against the class files and other labs, and have copied the format exactly, but am still receiving that error.
# Do you know what this error is?

with open('petitions.csv', 'wb') as f:
	my_writer = csv.DictWriter(f, fieldnames=("Title", "Published Date", "Issues", "Number_of_Signatures"))
	my_writer.writeheader()

	for i in range(0, len(titles)):
	my_writer.writerow({"Title" : titles[i], "Published Date" : publisheddate[i], "Number of Signatures" : NoS[i]})
	
	
