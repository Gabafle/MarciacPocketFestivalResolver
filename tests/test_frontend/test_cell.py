import unittest

from backend.structure.Chair import Chair
from frontend.Cell import Cell, CellState


class TestCell(unittest.TestCase):

    def test_CreateCellWithRow(self):
        # Arrange
        expected_value = 1
        cell = Cell(1, 2, 3)

        # Act
        actual_value = cell.row

        # Assert
        self.assertEqual(actual_value, expected_value)

    def test_CreateCellDefaultState(self):
        # Arrange
        expected_state = CellState.AVAILABLE
        cell = Cell(1, 2, 3)

        # Act
        actual_state = cell.state

        # Assert
        self.assertEqual(actual_state, expected_state)

    def test_SetCellState(self):
        # Arrange
        expected_state = CellState.OCCUPIED
        cell = Cell(1, 2, 3, CellState.OCCUPIED)

        # Act
        actual_state = cell.state

        # Assert
        self.assertEqual(actual_state, expected_state)

    def test_CellSetAvailable(self):
        # Arrange
        expected_state = CellState.AVAILABLE
        cell = Cell(1, 2, 3, CellState.OCCUPIED)
        cell.set_available()

        # Act
        actual_state = cell.state

        # Assert
        self.assertEqual(actual_state, expected_state)

    def test_CellOccupy(self):
        # Arrange
        expected_occupant = Chair()
        expected_state = CellState.OCCUPIED
        cell = Cell(1, 2, 3)
        cell.occupy(Chair())

        # Act
        actual_occupant = cell.occupant
        actual_state = cell.state

        # Assert
        self.assertEqual(actual_occupant, expected_occupant)
        self.assertEqual(actual_state, expected_state)

    def test_CellBlocked(self):
        # Arrange
        expected_state = CellState.BLOCKED
        cell = Cell(1, 2, 3)
        cell.block_cell()

        # Act
        actual_state = cell.state

        # Assert
        self.assertEqual(actual_state, expected_state)
