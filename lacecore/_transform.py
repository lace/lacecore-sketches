class Transform:
    def translate(self, translation):
        pass

    def recenter_at(self, coords):
        pass

    def recenter_at_centroid(self):
        pass

    def recenter_below_centroid(self):
        pass

    def rotate(self, rotation_matrix):
        pass

    def reorient(self, up, look):
        pass

    def scale(self, factor):
        pass

    def convert_units(self, from_units, to_units):
        pass

    def flip(self, axis, preserve_centroid):
        pass

    def flip_faces(self, face_indices_to_flip):
        pass
