from src.conversor import Markdown_Reader

def test_should_generate_basic_html_from_basic_md():
    #generate html from test_readme.md
    md = Markdown_Reader('tests/test_readme.md')
    html = md.generate_html_from_md()
    #print the html
    print(html)
    #assert the html
    assert html == """<h1> Title</h1><h2> Subtitle</h2><h3> Subsubtitle</h3>"""