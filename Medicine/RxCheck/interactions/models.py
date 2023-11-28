from django.db import models


class Drug(models.Model):
    # model representing user's Drug information
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    instructions = models.TextField(max_length=1000, help_text="Enter the instructions for "
                                                               "your medication", null=True)

    def __str__(self):
        # string for representing the model object
        return self.name

    def save(self, *args, **kwargs):
        # override the save method to create Drug_History instance automatically
        is_new_drug = not self.pk  # Check if it's a new Drug instance
        super(Drug, self).save(*args, **kwargs)  # Call the original save method

        if is_new_drug:
            # If it's a new Drug instance, create a Drug_History entry
            Drug_History.objects.create(drug=self)

class Drug_History(models.Model):
    # model representing user's Drug history
    id = models.AutoField(primary_key=True)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)

    def __str__(self):
        # string for representing the model object
        return f"History for user"
