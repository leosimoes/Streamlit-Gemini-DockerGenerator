import streamlit as st


class GeminiService:
    def __init__(_self):
        _self._descricao = ''
        _self._is_descricao_valida = False
        _self._docker_compose_descricao = ''
        _self._docker_compose_code = ''
        _self._dockerfile_descricao = ''
        _self._dockerfile_code = ''
        # ler api key
        # conectar com gemini
        # inserir primeiro prompt

    def set_descricao(_self, descricao):
        _self._descricao = descricao
        _self._is_descricao_valida = True

    def verificar_descricao_docker(_self):
        return _self._is_descricao_valida

    def gerar_docker_compose(_self):
        if _self._is_descricao_valida:
            _self._docker_compose_descricao = '...'
            _self._docker_compose_code = '...'

    def gerar_dockerfile(_self):
        if _self._is_descricao_valida:
            _self._dockerfile_descricao = '...'
            _self._dockerfile_code = '...'

    def get_docker_compose_descricao(_self):
        return _self._docker_compose_descricao

    def get_docker_compose_code(_self):
        return _self._docker_compose_code

    def get_dockerfile_descricao(_self):
        return _self._dockerfile_descricao

    def get_dockerfile_code(_self):
        return _self._dockerfile_code


@st.cache_data
def create_gemini_service():
    return GeminiService()
