from django.db import models

# Create your models here.

class Blogs(models.Model):
    blog_title=models.CharField(max_length=100)
    blog_body=models.TextField()

    def __str__(self):
        return self.blog_title
class Comments(models.Model):
    # CASCADE is a rule in databases that automatically deletes related records when a record they depend on is deleted.
    blog=models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='comments')
    # ForeignKey is creating one(Blogs) to many(Comments) relation here
    # there are two more relation like this models.OneToOneField and models.ManyToManyField
    
    # about related_name'comments'
    # The related_name='comments' attribute lets you access all comments 
    # for a specific blog post directly from the blog object itself. 
    # It creates a convenient reverse relationship.
    comment=models.TextField()

    def __str__(self):
        return self.comment


