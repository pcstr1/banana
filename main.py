import argparse
from factory import Factory
from factory import AbstractFactory
from factory import BuilderFactory

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file_name', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--shape_style', required=True, choices=['tree', 'rectangle'], help='Visualization style')
    parser.add_argument('-i', '--icon_style', required=True, choices=['pokerface', 'default'], help='Icon family')
    
    args = parser.parse_args()
    
    factory = Factory()
    style = factory.create(args.file_name, args.shape_style, args.icon_style)

    style.show()

    return

if __name__ == "__main__":
    main()
