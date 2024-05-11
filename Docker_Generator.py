import streamlit as st
import base64
from services import create_gemini_service

########################################################################################################################
# Configura a página e Inicializa variáveis e constantes
########################################################################################################################
st.set_page_config(page_title='Docker Generator',
                   page_icon=':whale:',
                   layout='centered',
                   initial_sidebar_state='collapsed')

TITULO = 'Docker Generator'
AUTOR = 'Autor: Leonardo Simões'
INTRODUCAO = ('Aplicação Web feita em Python com Streamlit que utiliza o Gemini da Google para criar contéudos para '
              'os arquivos docker-compose.yml e Dockerfile dada uma descrição do sistema desejado.')

is_docker_compose_generated = False
is_dockerfile_generated = False
docker_compose_code = ''
dockerfile_code = ''

gemini_service = create_gemini_service()


def get_botao_de_download(conteudo, nome_arquivo):
    """Gera um link para baixar a string como arquivo"""
    b64 = base64.b64encode(conteudo.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{nome_arquivo}"><button>Baixar {nome_arquivo}</button></a>'


########################################################################################################################
# Exibição da página
########################################################################################################################
with st.container():
    st.title(TITULO)
    st.subheader(AUTOR)
    st.write(INTRODUCAO)

    with st.form('form_docker'):
        columns_checked = st.columns(2)
        with columns_checked[0]:
            is_docker_composer_checked = st.checkbox("Docker Compose")
        with columns_checked[1]:
            is_docker_file_checked = st.checkbox("Dockerfile")
        descricao = st.text_area('Descreva o sistema:', value='')

        if st.form_submit_button('Gerar', use_container_width=True):
            if gemini_service.verificar_descricao_docker(descricao):
                gemini_service.set_descricao(descricao)

                if is_docker_composer_checked:
                    gemini_service.gerar_docker_compose()
                    docker_compose_code = gemini_service.get_docker_compose_code()
                    is_docker_compose_generated = True

                if is_docker_file_checked:
                    gemini_service.gerar_dockerfile()
                    dockerfile_code = gemini_service.get_dockerfile_code()
                    is_dockerfile_generated = True
            else:
                is_docker_compose_generated = False
                is_dockerfile_generated = False
                st.write('A descrição do sistema que foi fornecida não é válida.')

    if is_docker_compose_generated:
        st.divider()
        st.write('### docker-compose.yml:')
        st.code(docker_compose_code, language="yaml")
        st.markdown(get_botao_de_download(docker_compose_code, 'docker-compose.yml'), unsafe_allow_html=True)

    if is_dockerfile_generated:
        st.divider()
        st.write('### Dockerfile:')
        st.code(dockerfile_code, language="dockerfile")
        st.markdown(get_botao_de_download(dockerfile_code, 'Dockerfile'), unsafe_allow_html=True)

    st.divider()
