from select_friend import select_friend
from steganography.steganography import Steganography

def read_message():
    # choose friend from the list
    sendr = select_friend()

    encrypted_image = raw_input("Provide encrypted image : C:\Users\GINNI\Desktop\Touch of Purple\New folder\j.JPG")
    secret_message = Steganography.decode(encrypted_image)
    print secret_message