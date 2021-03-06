#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import pytest


@pytest.fixture(autouse=True)
def revision():
    """Sets up the revision counter for each test call."""
    from pootle.core.models import Revision
    Revision.initialize(force=True)
