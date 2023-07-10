from controller.json_parser import JsonParser
from controller.output_generator import OutputGenerator


def main():
    json_parser = JsonParser(file_path='data.json')
    transactions = json_parser.parse()
    output_generator = OutputGenerator(transactions)
    output_generator.generate()


if __name__ == '__main__':
    main()
