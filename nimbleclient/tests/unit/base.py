# -*- coding: utf-8 -*-

# Copyright 2016 Huawei, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from osc_lib.tests import utils

from nimbleclient.tests.unit import fakes


class TestBase(utils.TestCommand):
    """Test case base class for all unit tests."""
    pass


class TestBaremetalComputeV1(TestBase):
    """Test case base class for the unit tests of Baremetal Compute V1 API."""

    def setUp(self):
        super(TestBaremetalComputeV1, self).setUp()

        fake_client = fakes.FakeBaremetalComputeV1Client()
        self.app.client_manager.baremetal_compute = fake_client
