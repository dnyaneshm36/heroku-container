from django.db import models
from django.conf import settings
# Create your models here.

class PostModel(models.Model):
    user_id     =                      models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content  =                        models.CharField(max_length=30)
    total_likes =                      models.PositiveIntegerField(default=0)
    total_comments =                   models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.content or ""
    
    class Meta:
        verbose_name = 'post detail'
        verbose_name_plural = 'Posts  details'




class PostlikesModel(models.Model):
    user_id     =                      models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post_id  =                         models.ForeignKey(PostModel,on_delete=models.CASCADE)
    updated_at  = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return str(self.user_id) or ""
    
    class Meta:
        verbose_name = 'post likes detail'
        verbose_name_plural = 'Posts likes details'
