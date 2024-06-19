from abc import ABC, abstractmethod
from typing import List

from node import InternalNode
from node import Node


# 定义访问者接口
class IVisitor(ABC):
    @abstractmethod
    def visit_tree(self, tree_style):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle_style):
        pass

# 实现访问者类
class Visitor(IVisitor):
    def visit_tree(self, tree_style):
        print(self.get_tree_info(tree_style))

    def visit_rectangle(self, rectangle_style):
        print(self.get_rectangle_info(rectangle_style))

    def get_tree_info(self, tree_style):
        children = tree_style.root.get_children()
        num_children = len(children)
        info = ""
        for index, child in enumerate(children):
            info += self.display_tree(tree_style, child, 0, [index == num_children - 1])
        return info

    def display_tree(self, tree_style, node: Node, level: int, is_last_child: List[bool]):
        info = ""
        for i in range(level):
            if not is_last_child[i]:
                info += '|' + ' ' * 2
            else:
                info += ' ' * 3
        if not is_last_child[level]:
            if node.is_internal():
                info += "├─" + tree_style.icon.get_internal_node_icon() + node.get_representation() + "\n"
            else:
                info += "├─" + tree_style.icon.get_leaf_node_icon() + node.get_representation() + "\n"
        else:
            if node.is_internal():
                info += "└─" + tree_style.icon.get_internal_node_icon() + node.get_representation() + "\n"
            else:
                info += "└─" + tree_style.icon.get_leaf_node_icon() + node.get_representation() + "\n"
        if isinstance(node, InternalNode):
            for child_index, child in enumerate(node.get_children()):
                is_last_child.append(child_index == len(node.get_children()) - 1)
                info += self.display_tree(tree_style, child, level + 1, is_last_child)
                is_last_child.pop()
        return info

    def get_rectangle_info(self, rectangle_style):
        children = rectangle_style.root.get_children()
        num_children = len(children)
        info = ""
        for index, child in enumerate(children):
            info += self.display_rectangle(rectangle_style, child, 0, [index == num_children - 1], index == 0)
        return info

    def display_rectangle(self, rectangle_style, node: Node, level: int, is_last_child: List[bool], is_head):
        info = ""
        is_toil = True
        if is_last_child[level]:
            if len(node.get_children()) != 0:
                is_toil = False
            else:
                for i in range(level):
                    if not is_last_child[i]:
                        is_toil = False
        else:
            is_toil = False
        if node.is_internal():
            icon = rectangle_style.icon.get_internal_node_icon()
        else:
            icon = rectangle_style.icon.get_leaf_node_icon()
        if is_head:
            representation = '┌─' + icon + node.get_representation() + ' '
            info += representation + f"{'─' * (50 - len(representation))}" + '┐\n'
        elif is_toil:
            representation = ""
            for i in range(level):
                representation += '└──'
            representation += '└─' + icon + node.get_representation() + ' '
            info += representation + f"{'─' * (50 - len(representation))}" + '┘\n'            
        else:
            representation = str('|' + f"{' ' * 2}") * level + "├─" + icon + node.get_representation() + ' '
            info += representation + f"{'─' * (50 - len(representation))}" + '┤\n'
        if isinstance(node, InternalNode):
            for child_index, child in enumerate(node.get_children()):
                is_last_child.append(child_index == len(node.get_children()) - 1)
                info += self.display_rectangle(rectangle_style, child, level + 1, is_last_child, False)
                is_last_child.pop()
        return info