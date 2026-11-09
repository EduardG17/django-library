from django.db import models

class Edition(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    author = models.CharField(max_length=100, verbose_name="Автор")

    def __str__(self):
        return self.title

class Reader(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")

    def __str__(self):
        return self.full_name

class Copy(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, verbose_name="Издание")
    wear_coefficient = models.IntegerField(default=1, verbose_name="Коэффициент износа")

    def __str__(self):
        return f"{self.edition.title} (экз. {self.id})"

class Issue(models.Model):
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE, verbose_name="Экземпляр")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="Читатель")
    issue_date = models.DateField(auto_now_add=True, verbose_name="Дата выдачи")
    planned_return_date = models.DateField(verbose_name="Плановая дата возврата")
    actual_return_date = models.DateField(null=True, blank=True, verbose_name="Фактическая дата возврата")

    def __str__(self):
        return f"{self.copy} -> {self.reader}"