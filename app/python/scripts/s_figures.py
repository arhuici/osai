# Ángel Romero Huici

"""
Getting articles
"""
import glob

"""
Getting number of figures
"""
import requests
import xml.etree.ElementTree as ET

def get_n_figures(pdf):
    num_figures = 0

    with open(pdf, "rb") as pdf_file:
        files = {"input": pdf_file}
        params = {"consolidateHeader": 1}
        response = requests.post("http://grobid:8070/api/processFulltextDocument", files=files, data=params)

    if response.status_code == 200:
        xml_output = response.text
    
        root = ET.fromstring(xml_output)
        namespace = {"tei": "http://www.tei-c.org/ns/1.0"}
    
        figures = root.findall(".//tei:figure", namespace)
        num_figures = len(figures)
        print("Figures found:", num_figures)
        
    else:
        print(f"Conversion error: {response.status_code}")
        print(response.text)
    return num_figures

"""
Drawing figures
"""
import matplotlib.pyplot as plt

def draw_figures(figures):
    plt.figure(1)
    plt.bar(list(range(0,len(figures))), figures)
    plt.show()
    plt.savefig("persistent/results/figures.png")
    print("image saved at /results")

"""
MAIN
"""
def main():
    files = glob.glob("persistent/articles/*.pdf")

    if files == []:
        print("No files found")

    else:
        figures = [get_n_figures(pdf) for pdf in files]
        draw_figures(figures=figures)

if __name__ == "__main__":
    main()