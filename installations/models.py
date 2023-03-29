from django.db import models
from vehicles.models import Vehicle
from inventory.models import TrackerDevice, Sim
from customers.models import Customer
from accounts.models import UserProfile
from companies.models import Company


class TrackerInstallation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='tracker_installations')
    tracker_device = models.ForeignKey(TrackerDevice, on_delete=models.CASCADE)
    sim = models.ForeignKey(Sim, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='tracker_installations')
    installed_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='tracker_installations')
    installed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle} - {self.tracker_device}"

    class Meta:
        unique_together = ['vehicle', 'tracker_device', 'sim']