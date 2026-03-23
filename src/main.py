from implementacaoClasses import (
    Usuario,
    AutenticacaoCelular,
    PortaAutomatizada,
    Camera,
    ServidorLocal,
    SistemaDeAmbiente,
    ControladorDeAcesso,
)


def main():
    usuario = Usuario(1, "Matheus", "Gerente")
    autenticacao = AutenticacaoCelular()
    porta = PortaAutomatizada("Entrada")
    camera = Camera("Recepção")
    servidor = ServidorLocal()
    ambiente = SistemaDeAmbiente()
    controlador = ControladorDeAcesso()

    print(usuario.solicitar_acesso())
    print(camera.reconhecer_usuario(usuario))

    if autenticacao.validar_qrcode("QR-123"):
        print(controlador.liberar_acesso(usuario, porta, "Entrada"))
        print(servidor.registrar_evento("Acesso liberado por QR Code na entrada."))

    print(usuario.emitir_comando_voz("ligar luzes"))
    print(ambiente.ligar_luzes())

    print(usuario.emitir_comando_voz("ligar ar-condicionado"))
    print(ambiente.ligar_ar())

    hora_atual = 20
    if not controlador.validar_horario(hora_atual):
        print(servidor.enviar_notificacao("Movimentação detectada fora do horário comercial."))


if __name__ == "__main__":
    main()
