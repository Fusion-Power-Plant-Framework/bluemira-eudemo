# SPDX-FileCopyrightText: 2021-present M. Coleman, J. Cook, F. Franza
# SPDX-FileCopyrightText: 2021-present I.A. Maione, S. McIntosh
# SPDX-FileCopyrightText: 2021-present J. Morris, D. Short
#
# SPDX-License-Identifier: LGPL-2.1-or-later

from contextlib import suppress
from unittest import mock

import matplotlib as mpl


def pytest_addoption(parser):
    """Adds a custom command line option to pytest to control plotting."""
    parser.addoption(
        "--plotting-on",
        action="store_true",
        default=False,
        help="switch on interactive plotting in tests",
    )


def pytest_configure(config):
    """Configures pytest with the plotting command line option."""
    if not config.option.plotting_on:
        # We're not displaying plots so use a display-less backend
        mpl.use("Agg")
        # Disable CAD viewer by mocking out every show_cad entry point.
        # The ``_geometryapi`` dispatcher star-imports from the active backend
        # (`_freecad.api` or `_cadquery`), which binds ``show_cad`` on
        # ``_geometryapi`` at import time — patching the underlying backend
        # alone does NOT propagate, so we mock all three module-level names.
        with suppress(ImportError):
            mock.patch("bluemira.codes._polyscope.ps").start()
        for name in (
            "bluemira.codes.cadapi._freecad.api.show_cad",
            "bluemira.codes.cadapi._cadquery.show_cad",
            "bluemira.codes._geometryapi.show_cad",
        ):
            with suppress(ImportError, AttributeError):
                mock.patch(name).start()
