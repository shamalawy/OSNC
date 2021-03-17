import logging
from nornir import InitNornir
from nornir.plugins.inventory.simple import SimpleInventory
from nornir.core.plugins.inventory import InventoryPluginRegister


def get_nornir_cfg():
    """
    Returns the Nornir object.
    """
    InventoryPluginRegister.register("SimpleInventory", SimpleInventory)
    nr = InitNornir(
        logging = {
            "log_file": "osnc_nornir.log",
            "level": "DEBUG"
        },
        runner={
            "plugin": "threaded",
            "options": {
                "num_workers": 10,
            },
        },
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                    "host_file": "inventory/hosts.yaml",
                    "group_file": "inventory/groups.yaml",
                    "defaults_file": "inventory/defaults.yaml"
            },
        },
    )
    return nr