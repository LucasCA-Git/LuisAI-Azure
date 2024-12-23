import os
import logging
from dotenv import load_dotenv
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

# Configuração do logging para arquivo
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "logChatbot.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()  # Também exibe logs no console
    ]
)
logger = logging.getLogger(__name__)

# Carrega as variáveis do .env
if load_dotenv():
    logger.info("Variáveis de ambiente carregadas com sucesso.")
else:
    logger.error("Erro ao carregar as variáveis de ambiente. Verifique o arquivo .env.")

# Configurações do LUIS obtidas do .env
APP_ID = os.getenv("APP_ID")
PREDICTION_KEY = os.getenv("PREDICTION_KEY")
ENDPOINT = os.getenv("ENDPOINT")

if not all([APP_ID, PREDICTION_KEY, ENDPOINT]):
    logger.critical("Uma ou mais variáveis do .env não foram encontradas. Verifique o arquivo .env.")
    exit(1)

# Inicializa o cliente LUIS
try:
    client = LUISRuntimeClient(endpoint=ENDPOINT, credentials=CognitiveServicesCredentials(PREDICTION_KEY))
    logger.info("Cliente LUIS inicializado com sucesso.")
except Exception as e:
    logger.critical(f"Erro ao inicializar o cliente LUIS: {e}")
    exit(1)

# Função para obter intenção e entidades
def obter_intencao(mensagem):
    try:
        response = client.prediction.resolve(APP_ID, query=mensagem)
        intent = response.top_scoring_intent.intent
        entities = [(e.entity, e.type) for e in response.entities]
        logger.info(f"Mensagem processada com sucesso. Intenção: {intent}, Entidades: {entities}")
        return intent, entities
    except Exception as e:
        logger.error(f"Erro ao processar a mensagem no LUIS: {e}")
        return "Erro", []

# Chatbot principal
if __name__ == "__main__":
    logger.info("Chatbot iniciado. Digite sua mensagem ou 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            logger.info("Chatbot encerrado pelo usuário.")
            break
        intent, entities = obter_intencao(user_input)
        print(f"Intenção: {intent}")
        print(f"Entidades: {entities}")
