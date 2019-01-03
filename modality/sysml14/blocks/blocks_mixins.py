# -*- coding: utf-8 -*-
"""Mixins to be implemented by user."""
from pyecore.ecore import EDerivedCollection


class AdjunctPropertyMixin:
    """User defined mixin class for AdjunctProperty."""

    def __init__(self, *, base_Property=None, principal=None, **kwargs):
        super().__init__()


class BindingConnectorMixin:
    """User defined mixin class for BindingConnector."""

    def __init__(self, *, base_Connector=None, **kwargs):
        super().__init__()


class BlockMixin:
    """User defined mixin class for Block."""

    def __init__(self, *, base_Class=None, isEncapsulated=None, **kwargs):
        super().__init__()

    def get_references(self):
        """@papyrus.req org.eclipse.papyrus.sysml14#REQ-SYSML14-Block-References"""
        raise NotImplementedError("operation get_references(...) not yet implemented")

    def get_parts(self):

        raise NotImplementedError("operation get_parts(...) not yet implemented")

    def get_flow_properties(self):

        raise NotImplementedError(
            "operation get_flow_properties(...) not yet implemented"
        )


class EndPathMultiplicityMixin:
    """User defined mixin class for EndPathMultiplicity."""

    def __init__(self, *, base_Property=None, lower=None, upper=None, **kwargs):
        super().__init__()


class ClassifierBehaviorPropertyMixin:
    """User defined mixin class for ClassifierBehaviorProperty."""

    def __init__(self, *, base_Property=None, **kwargs):
        super().__init__()


class ConnectorPropertyMixin:
    """User defined mixin class for ConnectorProperty."""

    def __init__(self, *, base_Property=None, connector=None, **kwargs):
        super().__init__()


class DistributedPropertyMixin:
    """User defined mixin class for DistributedProperty."""

    def __init__(self, *, base_Property=None, **kwargs):
        super().__init__()


class ElementPropertyPathMixin:
    """User defined mixin class for ElementPropertyPath."""

    def __init__(self, *, base_Element=None, propertyPath=None, **kwargs):
        super().__init__()


class ParticipantPropertyMixin:
    """User defined mixin class for ParticipantProperty."""

    def __init__(self, *, base_Property=None, end=None, **kwargs):
        super().__init__()


class PropertySpecificTypeMixin:
    """User defined mixin class for PropertySpecificType."""

    def __init__(self, *, base_Classifier=None, **kwargs):
        super().__init__()


class ValueTypeMixin:
    """User defined mixin class for ValueType."""

    def __init__(self, *, base_DataType=None, quantityKind=None, unit=None, **kwargs):
        super().__init__()


class DirectedRelationshipPropertyPathMixin:
    """User defined mixin class for DirectedRelationshipPropertyPath."""

    def __init__(
        self,
        *,
        base_DirectedRelationship=None,
        sourceContext=None,
        sourcePropertyPath=None,
        targetContext=None,
        targetPropertyPath=None,
        **kwargs,
    ):
        super().__init__()


class DerivedBindingpath(EDerivedCollection):
    pass


class BoundReferenceMixin:
    """User defined mixin class for BoundReference."""

    def __init__(self, *, bindingPath=None, boundEnd=None, **kwargs):
        super().__init__(**kwargs)


class NestedConnectorEndMixin:
    """User defined mixin class for NestedConnectorEnd."""

    def __init__(self, *, base_ConnectorEnd=None, **kwargs):
        super().__init__(**kwargs)
