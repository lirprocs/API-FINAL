from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..db_setup import Base


class Menu(Base): 
    __tablename__ = 'Menus'
    id = Column(Integer, primary_key=True, index=True)
    manual_id = Column(String, unique=True, nullable=True)
    title = Column(String(), unique=True, nullable=False)
    description = Column(String())
    # Отношение один-ко-многим с таблицей SubMenu
    submenus = relationship('SubMenu', back_populates='menu', cascade='all, delete-orphan')
