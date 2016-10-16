from bs4 import BeautifulSoup

# let's define a string which is actually a HTML Code text
hello_world = "<p>Hello This is a Paragraph</p>"

# define the mark up for BeautifulSoup

#Convert the String to Soup_String
soup_string = BeautifulSoup(hello_world,"lxml")

print(hello_world)  # the string we define which has HTML code.
print(soup_string)  # the string after using Beautiful Soup.



