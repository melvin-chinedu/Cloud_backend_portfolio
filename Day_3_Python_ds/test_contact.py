from contacts import save_contacts, load_contacts
import os

def test_save_and_load():
    test_data = {"melvin": {"phone": "+23480000000000", "email": "melvin@example.com"}}
    save_contacts(test_data)
    loaded = load_contacts()
    assert loaded == test_data
    
