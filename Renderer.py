import pygame
import cairo
import math

class Renderer:
    def __init__(self, buffer, width, height) -> None:
        self.shared_buffer = buffer
        self.width, self.height = width, height

    def render_stroke(self, stroke_points, pen):
        # print(f'stroke contains {len(stroke_points)} points')
        cairo_surface = cairo.ImageSurface.create_for_data(self.shared_buffer, cairo.FORMAT_ARGB32, self.width, self.height)
        context = cairo.Context(cairo_surface)
        for i in range(math.floor(len(stroke_points)/2-1)):
            # DEBUG: stroke as line segments for reference of what the spline should roughly look like
            context.set_line_width(0.75)
            context.set_source_rgb(0.0, 1.0, 0.0)
            context.move_to(stroke_points[2*i][0], stroke_points[2*i][1])
            context.line_to(stroke_points[2*(i+1)][0], stroke_points[2*(i+1)][1])
            context.stroke()

            # DEBUG: vel vector as small line segments for reference of what the velocity is being recorded as
            context.set_line_width(1.5)
            context.set_source_rgb(1.0, 0.0, 0.0)
            context.move_to(stroke_points[2*i][0], stroke_points[2*i][1])
            vec_length = math.sqrt(stroke_points[2*(i+1)+1][0]**2+stroke_points[2*(i+1)+1][1]**2)
            print(f'vector {stroke_points[2*(i+1)+1]} has length {vec_length}')
            context.line_to(
                stroke_points[2*(i+1)][0] + stroke_points[2*(i+1)+1][0]/vec_length,
                stroke_points[2*(i+1)][1] + stroke_points[2*(i+1)+1][1]/vec_length)
            context.stroke()
            # pygame.draw.line(self.target, '#00FF00', stroke_points[2*i], stroke_points[2*(i+1)], 1)
        for i in range(math.floor(len(stroke_points)/2-2)):
            # print(f'points are {2*i}, {2*i+1}, {2*i+2}, {2*i+3}')
            p0 = (stroke_points[2*i][0], stroke_points[2*i][1])
            p1 = (stroke_points[2*i][0]+stroke_points[2*i][0]/3, stroke_points[2*i][1]+stroke_points[2*i][1]/3)
            p2 = (stroke_points[2*i+2][0]-stroke_points[2*i+3][0]/3, stroke_points[2*i+2][1]-stroke_points[2*i+3][1]/3)
            p3 = (stroke_points[2*i+4][0], stroke_points[2*i+2][1])
            context.set_source_rgb(0.0, 0.0, 0.0)
            context.set_line_width(1.5)
            context.move_to(p0[0], p0[1])
            context.curve_to(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
            context.stroke()
