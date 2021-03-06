from django.db import models


class Questions(models.Model):
    question_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

