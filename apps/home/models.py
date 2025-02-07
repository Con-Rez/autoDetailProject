from django.db import models
import os

# Photo model defined, represents a photo with a title, image, and description
class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps/home/static/imgs/') # Where new images are uploaded to
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        try:
            this = Photo.objects.get(id=self.id)
            if this.image != self.image:
                old_image_path = this.image.path # The path to the old image
                super(Photo, self).save(*args, **kwargs) # Save the new image to the database
                if os.path.exists(old_image_path): # If the old image exists
                    os.remove(old_image_path) # Remove the old image
                new_image_path = self.image.path # The path to the new image
                os.rename(new_image_path, old_image_path) # Rename the new image to the old image
                self.image.name = os.path.basename(old_image_path) # Set the image name to the old image name
        except Photo.DoesNotExist:
            super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
