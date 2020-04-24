from django.db import models

class Movie(models.Model):
    """
    Represents a movie
    """
    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'

    name = models.CharField(max_length=100,verbose_name='عنوان فیلم')
    director = models.CharField(max_length=50,verbose_name='کارگردان')
    year = models.IntegerField(verbose_name='سال')
    length = models.IntegerField(verbose_name='مدت زمان')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.name

class Cinema(models.Model):
    """
    represents a Cinema
    """
    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'

    cinema_code = models.IntegerField('کد فیلم',primary_key=True)
    name = models.CharField('نام سینما',max_length=50)
    city = models.CharField('شهر',max_length=50,default='تهران')
    capacity = models.IntegerField('ظرفیت سینما')
    phone = models.CharField('تلفن',max_length=20,null=True)
    address =models.TextField('آدرس')

    def __str__(self):
        return self.name

class ShowTime(models.Model):
    """
    Represents a movie show in cinema at a specific time
    """

    class Meta:
        verbose_name = 'سانس فیلم'
        verbose_name_plural = 'سانس فیلم'

    movie = models.ForeignKey('Movie',on_delete = models.PROTECT,verbose_name='فیلم' )
    cinema = models.ForeignKey('Cinema',on_delete = models.PROTECT,verbose_name='سینما')
    start_time = models.DateTimeField('تاریخ')
    price = models.IntegerField('مبلغ')
    salable_seats = models.IntegerField('قابل فروش')
    free_seats = models.IntegerField('صندلی های خالی')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    SOLD_OUT = 3
    MOVIE_PLAYED = 3
    SHOW_CANCELED = 4
    status_choices = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده'),
        (SALE_OPEN,'در حال فروش بلیت'),
        (SOLD_OUT, 'اتمام بلیت'),
        (MOVIE_PLAYED, 'غیلم پخش شد'),
        (SHOW_CANCELED,'سانس لفو شد')
    )
    status = models.IntegerField(choices=status_choices,verbose_name='وضعیت')

    def __str__(self):
        return('{} {} {}'.format(self.movie,self.cinema,self.start_time))