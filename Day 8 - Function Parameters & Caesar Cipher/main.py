"""
Ceaser Cipher
"""

def ceaser (operation , text,shift):
    result = []
    for letter in text :
        if (operation == "encode"):
            newIndex = (lookupTable.index(letter) + shift) % 26
        else :
             newIndex = (lookupTable.index(letter) - shift) % 26
        result.append(lookupTable[newIndex])
    if (operation == "encode"):
        print(f"The encoded Text is : {"".join(result)}")
    else :
        print(f"The decoded Text is : {"".join(result)}")


while (True):
    lookupTable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    operation = input("Type 'encode' to encrypt , type 'decode' to decrypt: \n").strip().lower()

    message = input("Type your message:\n").strip().lower()

    shift = int(input("Type the shift number:\n"))
    ceaser(operation=operation,text=message, shift=shift)

    if input("Type 'yes' if you want to go Again , Otherwise type 'no : \n" ).strip().lower() != "yes" :
        break


    
# def encrypt (text, shift):
#     result = []
#     for letter in text :
#         newIndex = (lookupTable.index(letter) + shift) % 26
#         result.append(lookupTable[newIndex])

#     print(f"The encoded Text is : {"".join(result)}")

# def decrypt (text, shift):
#     result = []
#     for letter in text :
#         newIndex = (lookupTable.index(letter) - shift ) % 26
#         result.append(lookupTable[newIndex])

#     print(f"The decoded Text is : {"".join(result)}")