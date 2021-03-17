from nornir.core.task import Task, Result
from nornir_netmiko.tasks import netmiko_send_command


def show_version(task: Task) -> Result:

    task.run(
        name="show version",
        task=netmiko_send_command(
            command_string='show version',
            use_textfsm=True
        ),
    )
    return Result(
        host=task.host,
        result="show version collected",
    )

def show_interfaces(task: Task) -> Result:

    task.run(
        name="show interfaces",
        task=netmiko_send_command(
            command_string='show interfaces',
            use_textfsm=True
        ),
    )

    return Result(
        host=task.host,
        result="show interfaces collected",
    )
