#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Ruben Espino with help from Chris Warren"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser."""
    parser = argparse.ArgumentParser(description="Transform input text")
    parser.add_argument("-l", "--lower", help="Changes text to lowercase", action="store_true")
    parser.add_argument('text', help='text that is changed')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit()
    args = parser.parse_args(args)
    text = args.text

    if args.lower:
        text = text.lower()
    print(text)
    return text


if __name__ == '__main__':
    main(sys.argv[1:])
