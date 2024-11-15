from .basic_conf import BasicConf


class TfConf:
    class Development1(BasicConf):
        ALL_STACKS = ["vpc-stack"]

    class Local(BasicConf):
        ALL_STACKS = []

    class Staging1(BasicConf):
        ALL_STACKS = ["vpc-stack"]
