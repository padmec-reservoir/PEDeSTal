import unittest
import h5py
from ..meshmanager import MeshManager

class MeshManagerTest(unittest.TestCase):

    def setUp(self):
        self.mesh = MeshManager()
        self.file_instance = h5py.File('storage_test.hdf5', 'w', driver='core', backing_store=False)

    def tearDown(self):
        self.file_instance.close()

    def test_hdf5_file_loading(self):
        """
        Test if HDF5 file has been loaded upon instanciation
        Asserts with the name of the root dir of hdf5 file
        """
        self.assertEqual(self.mesh.storage_file.name, self.file_instance.name)
