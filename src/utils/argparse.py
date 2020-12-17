from argparse import ArgumentParser
from .ui import Cli, QT
from .agent import User, Ai

parser = ArgumentParser(
    prog="src/play.py",
    description="awesome othello AI",
    epilog="enjoy playing :D"
)

group = parser.add_mutually_exclusive_group(
    required=True
)
group.add_argument("-c", "--cli", action="store_true",
                   help="play game in command mode")
group.add_argument("-g", "--gui", action="store_true",
                   help="play game in GUI mode")

parser.add_argument("--p1", choices=["ai", "user"], default="user")
parser.add_argument("--p2", choices=["ai", "user"], default="ai")

options = parser.parse_args()


def ui_chooser():
    assert options.cli or options.gui
    if options.cli:
        return Cli()
    else:
        return QT()


def player_creator():
    p1 = User() if options.p1 == "user" else Ai()
    p2 = User() if options.p2 == "user" else Ai()
    return (p1, p2)
