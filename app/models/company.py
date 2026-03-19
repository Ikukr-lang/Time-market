from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from ..core.database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    name = Column(String(200), nullable=False)
    slug = Column(String(100), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    trial_end = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(days=7))

    specialists = relationship("Specialist", back_populates="company")
    subscription = relationship("Subscription", back_populates="company", uselist=False)
