"""This API route is only going to be used for demo and setup confirmation purposes."""

from fastapi import APIRouter, Depends
from ..models.test import Test
from ..services.test import TestService

__authors__ = ["Mustafa Aljumayli"]

openapi_tags = {
    "name": "Testing",
    "description": "These routes are only used for demo/setup confirmation purposes.",
}

api = APIRouter(prefix="/api/test")

test = 0


@api.get("/get_all", tags=["Testing"])
def get_all_tests(test_svc: TestService = Depends()) -> list[Test]:
    """Gets the Current Test"""
    return test_svc.get_tests()


@api.post("/add_test", tags=["Testing"])
def add_test(tester: Test, test_svc: TestService = Depends()) -> None:
    """Adds a new tester to the database"""
    return test_svc.add_new_tester(tester)


@api.get("/{id}", tags=["Testing"])
def get_test(id: int, test_svc: TestService = Depends()) -> Test:
    """Gets a tester with id, returns 404 error if it was not found"""
    return test_svc.get_test(id)


@api.put("/{id}/{new_test}", tags=["Testing"])
def update_test(id: int, new_test: int, test_svc: TestService = Depends()) -> Test:
    """Updates a tester with the matching id to hold a test of new_test"""
    return test_svc.update_tester(id, new_test)


@api.delete("/{id}", tags=["Testing"])
def delete_test(id: int, test_svc: TestService = Depends()) -> bool:
    """Attempts to delete a tester with id"""
    return test_svc.delete_tester(id)
