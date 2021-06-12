from uuid import uuid4


def get_filepath(instance, filename):
    extension = filename.split(".")[-1]
    filename = f"{uuid4()}.{extension}"
    return filename
