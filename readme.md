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