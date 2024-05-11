import streamlit as st
import base64

########################################################################################################################
# Configura a página e Inicializa variáveis e constantes
########################################################################################################################
st.set_page_config(page_title='Docker Generator',
                   page_icon=':whale:',
                   layout='centered',
                   initial_sidebar_state='collapsed')

TITULO = 'Docker Generator'
AUTOR = 'Autor: Leonardo Simões'
INTRODUCAO = '''
'''

is_docker_compose_generated, is_dockerfile_generated = False, False
docker_compose_code, docker_compose_descricao = '', ''
dockerfile_code, dockerfile_descricao = '', ''


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

            # Checar se a descição é válida
            is_descricao_valida = True

            if is_descricao_valida:
                if is_docker_composer_checked:
                    docker_compose_descricao = '...'
                    docker_compose_code = '...'
                    is_docker_compose_generated = True

                if is_docker_file_checked:
                    dockerfile_descricao = '...'
                    dockerfile_code = '...'
                    is_dockerfile_generated = True
            else:
                is_docker_compose_generated = False
                is_dockerfile_generated = False
                st.write('A descrição do sistema que foi fornecida não é válida.')

    if is_docker_compose_generated:
        st.write(docker_compose_descricao)
        st.code(docker_compose_code)
        st.markdown(get_botao_de_download(docker_compose_code, 'docker-compose.yml'), unsafe_allow_html=True)

    if is_dockerfile_generated:
        st.write(dockerfile_descricao)
        st.code(dockerfile_code)
        st.markdown(get_botao_de_download(dockerfile_code, 'Dockerfile'), unsafe_allow_html=True)
