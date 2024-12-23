# **Chatbot com Azure LUIS**

Este é um projeto de um chatbot simples baseado em **Python** que utiliza o **Azure LUIS (Language Understanding Intelligent Service)** para identificar intenções e extrair entidades de mensagens fornecidas pelos usuários.

---

## **Descrição do Projeto**

O chatbot é projetado para interpretar mensagens e identificar a intenção do usuário com base em um modelo treinado no Azure LUIS. Ele exibe a intenção identificada, bem como as entidades detectadas, e registra todas as interações em um arquivo de log.

### **Como Funciona**

1. O chatbot recebe uma mensagem de texto do usuário.  
2. A mensagem é enviada para o serviço **LUIS**, que retorna:  
   * A intenção principal (intent).  
   * Entidades relevantes extraídas da mensagem.  
3. As informações são exibidas ao usuário e registradas em um arquivo de log.

---

<div align="center">

## **Tecnologias Utilizadas** 

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Azure](https://img.shields.io/badge/Azure-0089D6?style=flat&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![dotenv](https://img.shields.io/badge/dotenv-2E7D32?style=flat&logo=envoy&logoColor=white)](https://github.com/motdotla/dotenv)
[![Logging](https://img.shields.io/badge/Logging-FFD700?style=flat&logo=logstash&logoColor=white)](https://www.elastic.co/logstash)

</div>



## **Configuração**

### **Pré-requisitos**

1. **Conta no Azure com LUIS habilitado.**  
2. **Python 3.8 ou superior.**

### **README.md: Chatbot com Azure LUIS**

# **Chatbot com Azure LUIS**

Este é um projeto de um chatbot simples baseado em **Python** que utiliza o **Azure LUIS (Language Understanding Intelligent Service)** para identificar intenções e extrair entidades de mensagens fornecidas pelos usuários.

---

## **Descrição do Projeto**

O chatbot é projetado para interpretar mensagens e identificar a intenção do usuário com base em um modelo treinado no Azure LUIS. Ele exibe a intenção identificada, bem como as entidades detectadas, e registra todas as interações em um arquivo de log.

### **Como Funciona**

1. O chatbot recebe uma mensagem de texto do usuário.  
2. A mensagem é enviada para o serviço **LUIS**, que retorna:  
   * A intenção principal (intent).  
   * Entidades relevantes extraídas da mensagem.  
3. As informações são exibidas ao usuário e registradas em um arquivo de log.

---

## **Tecnologias Utilizadas**

* **Python**: Linguagem de programação principal.  
* **Azure LUIS**: Serviço de análise de linguagem natural.  
* **dotenv**: Gerenciamento de variáveis de ambiente.  
* **Logging**: Registro de eventos para depuração e monitoramento.

---

---

## **Configuração**

### **Pré-requisitos**

1. **Conta no Azure com LUIS habilitado.**  
2. **Python 3.8 ou superior.**

### **Instalação**

1. Instale as dependências: 
- dentro da pasta .Chatbot/ 
```bash  
pip install -r requirements.txt`
```
2. Configure as variáveis de ambiente no arquivo `.env` na raiz do projeto:  
```js
APP_ID=seu-app-id-aqui
PREDICTION_KEY=sua-chave-de-api-aqui
ENDPOINT=seu-endpoint-aqui
```
---

## **Uso**

Execute o script principal:  
```bash  
python app.py
```
1. Digite uma mensagem para o chatbot. Por exemplo:  
```bash
Você: Qual será o tempo amanhã?
```
- O chatbot responderá com a intenção identificada e as entidades extraídas.  
- Para encerrar, digite `sair`.

---

## **Arquitetura do Código**

### **`app.py`**

1. **Configuração do Log:**  
   * O sistema registra eventos no arquivo `logs/logChatbot.log`.  
   * Mensagens de erro, sucesso e interações são armazenadas.  
2. **Integração com LUIS:**  
   * O cliente LUIS é inicializado usando as configurações do `.env`.  
   * A função `obter_intencao` processa mensagens no LUIS e retorna as intenções e entidades.  
3. **Chatbot Principal:**  
   * Um loop processa mensagens do usuário e exibe os resultados.

---

### **Explicação do Código `app.py`**

O arquivo `app.py` é o código principal do chatbot. Ele integra o Azure LUIS com o Python, gerencia as entradas do usuário e registra as interações em um arquivo de log. Vamos explorar as principais partes do código:

#### **1\. Configuração de Logging**

```python  
 
`LOG_DIR = "logs"`  
`LOG_FILE = os.path.join(LOG_DIR, "logChatbot.log")`  
`os.makedirs(LOG_DIR, exist_ok=True)`

`logging.basicConfig(`  
    `level=logging.INFO,`  
    `format="%(asctime)s - %(levelname)s - %(message)s",`  
    `handlers=[`  
        `logging.FileHandler(LOG_FILE, encoding="utf-8"),`  
        `logging.StreamHandler()  # Também exibe logs no console`  
    `]`  
`)`  
`logger = logging.getLogger(__name__)`
```
* **Objetivo**: Configura o sistema de logging.  
* **Detalhes**:  
  * O código cria um diretório `logs` para armazenar os arquivos de log, caso ele não exista.  
  * O arquivo de log `logChatbot.log` é gerado dentro dessa pasta, e ele registra todas as mensagens (info, erro, etc.).  
  * O logging também exibe mensagens no console enquanto o chatbot está sendo executado.
#### **2\. Carregamento de Variáveis de Ambiente**

```python  
`if load_dotenv():`  
    `logger.info("Variáveis de ambiente carregadas com sucesso.")`  
`else:`  
    `logger.error("Erro ao carregar as variáveis de ambiente. Verifique o arquivo .env.")`
```
* **Objetivo**: Carregar variáveis de ambiente a partir do arquivo `.env`.  
* **Detalhes**: O arquivo `.env` contém configurações sensíveis, como o **APP\_ID**, **PREDICTION\_KEY** e **ENDPOINT** do serviço LUIS. O código usa a biblioteca `python-dotenv` para carregar essas variáveis.

#### **3\. Verificação das Variáveis de Ambiente**

```python  
`APP_ID = os.getenv("APP_ID")`  
`PREDICTION_KEY = os.getenv("PREDICTION_KEY")`  
`ENDPOINT = os.getenv("ENDPOINT")`

`if not all([APP_ID, PREDICTION_KEY, ENDPOINT]):`  
    `logger.critical("Uma ou mais variáveis do .env não foram encontradas. Verifique o arquivo .env.")`  
    `exit(1)`
```
* **Objetivo**: Garantir que todas as variáveis de ambiente estejam presentes.  
* **Detalhes**: Se qualquer uma das variáveis estiver faltando, o sistema registra um erro crítico e encerra a execução.

#### **4\. Inicialização do Cliente LUIS**

```python  

`try:`  
    `client = LUISRuntimeClient(endpoint=ENDPOINT, credentials=CognitiveServicesCredentials(PREDICTION_KEY))`  
    `logger.info("Cliente LUIS inicializado com sucesso.")`  
`except Exception as e:`  
    `logger.critical(f"Erro ao inicializar o cliente LUIS: {e}")`  
    `exit(1)`
```
* **Objetivo**: Conectar ao serviço LUIS usando as credenciais fornecidas.  
* **Detalhes**: O cliente LUIS é inicializado com o **endpoint** e a **chave de API** fornecidos. Se ocorrer algum erro na inicialização, o sistema registra o erro e termina a execução.

#### **5\. Função para Obter Intenção e Entidades**

```python  
`def obter_intencao(mensagem):`  
    `try:`  
        `response = client.prediction.resolve(APP_ID, query=mensagem)`  
        `intent = response.top_scoring_intent.intent`  
        `entities = [(e.entity, e.type) for e in response.entities]`  
        `logger.info(f"Mensagem processada com sucesso. Intenção: {intent}, Entidades: {entities}")`  
        `return intent, entities`  
    `except Exception as e:`  
        `logger.error(f"Erro ao processar a mensagem no LUIS: {e}")`  
        `return "Erro", []`
```
* **Objetivo**: Enviar uma mensagem para o LUIS e obter a intenção e as entidades.  
* **Detalhes**:  
  * A mensagem do usuário é enviada para o modelo LUIS usando o método `resolve()`.  
  * A intenção principal e as entidades são extraídas da resposta.  
  * O sistema registra as intenções e entidades obtidas ou um erro, se ocorrer.

#### **6\. Chatbot Principal**

```python  
`if __name__ == "__main__":`  
    `logger.info("Chatbot iniciado. Digite sua mensagem ou 'sair' para encerrar.")`  
    `while True:`  
        `user_input = input("Você: ")`  
        `if user_input.lower() == "sair":`  
            `logger.info("Chatbot encerrado pelo usuário.")`  
            `break`  
        `intent, entities = obter_intencao(user_input)`  
        `print(f"Intenção: {intent}")`  
        `print(f"Entidades: {entities}")`
```
* **Objetivo**: Controlar a interação com o usuário.  
* **Detalhes**:  
  * O código entra em um loop onde o chatbot aguarda a entrada do usuário.  
  * O chatbot usa a função `obter_intencao` para processar a entrada e retorna a intenção e as entidades.  
  * O usuário pode digitar "sair" para encerrar a interação.

## **Azure LUIS**

### **O que é?**

O **Language Understanding Intelligent Service (LUIS)** é uma API de inteligência artificial da Microsoft que usa processamento de linguagem natural (NLP) para identificar intenções e extrair informações de mensagens em linguagem natural.

### **Como o LUIS Responde?**

* **Base de Respostas:** O chatbot responde com base nas intenções detectadas pelo LUIS.  
  * **Exemplo:** Uma intenção chamada `Greeting` pode indicar uma saudação, como "Olá\!".  
* O sistema pode ser expandido para incluir respostas predefinidas em um arquivo JSON (opcional).

## **Logs**

Todos os eventos, sucessos e erros são registrados no arquivo:  
```bash  
logs/logChatbot.log

* 

**Exemplo de Log:**  

2024-12-23 10:30:00 - INFO - Cliente LUIS inicializado com sucesso.
2024-12-23 10:31:00 - INFO - Mensagem processada com sucesso. Intenção: WeatherQuery, Entidades: [('tempo', 'consulta')]`

* 
```
## **Licença** 📝

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

