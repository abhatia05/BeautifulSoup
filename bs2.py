from bs4 import BeautifulSoup

# let's define a string which is actually a HTML Code text
hello_world = "<p id='id1' class = 'paraclass1 paraclass2' title ='Title Paragraph'>Hello This is a Paragraph</p>"

# define the mark up for BeautifulSoup

#Convert the String to Soup_String
soup_string = BeautifulSoup(hello_world,"lxml")

print(hello_world)  # the string we define which has HTML code.
print(soup_string)  # the string after using Beautiful Soup.

print(soup_string.p) # it will print the whole P tag
print(soup_string.p['id']) #it will print id of the tag
print(soup_string.p['class']) # it will print class of the tag, Remember this is a list.
print(soup_string.p.text) # It will print value of the tag
print(soup_string.p['title']) # it will print title of the tag.


