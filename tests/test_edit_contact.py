from models.contact import Contact
from pages.add_contact_page import ContactPage
from pages.contacs_page import ContactsPage
from faker import Faker

fake = Faker()
def create_contact():
    return Contact(
        name = fake.first_name(),
        last_name = fake.last_name(),
        phone=fake.numerify("05#########"),
        email=fake.email(),
        address=fake.street_address(),
        description=fake.sentence(nb_words=2))


def test_edit_contact_name_field(authenticated):
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)
    
    contact = create_contact()
    contacts_page.create_contact(contact)
    new_name = fake.first_name()