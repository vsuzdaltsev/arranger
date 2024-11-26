"""Methods common for BasicService and other Basic abstract libraries."""

from functools import reduce


class BasicMixin:
    """Generate all related K8s manifests."""

    def _common_labels(self, resource_name):
        service_name_label = (
            {"service": self.service_name}
            if hasattr(self, "service_name")
            else {"service": self.service_name_from_class_name}
        )

        return {"resource_name": resource_name} | service_name_label

    @property
    def service_name_from_class_name(self):
        return reduce(
            lambda x, y: x + ("-" if y.isupper() else "") + y, self.__class__.__name__
        ).lower()
