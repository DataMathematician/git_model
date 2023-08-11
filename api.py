from pydantic import BaseModel


class Model(BaseModel):
    name: str
    val: str

def create_data(vals: object):
    print(f"creates {vals}")

def read_data(meta: Model) -> dict:
    return {'name': meta.name, 'val': meta.val}

def update_data(meta: Model) -> str:
    return f'updated {meta.name}'

def delete_data(meta: Model):
    return f'deleted {meta.name}'

def read_cde(table):
    pass

def update_cde(table):
    pass

def create_cde(table):
    pass

def delete_cde(table):
    pass