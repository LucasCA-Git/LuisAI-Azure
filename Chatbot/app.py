import os
from dotenv import load_dotenv
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurações do LUIS obtidas do .env
APP_ID = os.getenv("APP_ID")
PREDICTION_KEY = os.getenv("PREDICTION_KEY")
ENDPOINT = os.getenv("ENDPOINT")

# Inicializa o cliente LUIS
client = LUISRuntimeClient(endpoint=ENDPOINT, credentials=CognitiveServicesCredentials(PREDICTION_KEY))

def obter_intencao(mensagem):
    response = client.prediction.resolve(APP_ID, query=mensagem)
    intent = response.top_scoring_intent.intent
    entities = [(e.entity, e.type) for e in response.entities]
    return intent, entities

# Teste do chatbot
if __name__ == "__main__":
    print("Digite sua mensagem (ou 'sair' para encerrar):")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break
        intent, entities = obter_intencao(user_input)
        print(f"Intenção: {intent}")
        print(f"Entidades: {entities}")
