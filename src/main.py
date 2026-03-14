from textnode import TextNode, TextType
from htmlnode import HTMLNode
from copystatic import copystat, copy_file_recurive
from generate import generate_page, generate_pages_recursive
import sys , os, shutil
def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    dir_path_static = "./static"
    dir_path_public = "./docs"
    dir_path_content = "./content"
    dir_path_template = "./template.html"
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    #generate_page("./content/index.md","./template.html","./public/index.html")
    copy_file_recurive(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content,dir_path_template, dir_path_public, basepath)

main()