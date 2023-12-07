from sqlalchemy import Table, ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    def __repr__(self):
        return f'<Company {self.name}>'
    freebie=relationship('Freebie',backref='company')
    devs=relationship('Dev',secondary='company_dev',back_populates='companies')

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'
    freebie=relationship('Freebie',backref='dev')
    companies=relationship('Company',secondary='company_dev', back_populates='devs')
class Freebie(Base):
    __tablename__='freebies'

    id=Column(Integer(), primary_key=True)
    item_name=Column(String())
    value=Column(Integer())
    company_id=Column(Integer(), ForeignKey('companies.id'))
    dev_id=Column(Integer(), ForeignKey('devs.id'))

company_dev=Table(
    'companies_devs',
    Base.metadata,
    Column('company_id',ForeignKey('companies.id'), primary_key=True),
    Column('dev_id',ForeignKey('devs.id'), primary_key=True),
    extend_existing=True,
)