"""Creates Fake Data for the example Test feature"""

from sqlmodel import Session
from ...db import engine  # ! Make sure to import the engine, DO NOT create a new one

from ...models.test import Test

__authors__ = ["Mustafa Aljumayli"]

test1 = Test(title="Does the supabase DB work?")
test2 = Test(title="Does the API work?", count=3)
test3 = Test(title="Does CRUD work?")


def insert_fake_data(session: Session):
    """Adds the fake data defined above to the session"""
    session.add(test1)
    session.add(test2)
    session.add(test3)
