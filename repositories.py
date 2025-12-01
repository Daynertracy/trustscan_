from sqlalchemy.orm import Session
from . import models


# Repositório base (abstração de operações DB)
class BaseRepository:
	def __init__(self, db: Session):
		self.db = db


class UsuarioRepository(BaseRepository):
	def criar(self, nome: str, email: str, senha_hash: str):
		u = models.Usuario(nome=nome, email=email, senha_hash=senha_hash)
		self.db.add(u)
		self.db.commit()
		self.db.refresh(u)
		return u

	def buscar_por_email(self, email: str):
		return self.db.query(models.Usuario).filter_by(email=email).first()


class SiteRepository(BaseRepository):
	def criar(self, url: str, dominio: str):
		s = models.Site(url=url, dominio=dominio)
		self.db.add(s)
		self.db.commit()
		self.db.refresh(s)
		return s

	def listar_todos(self):
		return self.db.query(models.Site).all()


class AvaliacaoRepository(BaseRepository):
	def criar(self, site_id:int, ssl_valido:bool, dominio_criado_em:str, dominio_expira_em:str, registrar:str, indice_confiabilidade:int):
		a = models.AvaliacaoSite(
			site_id=site_id,
			ssl_valido=ssl_valido,
			dominio_criado_em=dominio_criado_em,
			dominio_expira_em=dominio_expira_em,
			registrar=registrar,
			indice_confiabilidade=indice_confiabilidade
		)
		self.db.add(a)
		self.db.commit()
		self.db.refresh(a)
		return a