import uuid
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_unsubscribed = models.BooleanField(default=False)
    unsubscribe_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)  # ← вот это добавь

    def __str__(self):
        return self.email

    def get_unsubscribe_url(self):
        return f"https://unsubscribe.recovia.solutions/unsubscribe/?token={self.unsubscribe_token}"