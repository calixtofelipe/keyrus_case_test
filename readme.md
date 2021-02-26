# OBJETIVO
Test Case
Escolha o case que tiver mais interesse e que melhor possa demonstrar seu conhecimento na tecnologia, o ambiente que usará pode ser qualquer um, On Premise ou cloud, o objetivo é avaliar o script final. Adote boas práticas de programação e Design Pattern se houver necessidade.

Case 1
Criar função que consome dados de um ftp em Spark. O Download do arquivo deve ser um .zip e descompactar em data frame para salvar em ambiente.

Case 2  
Criar um data frame com transações por municípios e data de atualização.

Considerando o data frame agrupar por município e considerando a data de atualização definir a ordem da transação.

Exemplo de schema:
Transação, Município, Estado e Data de atualização

O data frame final precisa conter um campo ordenando as transações por município
Transação, Município, Estado, data de Atualização e Ordem da Transação

Obs. Alimentar o data frame com mais de uma transação por município e mais de um município, mas não precisa ser um grande volume.
O objetivo é avaliar a lógica da solução e a organização do código em PySpark.

### CONFIGURAÇÕES
- As variáveis de acesso foram colocadas em um arquivo config.py que por segurança estão no .gitignore
exemplo de arquivo:
FTP_URL = "192.168.0.228"
FTP_USER = "fxxxx"
FTP_PASSWORD = "xxxxx"
FTP_FOLDER = "/home/fsociety/projetos/python/keyrus/xxx"
FTP_FILE = "data_municipio.zip"
FTP_DATASOURCE = "ftp://user:senha@192.168.0.228"

### CASE 1 
- Foi feito on premisse
Verificar notebook CASE_1.ipynb
- Observações: 
- Fiz duas possibilidades:
- PRIMEIRA
1 - descompacta e salva o arquivo descompactado.
2 - ler o arquivo descompactado
3 - salva o arquivo descompactado no database.
- SEGUNDA
1 - descompacta e salva o arquivo descompactado.
2 - ler o arquivo descompactado
3 - cria um rdd
4 - cria um dataframe
5 - salva o arquivo descompactado no database.

O code ftp_2_datalake é um code de teste para verificar se o ftp estava ok.

### CASE 2
- Foi feito on premisse
Verificar notebook CASE_2_COMPLETE.ipynb
- Observações: fiz de forma mais reduzida nesse arquivo que utilizei no databricks.
Mas na versão completa tentei seguir todos os passos do case.
