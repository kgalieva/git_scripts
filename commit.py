import argparse
from utils import Utils

# commit message is a required argument
parser = argparse.ArgumentParser(description='Process commit message.')
parser.add_argument('message', nargs=1, help='commit message')
args = parser.parse_args()
utils = Utils()
utils.call(["git", "commit", "-am", args.message[0]])