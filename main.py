characters = "abcdefghijklmnopqrstuvwxyz"
character_count = len(characters)

# List all our supported characters for the user
print("Supported Characters:\n" + characters + "\n")

def encrypt_character(plaintext, key):
  plain_index = characters.index(plaintext) # index ranges from 0 to 25
  key_index = characters.index(key)

  cipher_code = (key_index + plain_index) % 26

  cipher = characters[cipher_code]

  return cipher


def encrypt(plaintext, key):
  code = ""

  for plain_index, plain_character in enumerate(plaintext):
    key_index = plain_index % len(key)
    key_character = key[key_index]
    
    # encrypt character
    cipher_character = encrypt_character(plain_character, key_character)
    code += cipher_character

  return code


def invert_character(character):
  # mod 26 to turn a back to a
  inverted_index = (26 - characters.index(character)) % 26
  inverted = characters[inverted_index]

  return inverted


def invert(text):
  inverted_text = ""
  
  for character in text:
    inverted_text += invert_character(character=character)

  return inverted_text


def encrypt_or_decrypt(text, key):
  encrypted = text.startswith("!")

  if encrypted:
    ciphertext = text[1:]
    key = invert(key)
    return encrypt(plaintext=ciphertext, key=key)

  if not encrypted:
    ciphertext = "!" + encrypt(plaintext=text, key=key)
    return ciphertext


is_on = True


while is_on:
    print("type '/' to exit.\n")
    text = input("Type the text you'd like to encrypt or decrypt (add an '!' in front if you want to decrypt): ")
    key = input("Encryption key: ")

    try:
      if text == "/":
        is_on = False
      else:
        print(encrypt_or_decrypt(text, key))
    except ValueError:
      print("No spaces or symbols are allowed!")
    
