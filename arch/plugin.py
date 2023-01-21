import archinstall


class Plugin:
    def __init__(self) -> None:
        path, _ = archinstall.all_blockdevices(partitions=False).popitem()
        archinstall.arguments["harddrives"] = [path]
