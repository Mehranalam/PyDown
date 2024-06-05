# PyDown
A simple project to convert .md files into a coherent .html file. a simple Markdown-to-HTML converter in Python `without using the markdown library or other library` **just use regex**. We'll manually parse the Markdown syntax and convert it to HTML. This approach will cover basic Markdown features such as headers, bold text, italic text, links, and lists.

### Usage

```bash
$ python3 main.py input_md_file output_html_file lang
```

#### markdown ruls

```markdown
Headers: #, ##, ###, etc.
Bold text: **bold** or __bold__
Italic text: *italic* or _italic_
Links: [text](url)
Unordered lists: - item
Ordered lists: 1. item
```


- just use `re` lib or ReGex: https://en.wikipedia.org/wiki/Regular_expression

### Sample use

markdown file:

```markdown
# Header 1
## Header 2
### Header 3

This is a paragraph with **bold** text and *italic* text.

This is another paragraph with a [link](https://example.com).

- List item 1
- List item 2

1. Ordered item 1
2. Ordered item 2

```

to html file:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PyDown - version 0.0.1</title>
</head>

<body>
    <a href="https://github.com/Mehranalam/PyDown">Mehranalam/PyDown</a>
    <h1>Header 1</h1>
    <h2>Header 2</h2>
    <h3>Header 3</h3>
    <p></p>
    <p>This is a paragraph with <strong>bold</strong> text and <em>italic</em> text.</p>
    <p></p>
    <p>This is another paragraph with a <a href="https://example.com">link</a>.</p>
    <p></p>
    <li>List item 1</li>
    <li>List item 2</li>
    <p></p>
    <li>Ordered item 1</li>
    <li>Ordered item 2</li>
</body>

</html>
```
