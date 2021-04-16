import argparse
import os
import sys

from .proj_generator import ProjGenerator


def run():
    parser = argparse.ArgumentParser(description="Better tool to create rust projects")
    parser.add_argument("--proj", type=str, help="Name of rust project")
    parser.add_argument("--lib", action="store_true", default=False)
    parser.add_argument("--both", action="store_true", default=False)
    parser.add_argument("--force", action="store_true", default=False)

    args = parser.parse_args()

    if os.path.exists(args.proj) and not args.force:
        print(f"\033[91mError: The project {args.proj} already exists, use --force to overwrite it!\033[91m") 
        sys.exit()   

    project_generator = ProjGenerator(dir_name=args.proj, is_lib=args.lib, is_both=args.both)
    project_generator.generate()
    