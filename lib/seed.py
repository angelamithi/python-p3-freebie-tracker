#!/usr/bin/env python
from models import Company,Dev,Freebie,company_dev
from sqlalchemy.orm import Session

# Script goes here!
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
