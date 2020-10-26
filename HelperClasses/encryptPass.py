from cryptography.fernet import Fernet


class EncryptPasswords:

    def __init__(self, string):
        self.string = string

    def encryptPassword(self):
        b_string = str.encode(self.string)
        key = b'5Zn0_tUZxQows6fwBur2GCo3q_uNm3Q8VuQBHx22BW0='
        cipher_suit = Fernet(key)
        encrypted = cipher_suit.encrypt(b_string)
        str_encrypted = encrypted.decode('utf-8')
        return str_encrypted
