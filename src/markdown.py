from htmlnode import ParentNode
from block import block_to_block_type, BlockType
from textnode import text_node_to_html_node
from text import text_to_children
from textnode import TextNode, TextType
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        block = block.strip()
        if block != "":
            result.append(block)

    return result


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            node = paragraph_to_html_node(block)
        elif block_type == BlockType.HEADING:
            node = heading_to_html_node(block)
        elif block_type == BlockType.QUOTE:
            node = quoute_to_html_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node = ulist_to_html_node(block)
        elif block_type == BlockType.ORDERED_LIST:
            node = olist_to_html_node(block)
        elif block_type == BlockType.CODE:
            node = code_to_html_node(block)
        else: 
            raise ValueError("Invalid block type")
        
        
        children.append(node)

    return ParentNode('div',children)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph_text = " ".join(lines)
    children = text_to_children(paragraph_text)

    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)
def ulist_to_html_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li",children))
    return ParentNode("ul", html_items)
def olist_to_html_node(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line.split(". ",1)[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li",children))
    return ParentNode("ol", html_items)
def quoute_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:

        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def code_to_html_node(block):
    text = block.strip("`").strip("\n")

    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])
