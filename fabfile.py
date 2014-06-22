import os
from fabric.api import lcd, local

PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))
REQUIREMENTS_DIR = os.path.join(PROJECT_DIR, 'requirements')
NODE_MODULES_BIN_PATH = os.path.join(REQUIREMENTS_DIR, 'node_modules', '.bin')


def install_node_modules():
    with lcd(os.path.join(PROJECT_DIR, 'requirements')):
        local('npm install')


def compile_less():
    command = os.path.join(NODE_MODULES_BIN_PATH, 'lessc')
    src = os.path.join(
        PROJECT_DIR, 'radpress', 'static', 'radpress_less', 'main.less')
    dst = os.path.join(
        PROJECT_DIR, 'radpress', 'static', 'radpress', 'css', 'main.css')
    local('%s %s > %s' % (command, src, dst))
