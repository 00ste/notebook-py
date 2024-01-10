import pygame
import cairo
import math

class Renderer:
    def __init__(self, buffer, width, height) -> None:
        self.shared_buffer = buffer
        self.width, self.height = width, height

    def set_brush(context: cairo.Context, rgb_color, line_width):
        context.set_source_rgb(rgb_color[0], rgb_color[1], rgb_color[2])
        context.set_line_width(line_width)
    
    def draw_line(context: cairo.Context, start_point, end_point):
        context.move_to(start_point[0], start_point[1])
        context.line_to(end_point[0], end_point[1])
        context.stroke()
    
    def draw_spline(context: cairo.Context, start_point, end_point, start_velo, end_velo):
        control_point_1 = start_point
        control_point_2 = [
            start_point[0] + start_velo[0]/3,
            start_point[1] + start_velo[1]/3,
        ]
        control_point_3 = [
            end_point[0] - end_velo[0]/3,
            end_point[1] - end_velo[1]/3,
        ]
        control_point_4 = end_point

        context.move_to(control_point_1[0], control_point_1[1])
        context.curve_to(control_point_2[0], control_point_2[1], control_point_3[0],
                         control_point_3[1], control_point_4[0], control_point_4[1])
        context.stroke()
    
    def draw_vector(context: cairo.Context, start_point, vector, length):
        norm = math.sqrt(vector[0]**2+vector[1]**2)
        if norm > 0:
            context.move_to(start_point[0], start_point[1])
            context.rel_line_to(length*vector[0]/norm, length*vector[1]/norm)
            context.stroke()

    def render_stroke(self, stroke_points, pen):
        # print(f'stroke contains {len(stroke_points)} points')
        cairo_surface = cairo.ImageSurface.create_for_data(self.shared_buffer, cairo.FORMAT_ARGB32, self.width, self.height)
        context = cairo.Context(cairo_surface)

        n_points = math.floor(len(stroke_points) / 2)
        positions = [stroke_points[2*k] for k in range(n_points)]
        velocities = [stroke_points[2*k+1] for k in range(n_points)]
        print(f'positions: {positions}\nvelocities: {velocities}')

        '''
        # DEBUG: draw line segments
        Renderer.set_brush(context, (0.0, 1.0, 0.0), 1.00)
        for k in range(n_points-1):
            Renderer.draw_line(context, positions[k], positions[k+1])
        
        # DEBUG: draw vectors
        Renderer.set_brush(context, (1.0, 0.0, 0.0), 2.00)
        for k in range(n_points):
            Renderer.draw_vector(context, positions[k], velocities[k], 20)
        '''
        
        # draw smooth splines
        Renderer.set_brush(context, (0.0, 0.0, 0.0), 1.00)
        for k in range(n_points-1):
            Renderer.draw_spline(context,
                positions[k],
                positions[k+1],
                velocities[k],
                velocities[k+1]
            )