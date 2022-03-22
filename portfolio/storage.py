from whitenoise.storage import CompressedManifestStaticFilesStorage


class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False
    STATICFILES_STORAGE = "whitenoise.django.GzipManifestStaticFilesStorage"
