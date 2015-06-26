import argparse
import re
import json
from os import listdir
from os.path import join, isdir

def build_init_dir_tree(path):
  tree = dict()
  for _file in listdir(path):
    new_path = join(path, _file)
    if isdir(new_path) and "__init__.py" in listdir(new_path):
      if not new_path in tree:
        tree[new_path] = []
      tree[new_path].append(build_init_dir_tree(new_path))
  return tree