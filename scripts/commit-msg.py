#!/usr/bin/python

import argparse
import sys

def parse_msg():  
  print("[commit-msg.py] sys.argv: {}".format(sys.argv))
  commit_editmsg = sys.argv[1]
  commit_msg = None
  with open(commit_editmsg, "r") as fd:
    commit_msg = fd.read()
  print("[commit-msg.py] msg: {}".format(commit_msg))
  return commit_msg.strip()

def main(msg):
  if len(msg) == 0:
    print("[commit-msg.py] empty commit msg is not allowed")
    sys.exit(1)
  if not msg[0].isupper():
    print("[commit-msg.py] commit msg should starts with uppercase. (msg: {})".format(msg))
    sys.exit(1)

if __name__ == "__main__":
  msg = parse_msg()
  main(msg)
