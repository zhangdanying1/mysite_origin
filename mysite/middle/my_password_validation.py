from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class PasswordChangeValidator:
    """
    New password cannot be the same as the old one.
    """
    def validate(self, new_password1, user=None):
        if user.check_password(new_password1):
            raise ValidationError(
                _("New password cannot be the same as the old one Oh!!!"),
                code='New_password_cannot_be_same',
            )

    def get_help_text(self):
        return _('New password cannot be the same as the old one(help_text).')
