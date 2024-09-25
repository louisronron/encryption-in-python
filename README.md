
# FYS204 Encryption and Decryption Tutorial

## Part 1: XOR Encryption (Simple Text Key)

### What is Encryption/Decryption?
Encryption is the process of converting readable data (plaintext) into a coded format (ciphertext) to keep it secure from unauthorized access. Decryption is the reverse process, turning the ciphertext back into readable data using a key. Encryption is essential in protecting sensitive information, such as passwords and messages.

### Objective:
Learn to run a simple encryption program using XOR encryption and a passphrase/key.

### Instructions:
1. Go to the GitHub link provided below:  
   **[XOR Encryption Code](https://github.com/louisronron/encryption-in-python/blob/main/simple_xor_encrypt_decrypt.py)**
   
2. Download or copy-paste the code into your Python environment.

3. Run the program and enter the following details when prompted:
   - **Plaintext:** `"This is unit FYS204 at WPU"`
   - **Passphrase/Key:** `"fys204pwd2024"`

4. Observe the encrypted output.

5. Run the program again with:
   - **Plaintext:** `"We are learning cybersecurity"`
   - **Passphrase/Key:** `"fys204pwd2024"`

6. Record your results: Write down both the plaintext and the encrypted text, along with the passphrase or key used.

7. Take a screenshot of your program output.

8. Insert the screenshot into your tutorial document as evidence of completion.

---

## Part 2: Password Hashing with SHA-512 (Step-by-Step)

### What is Hashing?
Hashing is the process of converting any length of data (such as a password) into a fixed-length string of characters, which looks like a random jumble. Hashing is **one-way**, meaning once data is hashed, it cannot be reversed to retrieve the original input. This is why hashing is used to store sensitive data like passwords.

### Objective:
Understand how to hash passwords using the SHA-512 algorithm in Python.

### Instructions:

1. **Step 1: Import the hashlib library.**
   Insert the following line into your Python environment:
   ```python
   import hashlib
   ```

2. **Step 2: Define a function to hash the password.**
   Insert this block of code:
   ```python
   def hash_password_sha512(password):
       sha512_hash = hashlib.sha512(password.encode()).hexdigest()
       return sha512_hash
   ```

3. **Step 3: Start the main function to collect user input.**
   Insert the following:
   ```python
   def main():
       password = input("Enter a new password: ")
   ```

4. **Step 4: Notify the user that hashing is happening.**
   Add this line inside the `main()` function:
   ```python
   print("Hashing the password with SHA-512...")
   ```

5. **Step 5: Hash the password and display the result.**
   Insert the following code:
   ```python
   hashed_password = hash_password_sha512(password)
   print("The hashed password is:", hashed_password)
   ```

6. **Step 6: Notify the user about database storage.**
   Add this line:
   ```python
   print("This is what would be stored in the database.")
   ```

7. **Step 7: Run the main function.**
   Add this block of code to run the program:
   ```python
   if __name__ == "__main__":
       main()
   ```

8. **Step 8: Run the program and take a screenshot.**
   - Run the program and enter a new password when prompted.
   - Observe the hashed password output.
   - Take a screenshot of the program output and insert it into your document as evidence of completion.

---

## Part 3: Exploring Encryption and Hashing Tools

### Objective:
Explore online tools to see encryption, decryption, and hashing in action.

### Instructions:
1. Go to the **[AnyCrypt Tool](https://anycript.com/crypto)**.

2. Spend 30 minutes experimenting with the tool. Enter various plaintexts to see how different algorithms (encryption, decryption, and hashing) work.

3. No specific instructions are provided here; this is your opportunity to explore and familiarize yourself with different encryption and hashing methods.

---
