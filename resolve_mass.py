import xml.etree.ElementTree as ET
import os
import sys

def get_robot_name(urdf_file):
    tree = ET.parse(urdf_file)
    root = tree.getroot()

    robot_name = root.get('name')
    return robot_name

def get_link_masses(urdf_file):
    tree = ET.parse(urdf_file)
    root = tree.getroot()

    link_masses = {}
    for link in root.findall('link'):
        link_name = link.get('name')
        inertial = link.find('inertial')
        if inertial is not None:
            mass = float(inertial.find('mass').get('value'))
            link_masses[link_name] = mass

    return link_masses

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
# print("script_path = %s" % script_dir)
if len(sys.argv) > 1: # for example: b1_description/xacro/b1.urdf
    urdf_file = script_dir +  "/" + sys.argv[1]
else:
    print("Please provide the URDF file path as a command-line argument.")
    sys.exit(1)

urdf_file = "/home/wang/forest_ws/install/share/centauro_urdf/urdf/centauro.urdf"


link_masses = get_link_masses(urdf_file)
upper_masses = 0
lower_masses = 0
total_masses = 0
for link_name, mass in link_masses.items():
    total_masses += mass
    # print(f"Link link_name has a mass of 'mass' kg")

robot_name = get_robot_name(urdf_file)

print("---- robot " + robot_name + " info----")
print("Total mass of the robot: " + str(total_masses) + " kg")
print("--------------------------------------")

