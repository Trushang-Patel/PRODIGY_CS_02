from PIL import Image
import os

def encrypt_image(image_path, output_path, key=100):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        pixels = img.load()

        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r + key) % 256,
                    (g + key) % 256,
                    (b + key) % 256
                )
        img.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
    except Exception as e:
        print("Error encrypting image:", e)

def decrypt_image(image_path, output_path, key=100):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        pixels = img.load()

        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                pixels[x, y] = (
                    (r - key) % 256,
                    (g - key) % 256,
                    (b - key) % 256
                )
        img.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
    except Exception as e:
        print("Error decrypting image:", e)

def main():
    print("=== Image Encryption Tool ===")
    choice = input("Choose operation (encrypt/decrypt): ").strip().lower()
    image_path = input("Enter path to image: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        key = int(input("Enter encryption/decryption key (integer): "))
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return

    if choice == "encrypt":
        encrypt_image(image_path, output_path, key)
    elif choice == "decrypt":
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid operation selected. Choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
