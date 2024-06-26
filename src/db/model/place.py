# src/db/model.py

from sqlalchemy import Column, Text, BigInteger, String
from sqlalchemy.orm import relationship

from src.db.base import Base


class Place(Base):
    __tablename__ = "places"
    id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    message_thread_id = Column(String, default="General", nullable=False)

    operations = relationship("OperationHistory", back_populates="place", post_update=True)
    camera_links = relationship("PlaceCameraLink", back_populates="place")