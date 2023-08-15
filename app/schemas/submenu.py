from pydantic import BaseModel


class SubMenuBase(BaseModel):
    title: str
    description: str | None = None


class SubMenuCreate(SubMenuBase):
    pass


class SubMenu(SubMenuBase):
    id: int | str
    parent_id: int

    class Config:
        orm_mode = True
