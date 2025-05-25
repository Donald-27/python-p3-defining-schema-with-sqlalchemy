#!/usr/bin/env python3

from sqlalchemy import create_engine
from lib.sqlalchemy_sandbox import Student, Base  

engine = create_engine('sqlite:///students.db')

if __name__ == '__main__':
    Base.metadata.create_all(engine) 
    import ipdb; ipdb.set_trace()
