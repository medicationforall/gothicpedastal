import cadquery as cq
from skirmishbunker import Bunker
from cadqueryhelper import shape

def custom_cut_window(self):
    cut_width = self.inset+self.wall_width
    if self.inset < 0:
        cut_width= (-1*(self.inset))+20

    height = self.height
    p_length = self.window_length+10
    padding = self.panel_padding
    p_height = height - self.panel_padding

    inner_inner_arch = (
        shape.arch_pointed(
            p_length + self.arch_padding_sides - self.inner_arch_sides-3,
            cut_width ,
            height - padding + self.arch_padding_top - self.inner_arch_top-9,
            ((height - padding)/2) + self.arch_inner_height - self.inner_arch_sides
        )
        .translate((0,0,1*(p_height/2)+2.75))
        .rotate((0,0,1),(0,0,0),180)
        .rotate((1,0,0),(0,0,0),self.angle-90)
        .translate((0,0,-1*(height/2)))
    )

    return inner_inner_arch

def custom_window(self):
    window = cq.Workplane("XY").box(10,10,10)

    height = self.height
    p_length = self.window_length-2
    padding = self.panel_padding
    p_height = height - self.panel_padding

    arch = shape.arch_pointed(
        18,
        3,
        117,
        37
    )

    cut_arch =  shape.arch_pointed(
        9,
        4,
        90,
        34
    )

    arch = arch.cut(cut_arch.translate((0,0,-2)))

    arches = (
        cq.Workplane("XY")
        .union(arch.translate((-6.4,3,-2)))
        .union(arch.translate((6.4,3,-2)))
        #.translate((0,10,1*(p_height/2)+2.75))
        .rotate((1,0,0),(0,0,0),self.angle-90)
        .translate((0,0,-9))
    )
    return arches

bp = Bunker()
bp.length = 200
bp.width = 200
bp.height = 140
bp.base_height=10
bp.inset=10
bp.render_floor_tiles = True
bp.render_ladders = False
bp.render_roof = True
bp.render_doors = False
bp.render_interior = True
bp.render_windows = True
bp.render_pips = True
bp.render_magnets = True
bp.wall_width = 7
bp.skip_windows = []
bp.custom_cut_window = custom_cut_window
bp.custom_cut_window_padding = -3
bp.custom_window = custom_window
bp.custom_window_padding = -8
bp.window_height = 90

bp.make()
body = bp.build_body()
roof = bp.build_roof()



#show_object(body)
cq.exporters.export(body, 'stl/gothic_pedastal_arch.stl')
#cq.exporters.export(roof, 'stl/gothic_pedastal_roof.stl')