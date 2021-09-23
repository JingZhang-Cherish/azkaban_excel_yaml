# -* encoding:utf-8 -*-
from collections import OrderedDict
import yaml


def ordered_yaml_load(yaml_path, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    with open(yaml_path) as stream:
        return yaml.load(stream, OrderedLoader)


def ordered_yaml_dump(data, stream=None, Dumper=yaml.SafeDumper, **kwds):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())

    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)


if __name__ == '__main__':
    dumpfile = open('dump.yml', 'w')

    pydir2 = {}
    cdir2 = OrderedDict()
    pydir2['c'] = cdir2
    cdir2['rep1'] = 1
    cdir2['csd2'] = 2
    cdir2['fs3'] = 3
    cdir2['asd4'] = 4
    cdir2['ioweq5'] = 5
    cdir2['asd6'] = 6

    ordered_yaml_dump(pydir2,dumpfile)
    dumpfile.close()
