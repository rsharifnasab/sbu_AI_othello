from argparse import ArgumentParser
from .ui import Cli, QT

parser = ArgumentParser(
    prog="src/play.py",
    description="awesome othello AI",
    epilog="enjoy playing :D"
)
group = parser.add_mutually_exclusive_group()
group.add_argument("-c", "--cli", action="store_true",
                   help="play game in command mode")
group.add_argument("-g", "--gui", action="store_true",
                   help="play game in GUI mode")



def ui_chooser():
    if parser.parse_args().cli:
        return Cli()
    else:
        return QT()
