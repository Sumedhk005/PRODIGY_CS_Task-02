from PIL import Image
import numpy as np

# Function to encrypt an image by modifying pixel values
def encrypt_image(image_path, shift_value, output_path):

    img = Image.open(image_path)
    img_array = np.array(img)

    
    encrypted_array = np.mod(img_array + shift_value, 255)

    encrypted_img = Image.fromarray(np.uint8(encrypted_array))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt an image by reversing the pixel manipulation
def decrypt_image(encrypted_path, shift_value, output_path):
   
    img = Image.open(encrypted_path)
    img_array = np.array(img)

    
    decrypted_array = np.mod(img_array - shift_value, 255)

    
    decrypted_img = Image.fromarray(np.uint8(decrypted_array))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Main function to handle user input
def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt an image? ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice! Please select 'E' for encryption or 'D' for decryption.")
        return

    image_path = input("Enter the path of the image: ")
    shift_value = int(input("Enter the shift value (e.g., 50): "))
    output_path = input("Enter the output image path: ")

    if choice == 'E':
        encrypt_image(image_path, shift_value, output_path)
    elif choice == 'D':
        decrypt_image(image_path, shift_value, output_path)

if __name__ == "__main__":
    main()
