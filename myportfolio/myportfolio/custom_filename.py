from django.core.files.storage import FileSystemStorage

class NoUnderscoreStorage(FileSystemStorage):
    def get_valid_name(self, name):
        return name
