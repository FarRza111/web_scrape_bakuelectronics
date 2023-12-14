import pandas as pd
from model import ExternalTable
from pydantic import BaseModel, ValidationError



class ExternalTable(BaseModel):
    id: str
    name: str
    age: int
    email: str

    def __repr__(self):
        return " "

    class Config:
        mode = True


t = {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"} # ALWAYS TEST WITH ONE LINE OF CODE and THEN you can validate them # 

print(ExternalTable(**t))



external_table_data = [
    {"id": 1, "name": "Alice", "age": "25", "email": "Farix"},
    {"id": 2, "name": "Bob", "age": 30, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 22, "email": "charlie@example.com"},
    {"id": 4, "name": "David", "age": 28, "email": "david@example.com"},
]

df = pd.DataFrame(external_table_data)

ext_tab = df.to_dict(
    orient="records"
)  # just to test it from external table just in case if we have huge data

for row in ext_tab:
    try:
        validate_row = ExternalTable(**row)
        print(validate_row)
        print("row is valid")
    except ValidationError as e:
        print(f"row is not valid and this is type of error occured {e}")
