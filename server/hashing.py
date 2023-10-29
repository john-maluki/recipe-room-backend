from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"])


class Hash:
    def bcrypt(password: str):
        return pwd_ctx.hash(password)
