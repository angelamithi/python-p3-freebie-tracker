#!/usr/bin/env python
#seed.py
from models import Company,Dev,Freebie,company_dev,session

# Script goes here!
session.query(Company).delete()
session.query(Dev).delete()
session.query(Freebie).delete()
session.commit()
companies_info=[{
  "id": 1,
  "name": "Devcast",
  "founding_year": 1993
}, {
  "id": 2,
  "name": "Kwinu",
  "founding_year": 2010
}, {
  "id": 3,
  "name": "Gigashots",
  "founding_year": 2008
}, {
  "id": 4,
  "name": "Voonder",
  "founding_year": 1984
}, {
  "id": 5,
  "name": "Chatterpoint",
  "founding_year": 1992
}, {
  "id": 6,
  "name": "Eabox",
  "founding_year": 1998
}, {
  "id": 7,
  "name": "Zoovu",
  "founding_year": 2005
}, {
  "id": 8,
  "name": "Zava",
  "founding_year": 1987
}, {
  "id": 9,
  "name": "Vitz",
  "founding_year": 2011
}, {
  "id": 10,
  "name": "Kazu",
  "founding_year": 2004
}]

session.add_all([Company(**company) for company in companies_info])
session.commit()

devs_info=[{
  "id": 1,
  "name": "Ingaborg Maher"
}, {
  "id": 2,
  "name": "Elijah Shiel"
}, {
  "id": 3,
  "name": "Isidro Axford"
}, {
  "id": 4,
  "name": "Lou Volleth"
}, {
  "id": 5,
  "name": "Regan Jermin"
}, {
  "id": 6,
  "name": "Kristel Fawdery"
}, {
  "id": 7,
  "name": "Sonnnie Rubinowicz"
}, {
  "id": 8,
  "name": "Bobette Beaufoy"
}, {
  "id": 9,
  "name": "Maximo Elderton"
}, {
  "id": 10,
  "name": "Laurianne Kilgrove"
}]

session.add_all([Dev(**dev) for dev in devs_info])
session.commit()

freebie_info=[
  {
    "id": 1,
    "item_name": "Laptop",
    "value": 1500,
    "company_id": 3,
    "dev_id": 8
  },
  {
    "id": 2,
    "item_name": "Mouse",
    "value": 20,
    "company_id": 5,
    "dev_id": 2
  },
  {
    "id": 3,
    "item_name": "Keyboard",
    "value": 50,
    "company_id": 7,
    "dev_id": 6
  },
  {
    "id": 4,
    "item_name": "USB Drive",
    "value": 10,
    "company_id": 1,
    "dev_id": 9
  },
  {
    "id": 5,
    "item_name": "Headphones",
    "value": 30,
    "company_id": 9,
    "dev_id": 4
  },
  {
    "id": 6,
    "item_name": "Webcam",
    "value": 40,
    "company_id": 2,
    "dev_id": 7
  },
  {
    "id": 7,
    "item_name": "External Hard Drive",
    "value": 80,
    "company_id": 8,
    "dev_id": 1
  },
  {
    "id": 8,
    "item_name": "Monitor",
    "value": 200,
    "company_id": 4,
    "dev_id": 10
  },
  {
    "id": 9,
    "item_name": "Wireless Mouse",
    "value": 25,
    "company_id": 6,
    "dev_id": 5
  },
  {
    "id": 10,
    "item_name": "Graphics Card",
    "value": 300,
    "company_id": 10,
    "dev_id": 3
  }
]
session.add_all([Freebie(**freebie) for freebie in freebie_info])
session.commit()



