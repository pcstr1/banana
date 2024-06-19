import argparse
from style import TreeStyle, RectangleStyle
from visitor import Visitor
from data_struct import Array_style

def main():
    array_style = Array_style(10)
    
    tree1 = TreeStyle('test.json', 'default')
    rectangle1 = RectangleStyle('test.json', 'default')
    tree2 = TreeStyle('test.json', 'pokerface')
    rectangle2 = RectangleStyle('test.json', 'pokerface')
    array_style.add(tree1)
    array_style.add(rectangle1)
    array_style.add(tree2)
    array_style.add(rectangle2)

    visitor = Visitor();
    iterator = array_style.iterator();

    while iterator.has_next():
        style = iterator.next()
        style.accept(visitor)

    return

if __name__ == "__main__":
    main()
