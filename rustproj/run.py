import argparse

from .proj_generator import ProjGenerator


def run():
    parser = argparse.ArgumentParser(description="Better tool to create rust projects")
    parser.add_argument("--proj", type=str, help="Name of rust project")
    parser.add_argument("--lib", action="store_true", default=False)
    parser.add_argument("--both", action="store_true", default=False)

    args = parser.parse_args()

    project_generator = ProjGenerator(dir_name=args.proj, is_lib=args.lib, is_both=args.both)
    project_generator.generate()
    