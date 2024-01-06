import pygame
import cairo
import math

class Renderer:
    def __init__(self, buffer, width, height) -> None:
        self.shared_buffer = buffer
        self.width, self.height = width, height

    def render_stroke(self, stroke_points, pen):
        cairo_surface = cairo.ImageSurface.create_for_data(self.shared_buffer, cairo.FORMAT_ARGB32, self.width, self.height)
        context = cairo.Context(cairo_surface)
        for i in range(math.floor(len(stroke_points)/2-1)):
            # DEBUG: stroke as line segments for reference of what the spline should roughly look like
            context.set_line_width(0.75)
            context.set_source_rgb(0.0, 1.0, 0.0)
            context.move_to(stroke_points[2*i][0], stroke_points[2*i][1])
            context.line_to(stroke_points[2*(i+1)][0], stroke_points[2*(i+1)][1])
            context.stroke()
            # pygame.draw.line(self.target, '#00FF00', stroke_points[2*i], stroke_points[2*(i+1)], 1)