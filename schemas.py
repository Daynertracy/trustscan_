from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class RegisterRequest(BaseModel):
nome: str
email: EmailStr
senha: str


class LoginRequest(BaseModel):
email: EmailStr
senha: str


class SiteRequest(BaseModel):
url: str


class AvaliacaoOut(BaseModel):
id: int
site_id: int
ssl_valido: Optional[bool]
dominio_criado_em: Optional[str]
dominio_expira_em: Optional[str]
registrar: Optional[str]
indice_confiabilidade: Optional[int]
criado_em: Optional[datetime]


class Config:
orm_mode = True


class SiteOut(BaseModel):
id: int
url: str
dominio: str
criado_em: Optional[datetime]
avaliacoes: List[AvaliacaoOut] = []


class Config:
orm_mode = True