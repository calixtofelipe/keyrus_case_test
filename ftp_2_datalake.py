from ftplib import FTP, all_errors
from config import FTP_FILE, FTP_FOLDER, FTP_URL, FTP_USER, FTP_PASSWORD
import zipfile
import io
import os

"""
consome dados de um ftp em Spark. 
O Download do arquivo deve ser um .zip 
e descompactar em data frame para salvar em ambiente.
"""

# lista files no diretorio
def ftp_list_directory():
    ftp = FTP(FTP_URL, user=FTP_USER, passwd=FTP_PASSWORD)
    ftp.cwd("/home/fsociety/projetos/python/keyrus/ftp_folder")
    return ftp.retrlines("LIST")


# executa a transferencia de um arquivo do ftp zipado para o ambiente descompactado.
def ftp_2_datalake():
    with FTP(FTP_URL, user=FTP_USER, passwd=FTP_PASSWORD) as ftp:
        ftp.cwd(FTP_FOLDER)
        file_orig = FTP_FILE
        flo = io.BytesIO()
        ftp.retrbinary("RETR " + file_orig, flo.write)
        flo.seek(0)
        with zipfile.ZipFile(flo, "r") as zipped:
            zipped.extractall("")
