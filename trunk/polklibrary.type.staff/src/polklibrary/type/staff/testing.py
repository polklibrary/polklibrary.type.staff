# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import polklibrary.type.staff


class PolklibraryTypeStaffLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=polklibrary.type.staff)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'polklibrary.type.staff:default')


POLKLIBRARY_TYPE_STAFF_FIXTURE = PolklibraryTypeStaffLayer()


POLKLIBRARY_TYPE_STAFF_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLKLIBRARY_TYPE_STAFF_FIXTURE,),
    name='PolklibraryTypeStaffLayer:IntegrationTesting'
)


POLKLIBRARY_TYPE_STAFF_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLKLIBRARY_TYPE_STAFF_FIXTURE,),
    name='PolklibraryTypeStaffLayer:FunctionalTesting'
)


POLKLIBRARY_TYPE_STAFF_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLKLIBRARY_TYPE_STAFF_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PolklibraryTypeStaffLayer:AcceptanceTesting'
)
