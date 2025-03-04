# Ángel Romero Huici

"""
Getting articles
"""
import glob

"""
Obtaining links in text
"""
import requests
import xml.etree.ElementTree as ET
import re

def get_links(pdf):
    links = []

    with open(pdf, "rb") as pdf_file:
        files = {"input": pdf_file}
        params = {"consolidateHeader": 1}
        response = requests.post("http://grobid:8070/api/processFulltextDocument", files=files, data=params)

    if response.status_code == 200:
        xml_output = response.text
    
        root = ET.fromstring(xml_output)

        regex = r"https?://[^\s<>\"']+"

        all_text = " ".join(root.itertext()).strip()
        links = re.findall(regex, all_text)

        print("Links encontrados:", len(links))
        
    else:
        print(f"Error en la conversión: {response.status_code}")
        print(response.text)
    return links

"""
Printing links
"""
import json

def save_links(links):
    link_dict = {}
    for i in list(range(0,len(links))):
        link_dict[i] = links[i]

    with open('persistent/results/links.json', 'w') as fp:
        json.dump(link_dict, fp, indent=2)
    print('json saved at /results')

"""
MAIN
"""
def main():
    files = glob.glob("persistent/articles/*.pdf")

    if files == []:
        print("No files found")

    else:
        links = [get_links(pdf) for pdf in files]
        save_links(links=links)

if __name__ == "__main__":
    main()