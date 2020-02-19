import argparse, os, sys

def parse_arguments():
  """ Parse arguments from command line """
  parser = argparse.ArgumentParser()

  parser.add_argument("files",
    metavar="FILE",
    #type=int,
    nargs='?', #optional
    #nargs='+', #mandatory
    #default="",
    help="files to be parsed"
      )

  parser.add_argument("-v",
    "--verbose",
    action="store_true",
    default=False,
    help="outputs what the program does"
    )

  parser.add_argument("-d",
    "--debug",
    action="store_true",
    default=False,
    help="prints debug information (development)"
    )

  parser.add_argument("-a",
    "--append",
    metavar="APPEND",
    action="append", #append strings, can be called multiple times
    help="append options"
    )

  return parser.parse_args()


if __name__ == '__main__':
  """ Main function """
  args = parse_arguments()
  print(args)
