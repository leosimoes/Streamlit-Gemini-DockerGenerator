import streamlit as st
from chats import create_chat


class GeminiService:
    def __init__(_self):
        _self._descricao = ''
        _self._is_descricao_valida = False
        _self._docker_compose_code = ''
        _self._dockerfile_code = ''
        _self._chat = create_chat()

    def set_descricao(_self, descricao):
        if _self.verificar_descricao_docker(descricao):
            _self._descricao = descricao
            _self._is_descricao_valida = True
        else:
            _self._descricao = 'None'
            _self._is_descricao_valida = False

    def verificar_descricao_docker(_self, descricao):
        _self._chat.send_message(f'VALIDAR: {descricao}')
        return _self._chat.last.text == 'VALIDA'

    def gerar_docker_compose(_self):
        if _self._is_descricao_valida:
            _self._chat.send_message(f'DOCKERCOMPOSER:{_self._descricao}')
            docker_compose_code = _self._chat.last.text.replace('```dockerfile', '')
            docker_compose_code = docker_compose_code.replace('```', '')
            _self._docker_compose_code = docker_compose_code
        else:
            _self._docker_compose_code = 'None'

    def gerar_dockerfile(_self):
        if _self._is_descricao_valida:
            _self._chat.send_message(f'DOCKERFILE:{_self._descricao}')
            dockerfile_code = _self._chat.last.text
            dockerfile_code = dockerfile_code.replace('```dockerfile', '')
            dockerfile_code = dockerfile_code.replace('```', '')
            _self._dockerfile_code = dockerfile_code
        else:
            _self._dockerfile_code = 'None'

    def get_docker_compose_code(_self):
        return _self._docker_compose_code

    def get_dockerfile_code(_self):
        return _self._dockerfile_code


@st.cache_data
def create_gemini_service():
    return GeminiService()
