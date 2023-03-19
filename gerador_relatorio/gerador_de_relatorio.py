import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Título do App
st.markdown('''
# **App de Análise Exploratória**
Esse é um **App AED** criado com Streamlit utilizando a biblioteca **pandas-profiling**.
''')

# Upload CSV
with st.sidebar.header('1. Envie seu arquivo CSV'):
    uploaded_file = st.sidebar.file_uploader("Faça o upload do seu arquivo CSV de input", type=["csv"])
    st.sidebar.markdown("""
[Exemplo de arquivo CSV](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

# Relatório
if uploaded_file is not None:
    @st.cache_resource
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**DataFrame de Entrada**')
    st.write(df)
    st.write('---')
    st.header('**Relatório Pandas Profiling**')
    st_profile_report(pr)
else:
    st.info('Aguarde o Upload do Aqrquivo CSV.')
    if st.button('Pressione para Utilizar o Dataset de Exemplo'):
        # Example data
        @st.cache_resource
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**DataFrame de Entrada**')
        st.write(df)
        st.write('---')
        st.header('**Relatório Pandas Profiling**')
        st_profile_report(pr)