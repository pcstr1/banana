import json
from abc import ABC, abstractmethod
from typing import List

from node import InternalNode
from node import LeafNode
from node import Node
from icon import DefaultIcon
from icon import PokerFaceIcon
from icon import Icon

class Style(ABC):
    def __init__(self, file_name: str, icon_style: str):
        self.root = self.load_data(file_name, "root")
        self.icon = self.choose_icon(icon_style)

    def load_data(self, file_name: str, node_name: str) -> Node:
        try:
            with open(file_name, 'r') as file:
                json_data = json.load(file)
            return self.build_data(json_data, node_name)
        except (IOError, json.JSONDecodeError) as e:
            print(e)
            return None

    def build_data(self, json_data: dict, node_name: str) -> Node:
        if json_data is None:
            return None

        if not json_data:
            return LeafNode(node_name, "null")

        node = InternalNode(node_name)
        for key, value in json_data.items():
            if isinstance(value, dict):
                child_node = self.build_data(value, key)
                if child_node:
                    node.add_child(child_node)
            else:
                node.add_child(LeafNode(key, str(value)))
        return node

    def choose_icon(self, icon_style: str):
        if icon_style == "pokerface":
            icon = PokerFaceIcon()
        elif icon_style == "default":
            icon = DefaultIcon()
        else:
            icon = DefaultIcon()
        return icon

    @abstractmethod
    def show(self) -> None:
        pass

class TreeStyle(Style):
    def __init__(self, file_name: str, icon_style: str):
        super().__init__(file_name, icon_style)

    def show(self) -> None:
        children = self.root.get_children()
        num_children = len(children)
        for index, child in enumerate(children):
            self.display_tree(child, 0, [index == num_children - 1])

    def display_tree(self, node: Node, level: int, is_last_child: List[bool]):
        for i in range(level):
            if not is_last_child[i]:
                print('|' + f"{' ' * 2}", end="")
            else:
                print(f"{' ' * 3}", end="")
        if not is_last_child[level]:
            if node.is_internal():
                print("├─" + self.icon.get_internal_node_icon() + node.get_representation())
            else:
                print("├─" + self.icon.get_leaf_node_icon() + node.get_representation())
        else:
            if node.is_internal():
                print("└─" + self.icon.get_internal_node_icon() + node.get_representation())
            else:
                print("└─" + self.icon.get_leaf_node_icon() + node.get_representation())
        if isinstance(node, InternalNode):
            for child_index, child in enumerate(node.get_children()):
                is_last_child.append(child_index == len(node.get_children()) - 1)
                self.display_tree(child, level + 1, is_last_child)
                is_last_child.pop()

class RectangleStyle(Style):
    def __init__(self, file_name: str, icon_style: str):
        super().__init__(file_name, icon_style)

    def show(self) -> None:
        children = self.root.get_children()
        num_children = len(children)
        for index, child in enumerate(children):
            self.display_rectangle(child, 0, [index == num_children - 1], index == 0)

    def display_rectangle(self, node: Node, level: int, is_last_child: List[bool], is_head):
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
            icon = self.icon.get_internal_node_icon()
        else:
            icon = self.icon.get_leaf_node_icon()
        if is_head:
            representation = '┌─' + icon + node.get_representation() + ' '
            print(representation + f"{'─' * (50 - len(representation))}" + '┐')
        elif is_toil:
            representation = ""
            for i in range(level):
                representation += '└──'
            representation += '└─' + icon + node.get_representation() + ' '
            print(representation + f"{'─' * (50 - len(representation))}" + '┘')            
        else:
            representation = str('|' + f"{' ' * 2}") * level + "├─" + icon + node.get_representation() + ' '
            print(representation + f"{'─' * (50 - len(representation))}" + '┤')
        if isinstance(node, InternalNode):
            for child_index, child in enumerate(node.get_children()):
                is_last_child.append(child_index == len(node.get_children()) - 1)
                self.display_rectangle(child, level + 1, is_last_child, False)
                is_last_child.pop()
