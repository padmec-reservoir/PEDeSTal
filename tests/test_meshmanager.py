import unittest
import h5py
import meshio

from PEDeSTal.meshmanager import MeshStorage
from unittest import mock


class MeshStorageTest(unittest.TestCase):

    def setUp(self):
        self.mesh = MeshStorage('storage.hdf5')

    def test_hdf5_file_loading(self):
        with mock.patch('PEDeSTal.meshmanager.h5py.File') as mock_hdf5:
            mesh = MeshStorage('storage.hdf5')
            mock_hdf5.assert_called_with('storage.hdf5', 'w', driver='core')

    def test_load_mesh_file(self):
        with mock.patch('PEDeSTal.meshmanager.meshio.read') as mock_open_mesh:
            mock_open_mesh.return_value = [1, 2, 3, 4, 5]
            self.mesh.load_file('geometry_test.msh')
            mock_open_mesh.assert_called_with('geometry_test.msh')

    def test_create_elements(self):
        pass
