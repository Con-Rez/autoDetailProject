from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError
import datetime
import os

class Service(models.Model):
    name = models.CharField(max_length=100, blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    time_to_complete = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Photo model defined, represents a photo with a title, image, and description
IMGSPATH = 'apps/home/static/imgs/'
class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=IMGSPATH) # Where new images are uploaded to
    description = models.TextField(blank=True)

    def clean(self): # function checks size and orientation of the photos that change in the gallery
        
        if self.image:
            if hasattr(self.image, 'width') and hasattr(self.image, 'height'): # size check, normallay the images are 3024x4032
                if self.image.width < 2000 or self.image.height < 3000: # these parameters will only make the images slightly smaller and not affect page too much
                    raise ValidationError("Image too small. Width should be greater than 2000 and Height should be greater than 3000.")
                
                if self.image.width > self.image.height: # see if image is vertical, try to keep vertical slider images
                    raise ValidationError("Image must be vertical. Height should be greater than width.") # prevents horizontal images from messing with the webpage
                    

    def save(self, *args, **kwargs): #self=title of database entry, 
        self.full_clean()  # This runs the clean() method before saving
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
            else:
                super(Photo, self).save(*args, **kwargs)
        except Photo.DoesNotExist:
            super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# New model for Video transformations
VIDEOSPATH = 'apps/home/static/videos/'
class TransformationVideo(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to=VIDEOSPATH)  # Where new videos are uploaded to
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)  # Use this to control the display order in the carousel
    
    def clean(self):
        # Validate video file extension
        if self.video:
            ext = os.path.splitext(self.video.name)[1].lower()
            if ext not in ['.mp4', '.mov', '.avi', '.webm']:
                raise ValidationError("Unsupported file format. Please upload MP4, MOV, AVI, or WebM files.")
    
    def save(self, *args, **kwargs):
        self.full_clean()  # This runs the clean() method before saving
        try:
            # Check if this video already exists in the database
            this = TransformationVideo.objects.get(id=self.id)
            # If the video has changed
            if this.video != self.video:
                # Save new video to database
                old_video_path = this.video.path
                super(TransformationVideo, self).save(*args, **kwargs)
                
                # Remove the old video
                if os.path.exists(old_video_path):
                    os.remove(old_video_path)
                
                # Rename the new video to the old video
                new_video_path = self.video.path
                os.rename(new_video_path, old_video_path)
                
                # Set the video name to the old video name with the correct path
                print(VIDEOSPATH + os.path.basename(old_video_path))
                self.video.name = VIDEOSPATH + os.path.basename(old_video_path)
                super(TransformationVideo, self).save(*args, **kwargs)
            else:
                super(TransformationVideo, self).save(*args, **kwargs)
        except TransformationVideo.DoesNotExist:
            super(TransformationVideo, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    link = models.URLField()
    STAR_RATINGS = [(1, '1'), (2, '2'), (3, '3'), 
                   (4, '4'), (5, '5')]
    stars = models.IntegerField(choices=STAR_RATINGS, blank=False)

    def __str__(self):
        return self.title
        
    def get_star_range(self):
        return range(self.stars)
    
#discountModal feature update
class Promotion(models.Model):
    name = models.CharField(max_length=100)  # Name of Promotion
    code = models.CharField(max_length=50, unique=True)  # Code for Promotion
    message = models.TextField()  # Message Displayed on Appointments Page
    discount_percentage = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    start_date = models.DateField()  # When the promotion becomes active
    end_date = models.DateField()    # When the promotion ends

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date must be before end date.")
        if self.discount_percentage <= 0 or self.discount_percentage > 100:
            raise ValidationError("Discount percentage must be between 0 and 100.")

    def __str__(self):
        return self.name