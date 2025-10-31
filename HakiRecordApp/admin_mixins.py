import json
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType

class DetailedChangeLoggerMixin:
    """Mixin to log detailed changes (old → new) in Django admin."""

    def log_change(self, request, object, message):
        old_object = self.model.objects.get(pk=object.pk)
        changes = {}
        for field in self.model._meta.fields:
            field_name = field.name
            old_value = getattr(old_object, field_name)
            new_value = getattr(object, field_name)
            if old_value != new_value:
                changes[field.verbose_name] = {"old": old_value, "new": new_value}

        LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=ContentType.objects.get_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=json.dumps({"detailed_changes": changes}),
        )