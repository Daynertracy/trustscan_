from sqlalchemy import Column, Integer, String, Text, Boolean, Numeric, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Usuario(Base):
	__tablename__ = "usuarios"
	id = Column(Integer, primary_key=True, index=True)
	nome = Column(String(150))
	email = Column(String(200), unique=True, index=True)
	senha_hash = Column(String)
	criado_em = Column(TIMESTAMP, default=datetime.utcnow)


class Site(Base):
	__tablename__ = "sites"
	id = Column(Integer, primary_key=True, index=True)
	url = Column(String, nullable=False)
	dominio = Column(String, nullable=False)
	criado_em = Column(TIMESTAMP, default=datetime.utcnow)

	avaliacoes = relationship("AvaliacaoSite", back_populates="site")


class AvaliacaoSite(Base):
	__tablename__ = "avaliacoes_site"
	id = Column(Integer, primary_key=True, index=True)
	site_id = Column(Integer, ForeignKey("sites.id"))
	ssl_valido = Column(Boolean)
	dominio_criado_em = Column(String)
	dominio_expira_em = Column(String)
	registrar = Column(String)
	indice_confiabilidade = Column(Integer)
	criado_em = Column(TIMESTAMP, default=datetime.utcnow)

	site = relationship("Site", back_populates="avaliacoes")


class Produto(Base):
	__tablename__ = "produtos"
	id = Column(Integer, primary_key=True)
	nome = Column(String)
	descricao = Column(Text)
	criado_em = Column(TIMESTAMP, default=datetime.utcnow)

	precos = relationship("PrecoProduto", back_populates="produto")


class PrecoProduto(Base):
	__tablename__ = "precos_produto"
	id = Column(Integer, primary_key=True)
	produto_id = Column(Integer, ForeignKey("produtos.id"))
	loja = Column(String)
	preco = Column(Numeric(10, 2))
	atualizado_em = Column(TIMESTAMP, default=datetime.utcnow)

	produto = relationship("Produto", back_populates="precos")