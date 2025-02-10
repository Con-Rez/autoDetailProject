from django.db import models
import os

# Photo model defined, represents a photo with a title, image, and description
IMGSPATH = 'apps/home/static/imgs/'
class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=IMGSPATH) # Where new images are uploaded to
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs): #self=title of database entry, 
        # output the function arguments
        try:
            # Attempt getting the currently uploaded image as (this)
            this = Photo.objects.get(id=self.id) 
            # If the image has changed (this image is different from image being replaced)
            if this.image != self.image: 
                # Save new image to database
                old_image_path = this.image.path # Make a copy of the old image path
                super(Photo, self).save(*args, **kwargs) # Save the new image to the database
                
                # Remove the old image
                if os.path.exists(old_image_path): # If the old image exists
                    os.remove(old_image_path) # Remove the old image

                # Rename the new image to the old image
                new_image_path = self.image.path # The path to the new image
                os.rename(new_image_path, old_image_path) # Rename the new image to the old image
                
                # Set the image name to the old image name with the correct path
                print(IMGSPATH + os.path.basename(old_image_path))
                self.image.name = IMGSPATH + os.path.basename(old_image_path) # Set the image name to the old image name with the correct path
                super(Photo, self).save(*args, **kwargs) # Save the new image to the database again
        except Photo.DoesNotExist:
            super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
