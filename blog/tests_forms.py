from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Test class
    """

    def test_form_is_valid(self):
        """
        Test form
        """
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')
    def test_form_is_invalid(self):
        """
        assertFalse that will pass when the form is not valid.
        """
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
