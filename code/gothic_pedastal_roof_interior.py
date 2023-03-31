import cadquery as cq
from skirmishbunker import Bunker

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
bp.window_height = 50

bp.make()
body = bp.build_body()
roof = bp.build_roof()


show_object(body)
#cq.exporters.export(body, 'stl/gothic_pedastal_body.stl')
#cq.exporters.export(roof, 'stl/gothic_pedastal_roof.stl')