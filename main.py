import argparse
from ops import process_add_command, process_ls_command, process_rm_command, process_wc_command


def main():
    parser = argparse.ArgumentParser(description='File upload CLI')
    subparsers = parser.add_subparsers(dest='store')

    # Add subparser for 'add' command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('files', nargs='+', help='Files to upload')

    # subparser for 'ls' command
    subparsers.add_parser('ls')

    # subparser for 'rm' command
    rm_parser = subparsers.add_parser('rm')
    rm_parser.add_argument('files', nargs='+', help='Files to remove')

    # subparser for 'wc' command
    subparsers.add_parser('wc')

    args = parser.parse_args()

    if args.store == 'add':
        process_add_command(args.files)
    elif args.store == 'ls':
        process_ls_command()
    elif args.store == 'rm':
        process_rm_command(args.files)
    elif args.store == 'wc':
        process_wc_command()


if __name__ == "__main__":
    main()
