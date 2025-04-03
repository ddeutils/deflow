from pathlib import Path

from ddeutil.io import YamlEnvFl

from .conf import Process


def get_process(name: str, path: Path) -> Process:
    """Get Process instance from an input name and path values.

    :rtype: Process
    """
    for file in path.rglob("*"):
        if file.is_file() and file.stem == name:
            if file.suffix in (".yml", ".yaml"):
                data = YamlEnvFl(path=file).read()
                data["name"] = name
                process: Process = Process.model_validate(obj=data)
                assert (
                    process.group.name == file.parent.name
                ), "Group does not match with file location."
                assert (
                    process.group.stream.name == file.parent.parent.name
                ), "Stream does not match with file location."
                return process
            else:
                raise NotImplementedError(
                    f"Get process file: {file.name} does not support for "
                    f"type: {file.suffix}."
                )
    raise FileNotFoundError(f"{path}/**/{name}.yml")
