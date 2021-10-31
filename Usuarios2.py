import pandas as pd
import tkinter.filedialog as fdlg
import sqlite3
import os

sisteminha = os.path.abspath(os.path.dirname(__file__))

class Usuarios(object):
  def relatorios(self,arquivodobanco,tela):
    conexao =""
    try:
      files = os.listdir(arquivodobanco)
      os.chdir(arquivodobanco)
      files_bd =[arquivodobanco + '\\' + f for f in files if f[-2:]== 'db']
      for f in files_bd:
        conexao = sqlite3.connect(f)
      #conexao = sqlite3.connect('banco.db')
      
      df=pd.read_sql_query("""SELECT name FROM sqlite_schema 
      WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%' 
      ORDER BY 1""",conexao)
      for linha in df['name']:
        print(linha)
        df2=pd.read_sql_query("""SELECT * FROM """ + linha,conexao)
        #print(df2)
        #aqui seleciona a pasta a ser colocada o novo arquivo
        opcoes = {}                # as opções são definidas em um dicionário
        opcoes['initialdir'] = ''    # será o diretório atual
        opcoes['parent'] = tela
        opcoes['title'] = 'Local para salvar o relatorio'
        caminhoinicial = fdlg.askdirectory(**opcoes) 
        df2.to_excel(caminhoinicial +'/Relatorio da tabela ' + linha + ' do Banco.xlsx', index=False)
      return "Gerado com sucesso!"
    except conexao.Error as error:
      return "Ocorreu um erro, não gerado!"