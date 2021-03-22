from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA3_512, SHA1, SHA512
from Crypto.Protocol.KDF import PBKDF2

# ---------------------
# AES and PKCS7 padding
# ---------------------

# Generate random bytes
key = get_random_bytes(32)
iv = get_random_bytes(16)

# Encrypt
data = b'Unaligned'
cipher1 = AES.new(key, AES.MODE_CBC, iv)
pad_data = pad(data, 16, style="pkcs7")
enc = cipher1.encrypt(pad_data)

# Decrypt
cipher2 = AES.new(key, AES.MODE_CBC, iv)
dec = cipher2.decrypt(enc)
unpad_data = unpad(dec, 16, style="pkcs7")

# Encrypt a file
def sym_encrypt_file(input_file, output_file, cipher, buffer_size=4096):
    pad_done = False
    while True:
        clear = input_file.read(buffer_size)

        if not clear:
            break

        # if the length of the data is less than buffer_size, it means
        # that we're at the end of the file -> the last data must be padded
        if len(clear) < buffer_size:
            pad_data = pad(clear, 16, style="pkcs7")
            enc = cipher.encrypt(pad_data)
            output_file.write(enc)
            pad_done = True
            break
        else:
            enc = cipher.encrypt(clear)
            output_file.write(enc)

    # if the pad is not done yet, it's because the last data was exactly
    # the size of buffer_size, therefore it was impossible to know if
    # other data could be read or not
    if not pad_done:
        pad_data = pad(b'', 16, style="pkcs7")
        enc = cipher.encrypt(pad_data)
        output_file.write(enc)

# Decrypt a file
def sym_decrypt_file(input_file, output_file, cipher, buffer_size=4096):
    backup = None
    while True:
        enc = input_file.read(buffer_size)

        if not enc:
            # if no more data can be read and if the last buffer is
            # stored, it means that the last data was exactly the size
            # of buffer_size -> unpad
            if backup:
                unpad_data = unpad(backup, 16, style="pkcs7")
                output_file.write(unpad_data)
            break
        else:
            # if the last buffer is stored, write it to the file
            if backup:
                output_file.write(backup)
                backup = None

        dec = cipher.decrypt(enc)

        # if the length of the data is less than buffer_size, it means
        # that we're at the end of the file -> unpad
        if len(dec) < buffer_size:
            unpad_data = unpad(dec, 16, style="pkcs7")
            output_file.write(unpad_data)
            break
        else:
            # make a backup of the last buffer because we cannot know
            # if it was the last data of the file
            backup = dec[:]

# ---
# RSA
# ---

# Generate key
rsa_key = RSA.generate(2048)

# Export PEM pkcs8
encrypted_key = rsa_key.export_key(passphrase="test1234", pkcs=8, protection="scryptAndAES256-CBC")
with open("my_key.pem", "wb") as file:
    file.write(encrypted_key)

# Import PEM
def rsa_from_pem(pem_path, passphrase=None):
    with open(pem_path, "rb") as file:
        key_content = file.read()
    if passphrase:
        return RSA.import_key(key_content, passphrase=passphrase)
    return RSA.import_key(key_content)

# Encrypt data
cipher_rsa = PKCS1_OAEP.new(rsa_key)
enc = cipher_rsa.encrypt(b'This is a secret message !')

# Decrypt data
dec = cipher_rsa.decrypt(enc)

# ----
# Hash
# ----

sha3 = SHA3_512.new()
sha3.update(b'this is a test')
hash = sha3.digest()

def hash_sha1(input_file_path):
    hasher = SHA1.new()

    with open(input_file_path, "rb") as file:
        while True:
            buffer = file.read(4096)
            if not buffer:
                break
            hasher.update(buffer)
    return hasher.digest()

# ------
# PBKDF2
# ------

salt = get_random_bytes(64)
key = PBKDF2("test1234", salt, 32, count=10000, hmac_hash_module=SHA1)
print(key)

s = ''