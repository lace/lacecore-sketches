from blmath.util.decorators import setter_property


class MeshData:
    @property
    def attr_is_mutable(self, attr):
        pass

    @property
    def num_v(self):
        pass

    @setter_property
    def v(self, val):
        pass

    @setter_property
    def vc(self, val):
        pass

    @setter_property
    def vg(self, val):
        pass

    @property
    def num_f(self):
        pass

    @property
    def is_tri(self):
        pass

    @property
    def is_quad(self):
        pass

    @setter_property
    def f(self, val):
        pass

    @setter_property
    def fvn(self, val):
        pass

    @setter_property
    def fvt(self, val):
        pass

    @setter_property
    def fc(self, val):
        pass

    @setter_property
    def fg(self, val):
        pass
