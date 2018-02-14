import h5py
import meshio

class MeshStorage:

    def __init__(self, hfd5_filename):
        self.storage_file = h5py.File(hfd5_filename, 'w', driver='core')

    def load_file(self, mesh_filename):
        self.points, self.cells, self.point_data, self.cell_data, self.field_data = meshio.read(mesh_filename)

        # self.mesh_data = h5py.File("new_mesh.hdf5", 'w')
        #
        # self.all_entities = self.mesh_data.create_group('all_entities')
        # self.node_data = self.all_entities.create_group('node_data')
        # self.line_data = self.all_entities.create_group('line_data')
        # self.cell_2D_data = self.all_entities.create_group('cell_2D_data')
        # self.cell_3D_data = self.all_entities.create_group('cell_3D_data')
        #
        # self.field_h5dir = self.mesh_data.create_group('fields')
