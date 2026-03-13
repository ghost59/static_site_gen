import os, pathlib
from markdown import markdown_to_html_node
from extract import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating from {from_path} to {dest_path} using {template_path}")
    os.makedirs(os.path.dirname(dest_path),exist_ok=True)
    with open(from_path, 'r') as f:
        path = f.read()
    with open(template_path,'r') as f:
        temp = f.read()
    mark = markdown_to_html_node(path)
    html_string = mark.to_html()
    title = extract_title(path)
    new_html = temp.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    with open(dest_path,'w') as f: 
        f.write(new_html)
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Build the full from {template_path} to {dest_dir_path}")
    for each_entry in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content,each_entry)
        dest_path = os.path.join(dest_dir_path, each_entry)
        if os.path.isfile(file_path):
            dest_path = pathlib.Path(dest_path).with_suffix(".html")
            generate_page(file_path, template_path, dest_path)
        else: 
            generate_pages_recursive(file_path, template_path, dest_path)
        