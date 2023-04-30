import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company
from phonenumber_field.modelfields import PhoneNumberField
from django.core.files.storage import default_storage,FileSystemStorage


def user_directory_path(instance, filename):
    return f'accounts/user_{instance.id}/documents/{filename}'

class UserType(models.Model):
    usertype = models.CharField(max_length=255)
    datentime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.usertype

class UserProfile(AbstractUser):
    # is_manager  = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    # is_installer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='owned_companies')
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True, related_name='owned_companies')
    contact_number_1 = PhoneNumberField(blank=True, null=True) # use CharField if you don't want to use PhoneNumberField
    contact_number_2 = PhoneNumberField(blank=True, null=True)
    nic = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    refrence = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(upload_to='accounts/user_None/documents', blank=True, null=True)


    def save(self, *args, **kwargs):
        # Check if a document is being uploaded
        if self.document:
            old_document_path = self.document.path

        # Save the instance (This will populate the id field if it's a new instance)
        super(UserProfile, self).save(*args, **kwargs)

        # Check if a document is being uploaded
        if self.document:
            new_document_folder = f"accounts/user_{self.id}/documents/"
            new_document_path = os.path.join(new_document_folder, os.path.basename(self.document.name))

            # If the new_document_path is different from the old_document_path, move the file to the new location
            if old_document_path != default_storage.path(new_document_path):
                if not default_storage.exists(new_document_folder):
                    os.makedirs(default_storage.path(new_document_folder))
                fs = FileSystemStorage()
                fs.save(new_document_path, self.document.file)
                fs.delete(old_document_path)
                self.document.name = new_document_path
                # Save the instance again to update the document field
                super(UserProfile, self).save(update_fields=['document'])


class ContactNumber(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='contact_numbers')
    number = PhoneNumberField()

    def __str__(self):
        return str(self.number)

class UserDocument(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.description or self.document.name