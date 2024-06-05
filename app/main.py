import re
import sys

def convert_markdown_to_html(input_file: str, output_file: str, lang: str):
    """
    Convert a Markdown file to an HTML file. - PyDown Mehranalam

    :param input_file: Path to the input Markdown file.
    :param output_file: Path to the output HTML file.
    """
    with open(input_file, 'r', encoding='utf-8') as md_file:
        lines = md_file.readlines()
    
    html_lines = []

    for line in lines:
        line = line.rstrip() 
        
        if line.startswith('#'):
            header_level = len(line.split(' ')[0])
            line_content = line[header_level+1:]
            html_lines.append(f'<h{header_level}>{line_content}</h{header_level}>')
        
        else:
            '''
            Headers: Check for lines starting with # and convert them to HTML header tags <h1>, <h2>, etc.
            Bold and Italic: Use regular expressions to replace **bold**, __bold__, *italic*, and _italic_ with <strong> and <em> tags.
            Links: Use regular expressions to replace [text](url) with <a href="url">text</a>.
            Lists: Convert - item to unordered list items <li> and 1. item to ordered list items <li>.
            Paragraphs: Wrap other lines in <p> tags.

            '''

            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'__(.*?)__', r'<strong>\1</strong>', line)

            line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
            line = re.sub(r'_(.*?)_', r'<em>\1</em>', line)

            line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)
            
            if line.startswith('- '):
                html_lines.append(f'<li>{line[2:]}</li>')
            elif re.match(r'^\d+\. ', line):
                html_lines.append(f'<li>{line.split(" ", 1)[1]}</li>')
            else:
                html_lines.append(f'<p>{line}</p>')
    
    html_content = '\n'.join(html_lines)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="{lang}">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>PyDown - version 0.0.1</title>
        </head>
        <body>
            <a href="https://github.com/Mehranalam/PyDown">Mehranalam/PyDown</a>
            {html_content}
        </body>
    </html>
"""

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"PyDown: Conversion complete: {output_file}")

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python main.py <input_md_file> <output_html_file> <lang>")
        sys.exit(1)

    # Get the input and output file names and language from the arguments
    input_md_file = sys.argv[1]
    output_html_file = sys.argv[2]
    lang = sys.argv[3]

    convert_markdown_to_html(input_md_file, output_html_file, lang)
