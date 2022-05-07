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
            elif line.startswith("* ") or line.startswith("- ") or line.startswith("+ "):
                self.replace_asterisk_with_li(line,html)
            elif line.startswith("[") and line.endswith(")"):
                self.replace_list_brackets_and_parentesis_with_html_a_tag(line,html)
            elif line.startswith("![") and line.endswith(")"):
                self.replace_md_image_with_img_tag(line,html)
            else:
                self.replace_empty_with_paragraph(line,html)
        html = ''.join(html)
        self.html = html
        return self.html

    def replace_hashes_with_html(self,line,html):

        num_hashes = len(line) - len(line.lstrip('#'))
        text = line.lstrip('#')
        html.append('<h{}>{}</h{}>'.format(num_hashes, text, num_hashes))
    def replace_asterisk_with_li(self,line,html):
        """
        Replace asterisk with li.
        """
        html.append('<li>{}</li>'.format(line.lstrip('*'),line.lstrip('- '),line.lstrip('+ ')))
    def replace_empty_with_paragraph(self,line,html):
        """
        Replace empty with paragraph.
        """
        html.append('<p>{}</p>'.format(line))
    def replace_list_brackets_and_parentesis_with_html_a_tag(self,line,html):
        """
        Replace list brackets and parentesis with html a tag.
        """
        link_name = line.split('[')[1].split(']')[0]
        link = line.split('(')[1].split(')')[0]
        html.append('<a href="{}">{}</a>'.format(link,link_name))
    def replace_md_image_with_img_tag(self,line,html):
        """
        Replace md image with img tag.
        """
        image_name = line.split('![')[1].split(']')[0]
        image = line.split('(')[1].split(')')[0]
        html.append('<img src="{}" alt="{}">'.format(image,image_name))
    def write_into_md_file_custom(self,text):
        with open(self.md_file, 'w') as f:
            f.write(text.strip())
    def generate_style_for_html(self):
        """
        Generate style for html.
        """
        theme1 = """
        
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap');
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Roboto, Arial;
            color:#fff;
        }
        body{
            min-width:100vh;
            background-color: #212121;
            text-align:center;
        }
        h1 {
            font-size: 2em;
            margin: 0.67em 0;
        }
        h2 {
            font-size: 1.5em;
            margin: 0.67em 0;
        }
        h3 {
            font-size: 1.17em;
            margin: 0.83em 0;
        }
        li{
            list-style:none;
            list-style-type:none;
            
        }
        a{
            text-decoration:none;
            color:white;
        }
        a:hover{
            text-decoration:underline;
            cursor:pointer;
        }
        img{
            max-width:30vw;
        }
        """
        return theme1
