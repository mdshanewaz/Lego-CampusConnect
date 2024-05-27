from django.db import models


class OrderCancellationRequest(models.Model):
    message = models.TextField(max_length=2000)
    created_for = models.CharField(max_length=50)
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="timestamp of creation order cancellation request"
    )
    submitted_by = models.EmailField(max_length=255)

    def __repr__(self):     # same as __str__(self):
        return "{}".format(self.id)
