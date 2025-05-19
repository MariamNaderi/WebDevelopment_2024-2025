from django.db import models

class Vegetable(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название овоща")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to='vegetables/',  
        verbose_name="Изображение",
        blank=True, 
        null=True   
    )

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ваше имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.name}"