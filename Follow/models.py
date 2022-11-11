from django.db import models
from Account.models import User

class Friend(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    friends = models.ForeignKey(User,on_delete=models.CASCADE,related_name="friends")
    category = models.CharField(max_length=50,choices=[("Following","Following"),
                                                    ("Follow","Follow"),
                                                    ("Following","Following"),
                                                    ("Mutual","Mutual"),
                                                    ("None","None")
                                                    ],default="None")
    status = models.CharField(max_length=50,choices=[("active","active"),
                                                    ("inactive","inactive"),
                                                    ("block","block"),
                                                    ("hide","hide"),
                                                    ("ignore","ignore")
                                                    ],default="active")

    def __str__(self):
        return self.user.username
