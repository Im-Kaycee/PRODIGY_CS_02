from PIL import Image
import numpy as np


def encryption(image_path, key):
    image = Image.open(image_path)

    # Convert image to NumPy array
    data = np.array(image)

    # Apply XOR operation with the key to encrypt the image
    encrypted_data = data ^ key

    # Convert the encrypted data back to an image
    encrypted_image = Image.fromarray(encrypted_data)

    # Save the encrypted image
    encrypted_image.save("encrypted_image.png")
    print("Encryption complete. Encrypted image saved as 'encrypted_image.png'.")



def decryption(encrypted_image_path, key2):
    # Load the encrypted image
    encrypted_image = Image.open(encrypted_image_path)

    # Convert image to NumPy array
    encrypted_data = np.array(encrypted_image)

    # Apply XOR operation with the same key to decrypt the image
    decrypted_data = encrypted_data ^ key2

    # Convert the decrypted data back to an image
    decrypted_image = Image.fromarray(decrypted_data)

    # Save the decrypted image
    decrypted_image.save("decrypted_image.png")
    print("Decryption complete. Decrypted image saved as 'decrypted_image.png'.")


def main():
    image_path = input("enter your image name with the extension")  # Change this to your image file name
    key = 123  # Key for encryption/decryption
    option = input('Do you want to encrypt or decrypt? ').lower()
    if option == 'encrypt':
        encryption(image_path, key)
    # Encrypt the image
    elif option == 'decrypt':
        key2 = int(input('Enter your key'))
        decryption("encrypted_image.png", key2)


if __name__ == "__main__":
    main()
