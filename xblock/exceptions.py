"""
Module for all xblock exception classes
"""
import json

from webob import Response


class XBlockNotFoundError(Exception):
    """
    Raised to indicate that an XBlock could not be found with the requested usage_id
    """
    def __init__(self, usage_id):
        # Exception is an old-style class, so can't use super
        Exception.__init__(self)
        self.message = f"Unable to load an xblock for usage_id {usage_id!r}"


class XBlockSaveError(Exception):
    """
    Raised to indicate an error in saving an XBlock
    """
    def __init__(self, saved_fields, dirty_fields, message=None):
        """
        Create a new XBlockSaveError

        `saved_fields` - a set of fields that were successfully
        saved before the error occurred
        `dirty_fields` - a set of fields that were left dirty after the save
        """
        # Exception is an old-style class, so can't use super
        Exception.__init__(self)

        self.message = message
        self.saved_fields = saved_fields
        self.dirty_fields = dirty_fields


class KeyValueMultiSaveError(Exception):
    """
    Raised to indicated an error in saving multiple fields in a KeyValueStore
    """
    def __init__(self, saved_field_names):
        """
        Create a new KeyValueMultiSaveError

        `saved_field_names` - an iterable of field names (strings) that were
        successfully saved before the exception occurred
        """
        # Exception is an old-style class, so can't use super
        Exception.__init__(self)

        self.saved_field_names = saved_field_names


class InvalidScopeError(Exception):
    """
    Raised to indicated that operating on the supplied scope isn't allowed by a KeyValueStore
    """
    def __init__(self, invalid_scope, valid_scopes=None):
        super().__init__()
        if valid_scopes:
            self.message = "Invalid scope: {}. Valid scopes are: {}".format(
                invalid_scope,
                valid_scopes,
            )
        else:
            self.message = f"Invalid scope: {invalid_scope}"


class NoSuchViewError(Exception):
    """
    Raised to indicate that the view requested was not found.
    """
    def __init__(self, block, view_name):
        """
        Create a new NoSuchViewError

        :param block: The XBlock without a view
        :param view_name: The name of the view that couldn't be found
        """
        # Can't use super because Exception is an old-style class
        Exception.__init__(self)
        self.message = f"Unable to find view {view_name!r} on block {block!r}"


class NoSuchHandlerError(Exception):
    """
    Raised to indicate that the requested handler was not found.
    """


class NoSuchServiceError(Exception):
    """
    Raised to indicate that a requested service was not found.
    """


class NoSuchUsage(Exception):
    """Raised by :meth:`.IdReader.get_definition_id` if the usage doesn't exist."""


class NoSuchDefinition(Exception):
    """Raised by :meth:`.IdReader.get_block_type` if the definition doesn't exist."""


class JsonHandlerError(Exception):
    """
    Raised by a function decorated with XBlock.json_handler to indicate that an
    error response should be returned.
    """
    def __init__(self, status_code, message):
        super().__init__()
        self.status_code = status_code
        self.message = message

    def get_response(self, **kwargs):
        """
        Returns a Response object containing this object's status code and a
        JSON object containing the key "error" with the value of this object's
        error message in the body. Keyword args are passed through to
        the Response.
        """
        return Response(
            json.dumps({"error": self.message}),
            status_code=self.status_code,
            content_type="application/json",
            charset="utf-8",
            **kwargs
        )


class DisallowedFileError(Exception):
    """Raised by :meth:`.XBlock.open_local_resource` if the requested file is not allowed."""


class FieldDataDeprecationWarning(DeprecationWarning):
    """Warning for use of deprecated _field_data accessor"""


class UserIdDeprecationWarning(DeprecationWarning):
    """Warning for use of deprecated user_id accessor"""


class XBlockParseException(Exception):
    """
    Raised if parsing the XBlock olx fails.
    """
