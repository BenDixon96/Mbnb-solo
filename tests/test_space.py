from lib.space import Space
from unittest.mock import Mock
from lib.booking import Booking

def test_constructs():
    space = Space(1, 'Test Space', 'test description', 100.50, '2023-10-15', '2023-11-15', 1)
    assert space.id == 1
    assert space.space_name == 'Test Space'
    assert space.space_description == 'test description'
    assert space.price_per_night == 100.50
    assert space.available_from == '2023-10-15'
    assert space.available_to == '2023-11-15'
    assert space.user_id== 1


def test_compares():
    user1 = Space(1, 'Test Space', 'test description', 100.00, '2023-10-15', '2023-11-15', 1)
    user2 = Space(1, 'Test Space', 'test description', 100.00, '2023-10-15', '2023-11-15', 1)
    assert user1 == user2


def test_format():
    space = Space(1, 'Test Space', 'test description', 100, '2023-10-15', '2023-11-15', 1)
    assert str(space) == 'Space(1, Test Space, test description, 100, 2023-10-15, 2023-11-15, 1)'

def test_get_bookings_mock():
    book1 =  Booking(1, '2023-10-18','Confirmed', 2, 1)
    book2 = Booking(1, '2023-10-18','Confirmed', 2, 1)
   
    user1 = Space(1, 'Test Space', 'test description', 100.00, '2023-10-15', '2023-11-15', 1)
    b_list = [book1, book2]
    user1.get_bookings(b_list)
    assert len(user1.current_bookings) == 2


