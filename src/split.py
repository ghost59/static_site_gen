from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes: 
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_node = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_node.append(TextNode(sections[i],TextType.TEXT))
            else: 
                split_node.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue

        og_text = old.text
        image = extract_markdown_images(og_text)
        if len(image) == 0:
            new_nodes.append(old)
            continue

        for alt, url in image:
            img_md = f"![{alt}]({url})"
            sections = og_text.split(img_md,1)
            before, og_text = sections[0], sections[1]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

        if og_text:
            new_nodes.append(TextNode(og_text,TextType.TEXT))
    return new_nodes
            

                



def split_nodes_link(old_nodes):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue

        og_text = old.text
        links = extract_markdown_links(og_text)
        if len(links) == 0:
            new_nodes.append(old)
            continue

        for text, url in links:
            link_md = f"[{text}]({url})"
            sections = og_text.split(link_md,1)
            if len(sections) != 2: 
                raise ValueError("invalid markdown, link section not closed")
            before, og_text = sections[0], sections[1]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url))
        if og_text:
            new_nodes.append(TextNode(og_text,TextType.TEXT))
    return new_nodes