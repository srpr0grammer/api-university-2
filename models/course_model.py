from typing import Optional

from sqlmodel import Field, SQLModel


class Course(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    classes: int
    hours: int
