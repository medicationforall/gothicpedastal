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
bp.render_roof = False
bp.render_doors = False
bp.render_interior = True
bp.render_windows = True
bp.wall_width = 7
bp.skip_windows = []
bp.window_height = 50

bp.make()
bunker = bp.build()

show_object(bunker)
#cq.exporters.export(bunker, 'stl/gothic_pedastal_with_roof.stl')
