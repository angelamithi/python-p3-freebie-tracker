# models.py
from sqlalchemy import Table, ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, sessionmaker
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
    freebie = relationship('Freebie', backref='company')
    devs = relationship('Dev', secondary='companies_devs', back_populates='companies')

    def company_freebies(self):
        return self.freebie
    #session.query(Freebie).filter_by(company_id=self.id).all()
    def company_devs(self):
        return self.devs    
    
class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'<Dev {self.name}>'
    freebie = relationship('Freebie', backref='dev')
    companies = relationship('Company', secondary='companies_devs', back_populates='devs')
   
    def dev_freebies(self):
        return self.freebie
    #session.query(Freebie).filter_by(dev_id=self.id).all()
    def dev_companies(self):
        return self.companies


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    
    def dev_instance_for_freebie(self):
         return self.dev.name
    def company_instance_for_freebie(self):
        return self.company.name
    


company_dev= Table(
    'companies_devs',
    Base.metadata,
    Column('company_id', ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', ForeignKey('devs.id'), primary_key=True),
    extend_existing=True,
)

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)  

Session = sessionmaker(bind=engine)
session = Session()

company4=session.query(Company).get(4)
company4_freebies=company4.company_freebies()
for freebie in company4_freebies:
    print(f"Company 4 Freebies: {freebie.item_name}")

company3=session.query(Company).get(3)
company3_devs=company3.company_devs()
for dev in company3_devs:
    print(f"Company 3 devs:{dev.name}")

dev4=session.query(Dev).get(4)
dev4_freebies=dev4.dev_freebies()
for freebie in dev4_freebies:
    print(f'Dev 4 Freebies:{freebie.item_name}')

dev5=session.query(Dev).get(5)
dev5_company=dev5.dev_companies()
for dev in dev5_company:
    print(f"Developer 5 Company:{dev.name}")

freebie4=session.query(Freebie).get(4)
freebie4_dev=freebie4.dev_instance_for_freebie()
print(f"Dev who got freebie4:{freebie4_dev}")

freebie1=session.query(Freebie).get(9)
freebie1_company=freebie1.company_instance_for_freebie()
print(f'Freebie name:{freebie1_company}')