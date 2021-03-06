# -*- coding: utf-8 -*-
"""Mixins to be implemented by user."""
from pyecore.ecore import EDerivedCollection


class DerivedDerived(EDerivedCollection):
    pass


class DerivedDerivedfrom(EDerivedCollection):
    pass


class DerivedRefinedby(EDerivedCollection):
    pass


class DerivedSatisfiedby(EDerivedCollection):
    pass


class DerivedTracedto(EDerivedCollection):
    pass


class DerivedVerifiedby(EDerivedCollection):
    pass


class RequirementMixin:
    """User defined mixin class for Requirement."""

    @property
    def master(self):
        raise NotImplementedError("Missing implementation for master")

    def __init__(
        self,
        *,
        base_Class=None,
        derived=None,
        derivedFrom=None,
        id=None,
        master=None,
        refinedBy=None,
        satisfiedBy=None,
        text=None,
        tracedTo=None,
        verifiedBy=None,
        **kwargs,
    ):
        super().__init__()


class TestCaseMixin:
    """User defined mixin class for TestCase."""

    def __init__(self, *, base_Behavior=None, base_Operation=None, **kwargs):
        super().__init__()


class TraceMixin:
    """User defined mixin class for Trace."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_traced_from(self, ref=None, result=None):

        raise NotImplementedError("operation get_traced_from(...) not yet implemented")


class RefineMixin:
    """User defined mixin class for Refine."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_refines(self, ref=None, result=None):

        raise NotImplementedError("operation get_refines(...) not yet implemented")


class CopyMixin:
    """User defined mixin class for Copy."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DeriveReqtMixin:
    """User defined mixin class for DeriveReqt."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SatisfyMixin:
    """User defined mixin class for Satisfy."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_satisfies(self, ref=None, result=None):

        raise NotImplementedError("operation get_satisfies(...) not yet implemented")


class VerifyMixin:
    """User defined mixin class for Verify."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_verifies(self, ref=None, result=None):

        raise NotImplementedError("operation get_verifies(...) not yet implemented")
