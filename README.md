☔Rain Alert Bot

Este é um projeto em Python que verifica a previsão do tempo para as próximas horas utilizando a API do OpenWeatherMap e, caso haja previsão de chuva, envia um SMS por meio da API do Twilio alertando o usuário para levar um guarda-chuva.

🔐 Segurança com Variáveis de Ambiente
Para proteger dados sensíveis (como tokens de API e credenciais de serviços), este projeto utiliza variáveis de ambiente. Isso evita que essas informações fiquem expostas diretamente no código-fonte.

As seguintes variáveis devem ser configuradas:

TOKEN_API – chave de API do OpenWeatherMap
ACCOUNT – SID da conta Twilio
TOKEN_AUTH – token de autenticação da API Twilio

🔧 Tecnologias Utilizadas
Python 3

OpenWeatherMap API – Para obter dados meteorológicos.

Twilio API – Para envio de mensagens SMS.

dotenv (opcional) – Para carregamento automático de variáveis de ambiente.

🚀 Como Funciona
O script consulta a API do OpenWeatherMap para obter as próximas previsões de tempo.

Analisa se há previsão de chuva (código de condição < 700).

Caso positivo, envia um alerta SMS ao usuário usando a API do Twilio.

🗺️ Parâmetros de Localização
Por padrão, o script usa:

"lat": "-20.336840",
"lon": "-40.291931"

Você pode alterar para as coordenadas da sua cidade.
