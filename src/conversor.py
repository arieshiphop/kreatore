class Markdown_Reader:
    def __init__(self, md_file):
        self.md_file = md_file
        self.html = []

    def generate_html_from_md(self):
        """
        Generate HTML from a Markdown file.
        """
        
        with open(self.md_file, 'r') as f:
            md = f.read()
        
        self.html = self.read_lines_from_md_file(md)
        return self.html
            

    def read_lines_from_md_file(self,md):

        lines = md.split('\n')
        html = []
        for line in lines:
            if line.startswith('#'):
                self.replace_hashes_with_html(line,html)
            else:
                html.append(line)
        html = ''.join(html)
        self.html = html
        return self.html
    def replace_hashes_with_html(self,line,html):

        num_hashes = len(line) - len(line.lstrip('#'))
        text = line.lstrip('#')
        html.append('<h{}>{}</h{}>'.format(num_hashes, text, num_hashes))