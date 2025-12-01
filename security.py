from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Security:
"""Encapsula hashing e verificação de senhas."""
@staticmethod
def hash_senha(senha: str) -> str:
return pwd_context.hash(senha)


@staticmethod
def verificar_senha(senha: str, hash_salvo: str) -> bool:
return pwd_context.verify(senha, hash_salvo)