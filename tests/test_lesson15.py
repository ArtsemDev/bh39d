import unittest
from os import name

import pytest

from lesson15 import factorial


# class TestLesson15(unittest.TestCase):
#
#     def setUp(self) -> None:
#         pass
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         pass
#
#     # @unittest.skipIf(name == 'nt', 'Only UNIX system')
#     # @unittest.expectedFailure
#     def test_factorial(self):
#         self.assertEqual(factorial(5), 120)
#         self.assertEqual(factorial(6), 720)


@pytest.fixture()
def my_fixture():
    print('hello')


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'a, b',
    (
            (5, 120),
            (6, 720),
            (4, 24)
    )
)
async def test_factorial(a, b, my_fixture):
    assert await factorial(a) == b
