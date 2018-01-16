# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ukbg.medienportal


class UkbgMedienportalLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ukbg.medienportal)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ukbg.medienportal:default')


UKBG_MEDIENPORTAL_FIXTURE = UkbgMedienportalLayer()


UKBG_MEDIENPORTAL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UKBG_MEDIENPORTAL_FIXTURE,),
    name='UkbgMedienportalLayer:IntegrationTesting'
)


UKBG_MEDIENPORTAL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UKBG_MEDIENPORTAL_FIXTURE,),
    name='UkbgMedienportalLayer:FunctionalTesting'
)


UKBG_MEDIENPORTAL_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UKBG_MEDIENPORTAL_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='UkbgMedienportalLayer:AcceptanceTesting'
)
