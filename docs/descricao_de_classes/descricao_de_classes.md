# Descrição das classes

## Classes principais

### Usuario
Representa quem interage com o sistema. Armazena identificação, nome e perfil de acesso.

### ControladorDeAcesso
Centraliza a validação de perfil, horário e decisão de liberação de acesso.

### ServidorLocal
Mantém o registro de eventos e o envio de notificações, respeitando a restrição de infraestrutura local.

### PortaAutomatizada
Representa cada porta controlada pelo sistema e suas operações básicas de abertura e fechamento.

### AutenticacaoCelular
Modela a autenticação por QR Code e aproximação.

### Camera
Representa as câmeras usadas para reconhecimento e monitoramento.

### SistemaDeAmbiente
Agrupa o controle de luzes e ar-condicionado por comando de voz.

## Regra de conversão de requisitos em classes

Os substantivos relevantes do domínio foram convertidos em classes. Os dados observáveis viraram atributos, e as ações do sistema viraram métodos.
