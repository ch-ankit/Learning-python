#Strings
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name="ada"
last_name="lovelace"
full_name= first_name+ " " + last_name
print("Hello, "+full_name.title()+"!")

#Adding Whitespace to Strings with Tabs or Newlines
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping Whitespace
favorite_language="python "
print(favorite_language)
favorite_language=favorite_language.rstrip()
print(favorite_language.rstrip())

#Exercise
name="  \tEric"
message="Hello "+name.lstrip()+", would you like to learn some Python today?"
print(message)
name= "monty python"
print(name.title())
print(name.upper())
print(name.lower())

quote="'A person who never made a mistake never tried anything new.'"
author="\t\t\t\t\t\t -Albert Einstein"
print(quote)
print(author)

#Numbers
print(2+3)
print(3-2)
print(2*3)
print(3/2)
print(2**3)

#Floats
print(0.1+0.1)
print(0.2+0.2)
print(2*0.1)
print(2*0.2)
print(0.2+0.1)
print(3*0.1)

#Exercise
print(5+3)
print(10-2)
print(4*2)
print(16/2)

favoutite_number=7
print("My favourite number is "+str(favoutite_number))

