import sys

from .conf import load_conf
from .creds import get_env
from .shell import run_cmd


def main():
    conf = load_conf()
    env = get_env(conf)
    cmd = sys.argv[1:]
    run_cmd(cmd, env=env)
