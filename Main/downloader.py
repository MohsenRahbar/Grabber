"""
        Downloader project
"""
import requests
import os
from urllib.parse import urlparse


# Download function
def download(base_url):
    
    """
        Function for download 
    """
    # Break the url:
    source=urlparse(base_url)
    # Extraction name file:
    file_name= (os.path.basename(source.path))

    responce = requests.get(base_url)
    # Writ or create file:
    with open(file_name,"wb") as file:
        file.write(responce.content)

# Get url:
download(base_url=input("URL: "))
