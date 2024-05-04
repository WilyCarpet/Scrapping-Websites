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

    # Create root element for HTML
    root = ET.Element("html")

    # Create head and body elements

    #Content inside head element
    head = ET.SubElement(root, "head")
    ET.SubElement(head,"link rel=\"stylesheet\" href=\"stylesheet.css\"")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site"
    body = ET.SubElement(root, "body")

    #Content inside header element
    header = ET.SubElement(body,"header")
    ET.SubElement(header,"img src=\"Images/OPENAI symbol.webp\" alt=\"Open AI symbol\" class=\"header_img\"")
    header_h1 = ET.SubElement(header,"h1 class=\"header_h1\"")
    header_h1.text = "OpenAI Summarizes Articles"

    #Content inside main element
    main = ET.SubElement(body,"main")
    main_dev = ET.SubElement(main,"dev class=\"main_center\"")

    #Content inside footer element
    footer = ET.SubElement(body,"footer")
    p_footer = ET.SubElement(footer,"p")
    p_footer.text = "\u00A9 Austin Luebbers"

    # Extract header and paragraph for each article
    for line in range(1,len(content),2):

        article_header = content[line - 1].strip().replace('"', '')
        paragraph = "\t" + content[line].strip()

        # Create header and paragraph elements in main
        h2 = ET.SubElement(main_dev, "h2 class =\"main_h2\"")
        h2.text = article_header
        p = ET.SubElement(main_dev, "p class=\"main_p\"")
        p.text = paragraph

    # Write HTML tree to file
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8')


txt_file = "articles.txt"
html_file = "webpage.html"
txt_to_html(txt_file, html_file)

print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")
