# argparse

# Модуль argparse позволяет разбирать аргументы, передаваемые скрипту при его запуске из командной строки, и даёт возможность пользоваться этими аргументами в скрипте
# Аналог click

import argparse

parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('indir', type=str, help='Input dir for videos')
parser.add_argument('outdir', type=str, help='Output dir for videos')
parser.add_argument('-c', '--count', type=int, default=0, help='Count of repearation')
args = parser.parse_args()

print(args.count)
print(args.indir)
print(args.outdir)

# Запускать через командную строку из директории, где лежит файл:

# python .\TaskPython-V9-12.py --help
# python .\TaskPython-V9-12.py -h
# python .\TaskPython-V9-12.py .\TaskPython-V9-11.py factory
# c - опционально
# python .\TaskPython-V9-12.py .\TaskPython-V9-11.py factory -c 56


# End