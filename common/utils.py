from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?[1-9]\d{1,14}$',
    message="Telefon raqami xalqaro formatda bo'lishi kerak: masalan, '+998901234567'."
)