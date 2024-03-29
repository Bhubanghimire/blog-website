from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager  ## A new class is imported. ##
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, UserManager):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    image = models.ImageField(upload_to='image/user/')


class Category(models.Model):
    category = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=200, default="")
    post = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='image/post/', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default="adminn@gmail.com")
    created_date = models.DateField(auto_now=True)
    order = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-order',)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    @property
    def image_preview(self):
        if self.image:
            for i in range(2):
                return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return ""


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comment")
    comment = models.TextField()
    likes = models.ManyToManyField(User, related_name='comment_like')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="cmnts")
    created_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return self.comment

    def number_of_likes(self):
        return self.likes.count()


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name


class Reply(models.Model):
    reply_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user_reply")
    reply = models.CharField(max_length=20000)
    reply_to = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, related_name="reply_post")
    created_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return str(self.reply_by)


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return ""
