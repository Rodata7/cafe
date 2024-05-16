import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
import streamlit as st

# Centralizando título e subtítulo com CSS
st.markdown(
    """
    <style>
    .titulo {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='titulo'>Oi Brendoléia!</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='titulo'>Quer tomar café?</h2>", unsafe_allow_html=True)



col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17 = st.columns(15)

# Create a checkbox with a single option
with col10:
    single_option = st.checkbox("Sim")

# Check if the option is selected
    if single_option:
        st.write("Você é legal!")


# Create a checkbox with a single option

    single_option = st.checkbox("Não")

# Check if the option is selected
    if single_option:
        st.write("Sua chata!")




import streamlit as st

# Criar três colunas
col1, col2, = st.columns(2)

# Adicionar conteúdo em cada coluna
with col1:
    VIDEO_URL = "https://www.youtube.com/watch?v=8n14Sasjo3A"
    st.video(VIDEO_URL)

with col2:
    picture = st.camera_input("Faça uma careta")

    if picture:
        st.image(picture)

    st.write("..........................................................              site desenvolvido por Rodrigão Xeirozo              ..........................................................")


# Relógio