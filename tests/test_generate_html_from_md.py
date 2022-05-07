from src.Markdown_Reader import Markdown_Reader
from textwrap import dedent

def test_should_replace_headers():
    md = Markdown_Reader('tests/test_readme.md')
    md.write_into_md_file_custom(dedent("""# Title \n## Subtitle \n### Subsubtitle"""))
    html = md.generate_html_from_md()
    assert html == """<h1> Title </h1><h2> Subtitle </h2><h3> Subsubtitle</h3>"""

def test_should_replace_lines():
    md = Markdown_Reader('tests/test_readme.md')
    md.write_into_md_file_custom(dedent("""* item 1 \n* item 2 \n* item 3"""))
    html = md.generate_html_from_md()
    assert html == """<li> item 1 </li><li> item 2 </li><li> item 3</li>"""

def test_should_replace_non_starting_lines_with_paragraph():
    md = Markdown_Reader('tests/test_readme.md')
    md.write_into_md_file_custom(dedent("""item 1 \nitem 2 \nitem 3"""))
    html = md.generate_html_from_md()
    assert html == """<p>item 1 </p><p>item 2 </p><p>item 3</p>"""
def test_should_replace_list_brackets_and_parentesis_with_html_a_tag():
    md = Markdown_Reader('tests/test_readme.md')
    md.write_into_md_file_custom(dedent("""[link](http://www.google.com)"""))
    html = md.generate_html_from_md()
    assert html == """<a href="http://www.google.com">link</a>"""
def test_should_replace_md_image_with_img_tag():
    md = Markdown_Reader('tests/test_readme.md')
    md.write_into_md_file_custom(dedent("""![image](image.png)"""))
    html = md.generate_html_from_md().strip()
    print(html,md.generate_html_from_md())
    assert html == """<img src="image.png" alt="image">"""
    
