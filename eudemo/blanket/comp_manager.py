# SPDX-FileCopyrightText: 2021-present M. Coleman, J. Cook, F. Franza
# SPDX-FileCopyrightText: 2021-present I.A. Maione, S. McIntosh
# SPDX-FileCopyrightText: 2021-present J. Morris, D. Short
#
# SPDX-License-Identifier: LGPL-2.1-or-later
"""Component Manager"""

from bluemira.base.components import Component
from bluemira.base.reactor import ComponentManager
from bluemira.geometry.coordinates import Coordinates


class Blanket(ComponentManager):
    """Wrapper around a Blanket component tree."""

    def __init__(
        self, component_tree: Component, panel_points: Coordinates, r_inner_cut: float
    ):
        self.r_inner_cut = r_inner_cut
        self._panel_points = panel_points
        super().__init__(component_tree)

    @property
    def panel_points(self) -> Coordinates:
        """
        Returns
        -------
        :
            The panel points of the blanket.
        """
        return self._panel_points
