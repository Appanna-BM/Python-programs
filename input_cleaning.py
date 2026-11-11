# we use strip() to remove any trailing and leading whitespaces

name = "John"
c_name=name.strip().lower()
print(c_name)

#Removing specific characters in between
#Note : It targets any characters in the passed strings from both ends

url_padding="WWW.example.com"
c_url=url_padding.strip(".W")
print(f"Original url :{url_padding}")
print(f"cleaned url : {c_url}")

#Handling characters in the middle
#Note : strip() only removes from the outer ends , never the middle

sentence = "!!!Hello !!! World !!!"
clean_sentence = sentence.strip("!")
print("Middle character impact :")
print(f"Original : {sentence}")
print(f"cleaned : {clean_sentence}")

#use lstrip() to clean left side and rstrip() to clean rightside
