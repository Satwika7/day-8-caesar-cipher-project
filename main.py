from art import *
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
repeat="Yes"
first_time=True

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
  encryp_word = ""
  for i in range(len(text)):
    if text[i] not in alphabet:
      encryp_word+=text[i]
    else:
      for j in range(26):
  #we can also use .index() function to get the index value of a letter      
        if text[i] == alphabet[j]:
          index = j+shift%26
          if(index>25):
            index-=26
      encryp_word+=alphabet[index]
  print(encryp_word)
  text=encryp_word
def decrypt(text,shift):
  decryp_word = ""
  for i in range(len(text)):
# if they enter space,symbol or number we need to keep them as it is so
    if text[i] not in alphabet:
      decryp_word+=text[i]
    else:
      for j in range(26):
        if text[i] == alphabet[j]:
          index = j-shift%26
          if(index<0):
            index+=26
      decryp_word+=alphabet[index]
  print(decryp_word)
  text=decryp_word
def action(direction,shift):
  if(direction=="encode"):
      encrypt(text,shift)
  elif(direction=="decode"):
      decrypt(text,shift)
  else:
      print("not a valid choice.")
    
while repeat!= "No":
  if not first_time:
    repeat = input("Do you wanna continue 'Yes' or 'No'.")
    if repeat=="Yes":
      print(text)
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      shift = int(input("Type the shift number:\n"))
      action(direction,shift)
    elif repeat=="No":
      repeat="No"
    else:
      print("Invalid entry.")
  else:
    action(direction,shift)
    first_time=False
  
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    
