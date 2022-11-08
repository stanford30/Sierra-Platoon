from django.core.exceptions import ValidationError
from django.utils import timezone


def valid_stroke(stroke):
    valid_strokes = ["front crawl", "butterfly", "breast", "back", "freestyle"]
    if stroke not in valid_strokes:
        raise ValidationError(f"{stroke} is not a valid stroke")
    return stroke


def valid_date(date):
    if date > timezone.now():
        raise ValidationError(f"Can't set record in the future.")


def valid_record_date(date):
    if date < timezone.now():
        raise ValidationError(f"Can't break record before record was set.")
