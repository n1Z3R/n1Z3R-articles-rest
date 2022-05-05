from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MinimumOneDigitOrOneLetterValidator:
    '''Password validator which control password field with properties:
    1) minumum one or more digits.
    2) minumum one or more letters.'''

    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                _("This password must contain at least one digit.")
            )
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                _("This password must contain at least one letter.")
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least one letter and one number characters."
        )
