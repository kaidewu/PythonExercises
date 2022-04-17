import argparse
from pathlib import Path
from sys import stderr

class CpError(Exception):
    pass

def cpy_directory(src: Path, dest: Path):
    print('cp dir')

def copy_file(src: Path, dest: Path):
    if dest.is_dir():
        dest = dest / src.name
    if dest.is_file():
        raise CpError('Cannot override existing file')

def copy(src: Path, dest: Path):
    if src.is_file():
        copy_file(src, dest)
    elif src.is_dir():
        cpy_directory(src, dest)
    else:
        raise CpError('File type not supported')

def cli() -> argparse.Namespace:
    parse = argparse.ArgumentParser(
        prog='cp',
        description='Copy files',
    )
    parse.add_argument(
        'source',
        type=Path,
        help='Source directory or file'
    )
    parse.add_argument(
        'destination',
        type=Path,
        help='Destination directory or file'
    )
    return parse.parse_args()

def main():
    args = cli()
    try:
        copy(args.source, args.destination)
    except CpError as e:
        print(f'{e}', file=stderr)
        exit(1)

if __name__ == '__main__':
    main()