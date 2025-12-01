from abc import ABC


class BaseService(ABC):
	pass


class AuthService(BaseService):
	def __init__(self, usuario_repo, security):
		self.usuario_repo = usuario_repo
		self.security = security

	def status(self):
		return "AuthService OK"

	def registrar_usuario(self, nome: str, email: str, senha: str):
		existente = self.usuario_repo.buscar_por_email(email)
		if existente:
			raise ValueError("Email já cadastrado")
		hash_senha = self.security.hash_senha(senha)
		return self.usuario_repo.criar(nome, email, hash_senha)

	def autenticar(self, email: str, senha: str):
		usuario = self.usuario_repo.buscar_por_email(email)
		if not usuario:
			return None
		if not self.security.verificar_senha(senha, usuario.senha_hash):
			return None
		return usuario


# Serviço de site (usa composição para NetworkChecker e repositórios)
class SiteService(BaseService):
	def __init__(self, site_repo, avaliacao_repo, network):
		self.site_repo = site_repo
		self.avaliacao_repo = avaliacao_repo
		self.network = network

	def status(self):
		return "SiteService OK"


	def avaliar_site(self, url: str):
		dominio = url.replace("https://", "").replace("http://", "").split("/")[0]
		ssl_ok = self.network.check_ssl(dominio)
		info = self.network.get_whois(dominio)

		score = 50
		if ssl_ok:
			score += 25
		if info:
			score += 25

		site = self.site_repo.criar(url=url, dominio=dominio)
		avaliacao = self.avaliacao_repo.criar(
			site_id=site.id,
			ssl_valido=ssl_ok,
			dominio_criado_em=info.get("creation") if info else None,
			dominio_expira_em=info.get("expiration") if info else None,
			registrar=info.get("registrar") if info else None,
			indice_confiabilidade=score
		)

		return site, avaliacao


# Serviço de produto: demonstra polimorfismo (poderíamos ter várias estratégias de busca)
class ProdutoService(BaseService):
	def __init__(self):
		pass

	def status(self):
		return "ProdutoService OK"

	def buscar_por_imagem(self, bytes_imagem: bytes):
		# implementação simulada; em uma versão real usaríamos um modelo ML
		return {
			"produto": "Tênis esportivo (IA Simulada)",
			"precos": [
				{"loja": "Amazon", "preco": 199.90},
				{"loja": "Mercado Livre", "preco": 185.50},
				{"loja": "Shopee", "preco": 175.00}
			]
		}