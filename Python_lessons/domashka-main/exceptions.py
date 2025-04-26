# exceptions.py

class ContactNotFoundError(Exception):
    """Raised when a contact is not found in the phonebook."""
    pass


class InvalidContactError(Exception):
    """Raised when contact information is invalid."""
    pass


class FileOperationError(Exception):
    """Raised when a file operation fails."""
    pass
