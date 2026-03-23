class Usuario:
    def __init__(self, id_usuario: int, nome: str, perfil: str):
        self.id_usuario = id_usuario
        self.nome = nome
        self.perfil = perfil

    def solicitar_acesso(self):
        return f"{self.nome} solicitou acesso."

    def emitir_comando_voz(self, comando: str):
        return f"{self.nome} emitiu o comando de voz: {comando}."


class AutenticacaoCelular:
    def validar_qrcode(self, codigo: str) -> bool:
        return bool(codigo)

    def validar_aproximacao(self, token: str) -> bool:
        return bool(token)


class PortaAutomatizada:
    def __init__(self, local: str):
        self.local = local
        self.status = "fechada"

    def abrir(self):
        self.status = "aberta"
        return f"Porta de {self.local} aberta."

    def fechar(self):
        self.status = "fechada"
        return f"Porta de {self.local} fechada."


class Camera:
    def __init__(self, local: str):
        self.local = local

    def reconhecer_usuario(self, usuario: Usuario) -> str:
        return f"Usuário reconhecido pela câmera em {self.local}: {usuario.nome}."

    def detectar_movimentacao(self) -> str:
        return f"Movimentação detectada em {self.local}."


class ServidorLocal:
    def registrar_evento(self, evento: str) -> str:
        return f"Evento registrado no servidor local: {evento}"

    def enviar_notificacao(self, mensagem: str) -> str:
        return f"Notificação enviada: {mensagem}"


class SistemaDeAmbiente:
    def __init__(self):
        self.status_luzes = "desligadas"
        self.status_ar = "desligado"

    def ligar_luzes(self):
        self.status_luzes = "ligadas"
        return "Luzes ligadas."

    def desligar_luzes(self):
        self.status_luzes = "desligadas"
        return "Luzes desligadas."

    def ligar_ar(self):
        self.status_ar = "ligado"
        return "Ar-condicionado ligado."

    def desligar_ar(self):
        self.status_ar = "desligado"
        return "Ar-condicionado desligado."


class ControladorDeAcesso:
    def __init__(self, horario_inicial: int = 8, horario_final: int = 18):
        self.horario_inicial = horario_inicial
        self.horario_final = horario_final

    def validar_perfil(self, usuario: Usuario, area: str) -> bool:
        regras = {
            "RH": {"RH"},
            "Gerencia": {"Gerente", "RH"},
            "Entrada": {"Gestora", "Funcionário", "RH", "Gerente", "PCD"},
        }
        return usuario.perfil in regras.get(area, set())

    def validar_horario(self, hora_atual: int) -> bool:
        return self.horario_inicial <= hora_atual <= self.horario_final

    def liberar_acesso(self, usuario: Usuario, porta: PortaAutomatizada, area: str) -> str:
        if self.validar_perfil(usuario, area):
            return porta.abrir()
        return f"Acesso negado para {usuario.nome} na área {area}."
