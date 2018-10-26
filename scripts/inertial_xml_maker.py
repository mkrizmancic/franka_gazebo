from __future__ import print_function


def print_xml(i, s, m, v, com, d):
    v = v / s**3
    com = [x / s for x in com]

    for key in d.keys():
        d[key] = d[key] / s**5 * m / v

    print("link_{}".format(i))
    print("<inertial>")
    print("  <mass value=\"{}\" />".format(m))
    print("  <origin xyz=\"{} {} {}\" rpy=\"0 0 0\" />".format(com[0], com[1], com[2]))
    print("  <inertia ixx=\"{ixx}\" ixy=\"{ixy}\" ixz=\"{ixz}\" iyy=\"{iyy}\" iyz=\"{iyz}\" izz=\"{izz}\" />".format(**d))
    print("</inertial>")
    print()

    return


if __name__ == '__main__':
    s = 10

    # link_0
    m = 2.92
    v = 2.441565
    com = (-0.255660, -0.000288, 0.573320)
    d = {'ixx': 0.654063, 'ixy': -0.001306, 'ixz': -0.105360, 'iyy': 0.911640, 'iyz': 0.000905, 'izz': 0.855848}
    print_xml(0, s, m, v, com, d)

    # link_1
    m = 2.74
    v = 2.293251
    com = (0, -0.324958, -0.675818)
    d = {'ixx': 1.510005, 'ixy': 0, 'ixz': 0, 'iyy': 1.331894, 'iyz': 0.391346, 'izz': 0.519489}
    print_xml(1, s, m, v, com, d)

    # link_2
    m = 2.74
    v = 2.312302
    com = (0, -0.686100, 0.322285)
    d = {'ixx': 1.543134, 'ixy': 0, 'ixz': 0, 'iyy': 0.524368, 'iyz': -0.399036, 'izz': 1.363029}
    print_xml(2, s, m, v, com, d)

    # link_3
    m = 2.38
    v = 2.020883
    com = (0.469893, 0.316374, -0.317040)
    d = {'ixx': 0.654984, 'ixy': -0.210996, 'ixz': -0.282030, 'iyy': 0.839862, 'iyz': -0.184933, 'izz': 0.689243}
    print_xml(3, s, m, v, com, d)

    # link_4
    m = 2.38
    v = 2.005719
    com = (-0.360446, 0.336853, 0.318820)
    d = {'ixx': 0.673908, 'ixy': 0.292511, 'ixz': -0.203288, 'iyy': 0.695589, 'iyz': 0.198696, 'izz': 0.863934}
    print_xml(4, s, m, v, com, d)

    # link_5
    m = 2.74
    v = 2.275315
    com = (0, 0.610427, -1.041760)
    d = {'ixx': 2.522060, 'ixy': 0.000054, 'ixz': -0.000873, 'iyy': 2.397824, 'iyz': -0.644108, 'izz': 0.368812}
    print_xml(5, s, m, v, com, d)

    # link_6
    m = 1.55
    v = 1.303586
    com = (0.510509, 0.091080, 0.106343)
    d = {'ixx': 0.255113, 'ixy': -0.036776, 'ixz': 0.052922, 'iyy': 0.340177, 'iyz': 0.010973, 'izz': 0.469488}
    print_xml(6, s, m, v, com, d)

    # link_7
    m = 0.54
    v = 0.454402
    com = (0.109695, 0.107965, 0.650411)
    d = {'ixx': 0.074797, 'ixy': -0.010299, 'ixz': 0.003355, 'iyy': 0.074724, 'iyz': -0.007858, 'izz': 0.060392}
    print_xml(7, s, m, v, com, d)

    # hand
    m = 0.73
    v = 0.487946
    com = (0, 0.015244, 0.275912)
    d = {'ixx': 0.186195, 'ixy': 0, 'ixz': 0, 'iyy': 0.026739, 'iyz': 0, 'izz': 0.171368}
    print_xml(10, s, m, v, com, d)

    # left_finger
    m = 0.1
    v = 0.011221
    com = (0, 0.145644, 0.227941)
    d = {'ixx': 0.000338, 'ixy': 0, 'ixz': 0, 'iyy': 0.000332, 'iyz': 0, 'izz': 0.000078}
    print_xml(11, s, m, v, com, d)

    # right_finger
    m = 0.1
    v = 0.011221
    com = (0, 0.145644, 0.227941)
    d = {'ixx': 0.000338, 'ixy': 0, 'ixz': 0, 'iyy': 0.000332, 'iyz': 0, 'izz': 0.000078}
    print_xml(12, s, m, v, com, d)