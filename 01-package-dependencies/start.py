from sys import argv
import re
import requests as request
import json
from graphviz import Digraph

# Ссылка на сайт для получения информации о пакетах pip
URL = 'https://pypi.org/pypi/'


def get_deps_of_package_json(package_name):
    try:
        page = request.get(URL + package_name + '/json')
        json_object = json.loads(page.text)
        return json_object['info']['requires_dist'], True
    except Exception:
        return None, False


def find_dependencies(package_name):
    deps_package, flag = get_deps_of_package_json(package_name)
    if not flag:
        return
    if deps_package:
        for dep in deps_package:
            if re.compile(r'^[^;]+$').match(dep):
                dependency = dep.split(' ')[0].replace('\n', '')
                dot.edge(package_name, dependency)
                find_dependencies(dependency)
    if not dot.body:
        dot.edge(package_name, package_name)


# input_package_name = 'Sphinx'
input_package_name = argv[1]
dot = Digraph(name=input_package_name, comment='Package dependencies')
find_dependencies(input_package_name)
if dot.body:
    print(dot.source)
else:
    print('WARNING: Package(s) not found: ' + input_package_name)
