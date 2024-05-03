from xml.etree import ElementTree as ET

def txt_to_html(txt_file, html_file):
    """
    Converts a text file with header and paragraph to an HTML file.
    Make necessary changes for multiple news articles. This script is
    only for one news article.

    Args:
        txt_file (str): Path to the text file.
        html_file (str): Path to the output HTML file.
    """
    # Read text file content
    with open(txt_file, 'r') as f:
        content = f.readlines()

    # Create root element for HTML, try to remember the structure of a HTML file
    root = ET.Element("html")

    # Create head and body elements, try to understand how subElements works
    head = ET.SubElement(root, "head")
    link = ET.SubElement(head,"link rel=\"stylesheet\" href=\"stylesheet.css\"")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site"
    body = ET.SubElement(root, "body")

    # Extract header and paragraph for each article
    for line in range(1,len(content),2):

        header = content[line - 1].strip()
        paragraph = "".join(content[line]).strip()

        # Create header and paragraph elements in body
        h2 = ET.SubElement(body, "h2")
        h2.text = header
        p = ET.SubElement(body, "p")
        p.text = paragraph

    # Write HTML tree to file
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8')


txt_file = "articles.txt"
html_file = "webpage.html"
txt_to_html(txt_file, html_file)

print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")
