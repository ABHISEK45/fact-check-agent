from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    claims = relationship(
        "Claim",
        back_populates="report",
        cascade="all, delete-orphan"
    )


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    report_id = Column(
        Integer,
        ForeignKey("reports.id"),
        nullable=False
    )

    claim = Column(Text, nullable=False)
    claim_type = Column(String(100))
    search_query = Column(Text)
    verdict = Column(String(50))
    confidence = Column(String(50))
    correct_fact = Column(Text)
    explanation = Column(Text)

    report = relationship(
        "Report",
        back_populates="claims"
    )