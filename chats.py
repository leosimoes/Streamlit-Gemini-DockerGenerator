import google.generativeai as genai


def read_api_key():
    try:
        with open('GOOGLE_API_KEY.txt', 'r', encoding='utf-8') as arquivo:
            return arquivo.readline()
    except FileNotFoundError:
        return None


def read_primeiro_prompt():
    try:
        with open('primeiro_pompt.txt', 'r', encoding='utf-8') as arquivo:
            return arquivo.readline()
    except FileNotFoundError:
        return 'Retorne apenas "INVALIDA"'


def create_chat():
    genai.configure(api_key=read_api_key())

    generation_config = {
        "temperature": 0,
        "top_p": 1,
        "top_k": 0,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
    ]

    modelo = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    chat = modelo.start_chat(history=[
        {
            "role": "user",
            "parts": [
                "Considere que você é um chatbot que recebe como entrada mensagens que podem ser descrições de conteúdos de aplicações que serão usadas para gerar conteúdo para arquivos Dockerfile e docker-compose.yml.A entrada pode ser iniciada com os seguintes prefixos:- \"VALIDAR:\": neste caso, retorne \"VALIDA\" ou \"INVALIDA\" se a descrição fornecida puder ser usada para gerar conteúdo para Dockerfile e docker-compose.yml.- \"DOCKERFILE:\": gere e retorne apenas o conteúdo de um Dockerfile a partir da descrição fornecida, ou \"None\" se não for possível.- \"DOCKERCOMPOSER:\": gere e retorne apenas o conteúdo de um docker-compose.yml a partir da descrição fornecida, ou \"None\" se não for possível.Outras observações:- Caso a entrada não seja iniciada com um dos três prefixos, retorne \"INVALIDA\".- Caso o prefixo seja \"DOCKERFILE:\" ou \"DOCKERCOMPOSER:\", não retorne nada além de \"None\" ou do conteúdo do arquivo.- Este primeiro prompt deve ser respondido apenas com \"CONFIRMADO\" ou \"REJEITADO\"."]
        },
        {
            "role": "model",
            "parts": ["CONFIRMADO"]
        },
    ])
    return chat
