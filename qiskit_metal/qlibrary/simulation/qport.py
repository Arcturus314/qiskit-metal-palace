from qiskit_metal import draw, Dict
from qiskit_metal.toolbox_metal import math_and_overrides
from qiskit_metal.qlibrary.core import QComponent

class QPort(QComponent):
    
    # generates a simple rectangular port
    # copied from example here: https://qiskit.org/documentation/metal/tut/2-From-components-to-chip/2.31-Create-a-QComponent-Basic.html

    default_options = Dict(width='10um',
                           pos_x='0um',
                           pos_y='0um',
                           orientation='0',
                           layer='1')
    
    options = Dict(connector_gap='10um',
                   connector_height='10um')
    
    component_metadata = Dict(short_name='qport',
                             _qgeometry_table_poly='True')
    
    def make(self):
        p = self.parse_options()  # Parse the string options into numbers
            
        dist_from_center = (p.connector_gap + p.connector_height)/2
        gap = p.connector_gap
            
        if p.orientation == 0: rect = draw.rectangle(p.width, gap, p.pos_x, p.pos_y-dist_from_center)
        elif p.orientation == 180: rect = draw.rectangle(p.width, gap, p.pos_x, p.pos_y+dist_from_center)
        
        else: print("COMPONENT ORIENTATION NOT IN ASSIGNED GROUP")

        geom = {'qport_rect': rect}
        self.add_qgeometry('poly', geom, layer=p.layer, subtract=False)