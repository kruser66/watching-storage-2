from django.db import models
from django.utils.timezone import localtime


def format_duration(seconds):

    days = str(seconds // 3600 // 24) + 'д.' if seconds >= 86400 else ''
    hours = str(seconds // 3600 % 24).rjust(2, '0')
    minutes = str(seconds % 3600 // 60).rjust(2, '0')

    return f'{days} {hours}:{minutes}'


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self, leaved_at=None):
        if not leaved_at:
            leaved_at = localtime()

        return int((leaved_at - localtime(self.entered_at)).total_seconds())

    def is_long(self, minutes=60):
        duration = self.get_duration(self.leaved_at)

        return duration > minutes * 60
