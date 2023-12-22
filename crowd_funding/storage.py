from django.core.files.storage import FileSystemStorage


class ProjectImageStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None):
        if location is None:
            location = 'project_images/'
        super().__init__(location, base_url)


class UserProfileImageStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None):
        if location is None:
            location = 'user_profile_images/'
        super().__init__(location, base_url)
