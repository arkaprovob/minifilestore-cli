import argparse
from ops import process_add_command, process_ls_command, process_rm_command, process_wc_command, \
    process_fw_command, process_update_command


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

    # subparser for 'freq-words' command
    freq_parser = subparsers.add_parser('freq-words')
    freq_parser.add_argument('limit', type=int, help='Limit for frequency of words')
    freq_parser.add_argument('--order', default='desc',
                             choices=['asc', 'desc'],
                             help='Order of frequency of words')

    # subparser for 'freq-words' command
    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('file', help='File to update')
    update_parser.add_argument('--duplicate',
                               action='store_true', help='Setting this flag will result in '
                                                         'duplicate file creation. Default is '
                                                         'False.')

    args = parser.parse_args()

    if args.store == 'add':
        process_add_command(args.files)
    elif args.store == 'ls':
        process_ls_command()
    elif args.store == 'rm':
        process_rm_command(args.files)
    elif args.store == 'wc':
        process_wc_command()
    elif args.store == 'freq-words':
        process_fw_command(args.limit, args.order)
    elif args.store == 'update':
        process_update_command(args.file, args.duplicate)


if __name__ == "__main__":
    main()
