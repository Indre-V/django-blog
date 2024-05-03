from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):
    """
    This test does the following:
It imports the CollaborateForm and populates it.
It then checks to see if the form is valid based on the values we used. 
If it is not valid, the fail message is printed.
The test will fail because all fields are required, 
but we have failed to populate the name field in the dictionary passed to CollaborateForm.
We can get the test to pass by adding a value to the name field in the dictionary.
A dot . means that the test has passed. There will be one dot . for each passing test.
When the test fails, you get an F instead of a dot. 
If there is an error in your test, you will get an E.
The tests appear to be running out of order. 
The second test for the blog app appears to be running first. We'll explain why below.

    """

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'test name',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")
    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = CollaborateForm({
            'name': 'Matt',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
