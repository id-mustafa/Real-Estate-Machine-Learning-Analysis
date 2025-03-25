"""Service to handle the Test example feature"""

from ..db import db_session
from fastapi import Depends
from sqlmodel import Session, select

from .exceptions import ResourceNotFoundException

from ..models.test import Test

__authors__ = ["Mustafa Aljumayli"]


class TestService:
    """Service that preforms actions on the test table"""

    def __init__(
        self, session: Session = Depends(db_session)
    ):  # Add all dependencies via FastAPI injection in the constructor
        self._session = session

    def get_tests(self) -> list[Test]:
        """Gets all the current tests"""
        statement = select(Test)
        return self._session.exec(
            statement
        ).all()  # .all() converts the interable returned by .exec into a list of models

    def get_test(self, id: int) -> Test | None:
        """Gets the test with id=id"""
        test = self._session.get(Test, id)
        if test == None:
            raise ResourceNotFoundException(f"Tester of id={id} was not found")
        return test

    def add_new_test(self, new_test: Test) -> None:
        """Adds a new test in the shape of the defined Test"""
        new_test.id = None  # Explicitly make sure the id is None so SQLModel can handle the id selection
        self._session.add(new_test)
        self._session.commit()

    def update_test(self, id: int, new_count: int) -> Test:
        """Updates a test's test and returns it"""
        test = self.get_test(id)
        test.count = new_count
        self._session.add(test)
        self._session.commit()
        self._session.refresh(
            test
        )  # This line updates the test in memory to match what is in the database, it's needed after a commit if you intend to use that data in memory later
        return test

    def delete_test(self, id: int) -> bool:
        """Deletes a test and returns true if it was successful"""
        test = self.get_test(id)
        self._session.delete(test)
        self._session.commit()
        return True
