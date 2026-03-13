from split import split_nodes_image, split_nodes_delimiter, split_nodes_link
from textnode import TextType, TextNode
from textnode import text_node_to_html_node
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes,"_",TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`",TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

idea = "some text [link](https://example.com) more text"
times = text_to_textnodes(idea)
print(times)

def text_to_children(text):
    # This comes from your previous work!
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        # This is the function you just showed me!
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children