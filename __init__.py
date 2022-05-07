from src.Markdown_Reader import Markdown_Reader

def convert_markdown_to_html(md_file):
    """
    Convert markdown to html.
    """
    html_file = open("./index.html", "w")
    
    md = Markdown_Reader(md_file)
    html = md.generate_html_from_md()
    style = md.generate_style_for_html()
    html_file.write(html)
    html_file.write(style)
    html_file.close()
