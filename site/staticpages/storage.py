from django.contrib.staticfiles.storage import StaticFilesStorage, CachedStaticFilesStorage

from require.storage import OptimizedStaticFilesStorage
from pipeline.storage import PipelineStorage

class RequirePipelineStorage(OptimizedStaticFilesStorage, PipelineStorage, StaticFilesStorage):
    pass