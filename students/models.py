from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    FIRST_YEAR = 'first'
    SECOND_YEAR = 'second'
    THIRD_YEAR = 'third'
    FOURTH_YEAR = 'fourth'

    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST_YEAR, 'первый курс'),
        (SECOND_YEAR, 'второй курс'),
        (THIRD_YEAR, 'третий курс'),
        (FOURTH_YEAR, 'четвертый курс'),
    ]

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    year = models.CharField(max_length=6, choices=YEAR_IN_SCHOOL_CHOICES, default=FIRST_YEAR, verbose_name='Курс')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['last_name']


# class Student(models.Model):
#     first_name = models.CharField(max_length=150, verbose_name='Имя')
#     last_name = models.CharField(max_length=150, verbose_name='Фамилия', unique=True)
#     age = models.IntegerField(help_text='Введите возраст')
#     is_activ = models.BooleanField(default=True)
#     description = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='photos/', verbose_name='Фотография')
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag)
#
#     STATUS_CHOICES = [
#         ('draft', 'Draft'),
#         ('published', 'Published')
#     ]
#
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     class Meta:
#         verbose_name = 'студент'
#         verbose_name_plural = 'студенты'
#         ordering = ['last_name']
#         db_table = 'custom_table_name'

# class Group(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
#
#     def __str__(self):
#         return self.name


