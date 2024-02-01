# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from polklibrary.type.staff import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPolklibraryTypeStaffLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ITask(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )
