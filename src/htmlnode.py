class HTMLNode():
    def __init__(self, tag=None, value=None, children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError(self.children)
    def props_to_html(self):
        if not self.props: 
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())
    
        
        
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})" 
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, children=None, props=props)
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        prop_str = self.props_to_html()
        return f"<{self.tag}{prop_str}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag=None,children=None):
        super().__init__(tag, children=children,props=None)
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent must have a tag")
        if self.children is None:
            raise ValueError("Parent needs children")
        pro_str = self.props_to_html()
        child_string = [child.to_html() for child in self.children]
        statement = "".join(child_string)
        for child in self.children:
            print(type(child),child)
        return f"<{self.tag}{pro_str}>{statement}</{self.tag}>"

    