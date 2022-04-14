from faker import Faker

def test_actions():
    fake = Faker()
    print (f"\nFAKER NUMBER: {fake.random_number()}")
    assert 1 == 1
