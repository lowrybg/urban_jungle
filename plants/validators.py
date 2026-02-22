from django.core.exceptions import ValidationError

def validate_start_with_capital(value):
    if not value[0].isupper():
        raise ValidationError("Plant name must start with a capital letter!")
