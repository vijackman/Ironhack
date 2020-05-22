import streamlit as st
import pandas as pd

st.header('Receitas do Jack')

st.write('Por Victor Jackman')

st.write(
    'Esse é um app de receitas, que permite buscar a receita tanto pelo nome da receita quanto por ingredientes aleatórios. Uma das ideias do app é trazer comodidade pro usuario,m ao mesmo tempo que disponibiliza que o cliente busque uma receita pra que algum ingrediente nao estrague no armário ou na geladeira..')

import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm.auto import tqdm
import numpy as np
import re
from time import sleep
import random
from unidecode import unidecode

df = pd.read_csv('../df_Projeto_Final_v1.csv')

count = 0
count_2 = 0
index = []
variavel_2 = 1
ingrediente_1 = 0
busca = st.selectbox('Você quer buscar a receita pelo nome da receita ou por ingrediente ? ',
                     ['Selecione 1 opção', 'Nome da receita', 'Ingrediente'])

if busca == 'Ingrediente':
    ingrediente_1 = st.text_input('Digite o Ingrediente (letras minusculas e sem acentos):')
if ingrediente_1 != 0:
    for i in range(len(df['ingredientes'])):
        if ingrediente_1 in df['ingredientes'][i]:
            count += 1
            index.append(i)
            st.write('Receita ', df.loc[i, 'indice'], ': _-_-_-_-_-_-_-_-_-_-_-_', 'Receita:', df['nome'][i])
    if ingrediente_1 not in df['ingredientes'][i] and count == 0:
        st.write('Não localizei nenhuma receita com esse ingrediente, tente novamente: ')
        st.write('Tente digitar novamente o Ingrediente (letras minusculas e sem acentos): ')
    st.write('Foram encontradas ', count, ' receitas!')
    variavel = int(st.text_input('Selecione uma receita (numero do indice): '))
    if variavel == df['indice'][variavel]:
        st.write('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- Receita ', df.loc[variavel, 'nome'],
                 ': -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
        st.write('Categoria: ', df['categorias'][variavel])
        st.write('Tempo de preparo:', df['tempo_de_preparo_min'][variavel], 'minutos')
        st.write('Tempo de espera:', df['tempo_de_espera_min'][variavel], 'minutos')
        st.write('Tempo de cozimento:', df['tempo_de_cozimento_min'][variavel], 'minutos')
        st.write('Rendimento:', df['rendimento'][variavel])
        st.write('Ingredientes', df['ingredientes'][variavel])
        st.write('Modo de preparo', df['modo de preparo'][variavel])
        mask = ((df['categorias'] == df['categorias'][variavel]) & (df['nome'] != df['nome'][variavel]))
        st.write('Outras receitas que você também pode se interessar: ')
        passo_1 = df[mask]['nome']
        passo_2 = passo_1.sample(3)
        sugestoes = list(passo_2)
        lista_recomendada = list(passo_2.index)
        st.write(lista_recomendada[0], '- _  - _  - _', sugestoes[0])
        st.write(lista_recomendada[1], '- _  - _  - _', sugestoes[1])
        st.write(lista_recomendada[2], '- _  - _  - _', sugestoes[2])
        st.write('Para selecionar uma nova receita, basta colocar o indice no campo de busca acima da receita. ')
    else:
        variavel = int(input('Não localizei esse ingrediente. Tente novamente : '))
elif busca == 'Nome da receita':
    nome_da_receita = (st.text_input('Digite o nome da receita (letras minusculas e sem acento): '))
    for n in range(len(df['ingredientes'])):
        if nome_da_receita in df['nome'][n]:
            count_2 += 1
            index.append(n)
            st.write(' Receita ', df.loc[n, 'indice'], ': _-_-_-_-_-_-_-_-_-_-_-_', 'Receita:', df['nome'][n])
    if nome_da_receita not in df['nome'][n] and count_2 == 0:
        st.write('Não localizei nenhuma receita com esse nome, tente novamente: ')
    st.write('Foram encontradas ', count_2, ' receitas!')
    variavel_2 = int(st.text_input('Selecione uma receita (numero do indice): '))
    if variavel_2 == df['indice'][variavel_2]:
        st.write('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-', 'Receita ', df['nome'][variavel_2],
                 '-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
        st.write('Categoria: ', df['categorias'][variavel_2])
        st.write('Tempo de preparo:', df['tempo_de_preparo_min'][variavel_2], 'minutos')
        st.write('Tempo de espera:', df['tempo_de_espera_min'][variavel_2], 'minutos')
        st.write('Tempo de cozimento:', df['tempo_de_cozimento_min'][variavel_2], 'minutos')
        st.write('Rendimento:', df['rendimento'][variavel_2])
        st.write('Ingredientes', df['ingredientes'][variavel_2])
        st.write('Modo de preparo', df['modo de preparo'][variavel_2])
        mask = ((df['categorias'] == df['categorias'][variavel_2]) & (df['nome'] != df['nome'][variavel_2]))
        st.write(('~ - ' * 8), 'Outras receitas que você também pode se interessar: ', ('~ - ' * 8))
        passo_1 = df[mask]['nome']
        passo_2 = passo_1.sample(3)
        sugestoes = list(passo_2)
        lista_recomendada = list(passo_2.index)
        st.write(lista_recomendada[0], '- _  - _  - _', sugestoes[0])
        st.write(lista_recomendada[1], '- _  - _  - _', sugestoes[1])
        st.write(lista_recomendada[2], '- _  - _  - _', sugestoes[2])
        st.write("Para selecionar uma nova receita, basta colocar o indice no campo de busca acima da receita.")
