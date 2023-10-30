
class Point:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class InderpolationInfo:
    def __init__(self):
        self.order = []  # point_name1, point_name2, ....
        self.names_to_points = {}  # point_name: Point
        self.names_to_parents_names = {}  # point_name: parent_point_name
        self.names_to_parent_linking = {}  # point_name: True/False

    def add(self, u, v, name, parent_name=None, is_linked=False):
        point = Point(u=u, v=v)
        self.names_to_points[name] = point
        self.names_to_parents_names[name] = parent_name
        self.order.append(name)
        self.names_to_parent_linking[name] = is_linked

    def get_u_by_name(self, name):
        return self.names_to_points[name].u

    def get_v_by_name(self, name):
        return self.names_to_points[name].v





if __name__ == '__main__':
    interpolation_info = InderpolationInfo()

    interpolation_info.add(u=14, v=6, name='first', parent_name=None)
    interpolation_info.add(u=4, v=14, name='second', parent_name='first', is_linked=True)
    interpolation_info.add(u=-5, v=14, name='third', parent_name='first', is_linked=True)








