import ssl, socket
import whois


class NetworkChecker:
	"""Serviço responsável por operações de rede (check SSL e whois).

	Expondo métodos em instância permite sobrescrever em testes (polimorfismo).
	"""
	def check_ssl(self, domain: str) -> bool:
		try:
			ctx = ssl.create_default_context()
			conn = ctx.wrap_socket(socket.socket(), server_hostname=domain)
			conn.settimeout(5)
			conn.connect((domain, 443))
			conn.close()
			return True
		except Exception:
			return False

	def get_whois(self, domain: str):
		try:
			data = whois.whois(domain)
			return {
				"creation": str(data.creation_date),
				"expiration": str(data.expiration_date),
				"registrar": str(data.registrar)
			}
		except Exception:
			return None