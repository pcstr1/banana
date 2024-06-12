from style import Style,TreeStyle, RectangleStyle

# factory
class Factory:
    def create(self, file_name: str, shape_style: str, icon_style: str) -> 'Style':
        if shape_style == "tree" :
            return TreeStyle(file_name, icon_style)
        elif shape_style == "rectangle" :
            return RectangleStyle(file_name, icon_style)

class TreeStyleFactory:
    def create(self, file_name: str, icon_style: str) -> 'TreeStyle':
        return TreeStyle(file_name, icon_style)
    
class RectangleStyleFactory:
    def create(self, file_name: str, icon_style: str) -> 'RectangleStyle':
        return RectangleStyle(file_name, icon_style)
    
# abstract factory
class AbstractFactory:
    def create(self, file_name: str, shape_style: str, icon_style: str) -> 'Style':
        if shape_style == "tree" :
            treeStyleFactory = TreeStyleFactory()
            return treeStyleFactory.create(file_name, icon_style)
        elif shape_style == "rectangle" :
            rectangleStyleFactory = RectangleStyleFactory()
            return rectangleStyleFactory.create(file_name, icon_style)
        
# builder
class BuilderFactory:
    def __init__(self):
        self.file_name = ""
        self.shape_style = ""
        self.icon_style = ""

    def set_file_name(self, file_name: str) -> 'BuilderFactory':
        self.file_name = file_name
        return self

    def set_shape_style(self, shape_style: str) -> 'BuilderFactory':
        self.shape_style = shape_style
        return self

    def set_icon_style(self, icon_style: str) -> 'BuilderFactory':
        self.icon_style = icon_style
        return self

    def build(self) -> 'Style':
        factory = Factory()
        return factory.create(self.file_name, self.shape_style, self.icon_style)
    
# composition
class CompositionFactory:
    def __init__(self):
        self.styles = {}

    def add_style(self, name: str, file_name: str, shape_style: str, icon_style: str):
        if shape_style == "tree":
            style = TreeStyle(file_name, icon_style)
        elif shape_style == "rectangle":
            style = RectangleStyle(file_name, icon_style)
        else:
            raise ValueError("Invalid shape style")

        self.styles[name] = style

    def remove_style(self, name: str):
        if name in self.styles:
            del self.styles[name]

    def get_style(self, name: str) -> 'Style':
        return self.styles.get(name, None)

