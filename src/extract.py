import re 
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    
def extract_markdown_links(text):
    pattern =  r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
def extract_title(markdown: str):
    if markdown.startswith("#"):
        text = markdown
        text.strip("#")
        return text
    else:
        raise Exception("boy!!!!!")
    
