from django.contrib import admin
from .models import MachineLearningPost, DeepLearningPost, DatasciencePost, RFLearningPost

# Register your models here.

admin.site.register(MachineLearningPost)
admin.site.register(DeepLearningPost)
admin.site.register(RFLearningPost)
admin.site.register(DatasciencePost)