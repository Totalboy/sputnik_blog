from django.db import models

class House(models.Model):
    #название(представленно в виде строки CharField)
	name = models.CharField("Название", max_length=50)
    #поле IntegerField может принемать и хранить целые числа
	price = models.IntegerField("Цена")
	#текст произвольной длины
	description = models.TextField("Описание")
	photo = models.ImageField("Фотография", upload_to="houses/photos", default="", blank=True)
	datetime = models.DateTimeField('Дата публикации')

	class Meta:
		verbose_name = "дом"
		verbose_name_plural = "Дома"
		ordering = ["-datetime"]

	def __str__(self):
		return self.name
		# return "Пост {1}, {2}".format(self.id, self.name)

