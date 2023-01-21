import json

import archinstall


class Plugin:
    def __init__(self) -> None:
        path, _ = archinstall.all_blockdevices(partitions=False).popitem()
        archinstall.arguments["silent"] = True
        archinstall.arguments["harddrives"] = [path]
        archinstall.arguments["disk_layouts"] = json.dumps(
            {
                path: {
                    "partitions": [
                        {
                            "boot": True,
                            "encrypted": False,
                            "filesystem": {"format": "fat32"},
                            "mountpoint": "/boot",
                            "size": "203MiB",
                            "start": "3MiB",
                            "type": "primary",
                            "wipe": True,
                        },
                        {
                            "btrfs": {
                                "subvolumes": {
                                    "@": "/",
                                    "@home": "/home",
                                    "@log": "/var/log",
                                    "@pkg": "/var/cache/pacman/pkg",
                                    "@.snapshots": "/.snapshots",
                                }
                            },
                            "encrypted": False,
                            "filesystem": {"format": "btrfs"},
                            "mountpoint": None,
                            "size": "100%",
                            "start": "206MiB",
                            "type": "primary",
                            "wipe": True,
                        }
                    ],
                    "wipe": True,
                },
            }
        )
