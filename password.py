import hashlib
import re
class Password:

    def __init__(self, password):
        self.password = password
        self.is_valid_password(self.password)

    def get(self):
        return hashlib.sha256(self.password.encode()).hexdigest()

    @classmethod
    def is_valid_password(cls, password):
        if len(password) < 8:
            raise ValueError("Длина пароля должна быть не менее 8 символов")
        if not bool(re.search(r'[0-9]', password)):
            raise ValueError("В пароле должны быть цифры")
        if not bool(re.search(r'[a-zA-Z]', password)):
            raise ValueError("В пароле должны быть буквы")
        cls.password = password
        return "пароль валиден"

    @classmethod
    def check(cls, hash1, password):
        return bool(hash1 == hashlib.sha256(password.encode()).hexdigest())


