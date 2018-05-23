import warnings

from django.conf import settings


class ConfigWrapper(object):
    @staticmethod
    def alias_name():
        if hasattr(settings, 'DISCOVERY_PROFILE_NAME'):
            warnings.warn(
                "DISCOVERY_PROFILE_NAME is deprecated. Please use DISCOVERY_ALIAS_NAME instead.",
                DeprecationWarning
            )
            return settings.DISCOVERY_PROFILE_NAME
        else:
            return settings.DISCOVERY_ALIAS_NAME

    @staticmethod
    def is_read_only():
        return getattr(settings, 'DISCOVERY_READ_ONLY', False)

    @staticmethod
    def tables_include():
        return getattr(settings, 'DISCOVERY_INCLUDE', None) or None

    @staticmethod
    def tables_exclude():
        return getattr(settings, 'DISCOVERY_EXCLUDE', None) or None
