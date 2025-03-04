# Ángel Romero Huici

"""
Getting articles
"""
import glob

"""
Extracting abstract
"""
import requests
import xml.etree.ElementTree as ET

def get_abstract(pdf):
    abstract_text = ""

    with open(pdf, "rb") as pdf_file:
        files = {"input": pdf_file}
        params = {"consolidateHeader": 1}
        response = requests.post("http://grobid:8070/api/processFulltextDocument", files=files, data=params)

    if response.status_code == 200:
        xml_output = response.text
    
        root = ET.fromstring(xml_output)
        namespace = {"tei": "http://www.tei-c.org/ns/1.0"}
    
        abstract_element = root.find(".//tei:abstract", namespace)
        if abstract_element is not None:
            abstract_text = " ".join(abstract_element.itertext()).strip()
            print("Abstract extraído:")
            print(abstract_text[:50]+"...")
        else:
            print("No se encontró el abstract en el documento.")
    else:
        print(f"Error en la conversión: {response.status_code}")
        print(response.text)
    return abstract_text

"""
Drawing Wordcloud
"""
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def draw_wordcloud(abstracts):
    text = " ".join(abstracts)

    text = re.sub(r"[^a-zA-Z\s]", "", text.lower())

    wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="viridis", max_words=100).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Abstracts")
    plt.savefig("persistent/results/wordcloud.png")
    print("image saved at /results")

"""
MAIN
"""
def main():
    files = glob.glob("persistent/articles/*.pdf")

    if files == []:
        print("No files found")

    else:
        abstracts = [get_abstract(pdf) for pdf in files]
        draw_wordcloud(abstracts=abstracts)

if __name__ == "__main__":
    main()