from textnode import TextNode, TextType
from htmlnode import HTMLNode
from copystatic import copystat
from generate import generate_page, generate_pages_recursive
import sys 
def main():
    basepath = sys.argv
    if basepath is None:
        basepath = "/"
    #generate_page("./content/index.md","./template.html","./public/index.html")
    copystat("/home/neil/sitegen/static", "./public")
    #generate_pages_recursive("/home/neil/sitegen/content","/home/neil/sitegen/template.html","public/")
main()