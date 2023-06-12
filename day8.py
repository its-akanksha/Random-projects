alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(t, s):
  encrypted_text=[]
  for letter in t:
    if letter==" ":
      encrypted_text.append(" ")
      continue
    i=alphabet.index(letter)
    # print(i)
    new_index=i+s
    # print(new_index)
    if new_index>=25:
      new_index=new_index-26
    letter=alphabet[new_index]
    encrypted_text.append(letter)
    # print(letter)
    # letter+=encrypted_text
  print(f"The endcoded text is {''.join(encrypted_text)}")




#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     if new_position<=0:
#       new_position = 26 - shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The decoded text is {cipher_text}")
def decrypt(t, s):
  decrypted_text=[]
  for letter in t:
    if letter==" ":
      decrypted_text.append(" ")
      continue
    i=alphabet.index(letter)
    # print(i)
    new_index=i-s
    # print(new_index)
    if new_index<=0:
      new_index=(26-s)+i
    letter=alphabet[new_index]
    decrypted_text.append(letter)
    # print(letter)
    # letter+=encrypted_text
  print(f"The decoded text is {''.join(decrypted_text)}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction=="encode":
  encrypt(t=text, s=shift)
elif direction=="decode":
  decrypt(t=text, s=shift)
