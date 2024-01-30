import pygame
import cairo
import math
import array

import time

class Renderer:
    def __init__(self, width, height, padding) -> None:
        self.width, self.height = width, height
        self.padding = padding
        self.data_buffer = array.array('B', [0] * self.width * self.height * 4)
        self.screen_surface = cairo.ImageSurface.create_for_data(self.data_buffer,
            cairo.FORMAT_ARGB32, self.width, self.height)

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

    def render_stroke(self, context, stroke_points, pen):
        n_points = math.floor(len(stroke_points) / 2)
        positions = [stroke_points[2*k] for k in range(n_points)]
        velocities = [stroke_points[2*k+1] for k in range(n_points)]

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
    
    def render_page(self, strokes, page_dimensions, pan_x, pan_y, scale):
        '''
        # create screen surface
        screen_surface = pygame.Surface((self.width, self.height))
        screen_surface.fill((192, 192, 192)) # TODO: REPLACE WITH CLIENT BACKGROUND COLOUR VARIABLE DEFINED SOMEWHERE
        
        # create page buffer
        page_width_onscreen = min(page_dimensions[0], self.width-pan_x)
        page_height_onscreen = min(page_dimensions[1], self.height-pan_y)
        page_buffer = array.array('B', [0] * page_width_onscreen * page_height_onscreen * 4)
        
        # create page surface (cairo)
        page_surface = cairo.ImageSurface.create_for_data(page_buffer, cairo.FORMAT_ARGB32,
            page_width_onscreen, page_height_onscreen)
        page_context = cairo.Context(page_surface)
        '''
        # reset screen surface
        screen_context = cairo.Context(self.screen_surface)
        screen_context.set_source_rgb(0.8, 0.8, 0.8)
        screen_context.rectangle(0, 0, self.width, self.height)
        screen_context.fill()
        
        # create page surface
        page_width_onscreen = page_dimensions[0]
        page_height_onscreen = page_dimensions[1]

        page_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,
            page_width_onscreen, page_height_onscreen)
        page_context = cairo.Context(page_surface)

        # draw page background
        screen_context.set_source_rgb(1.0, 1.0, 1.0) # TODO: REPLACE WITH PAGE COLOUR VARIABLE FROM THE FILE
        screen_context.rectangle(0, 0, page_width_onscreen, page_height_onscreen)
        screen_context.fill()

        # stroke rendering
        for stroke in strokes:
            pen = stroke['pen']
            # transform all points with scaling, panning will happen later
            points = [(scale*point[0], scale*point[1]) for point in stroke['points']]
            for point in points:
                if 0 < point[0] < self.width and 0 < point[1] < self.height:
                    self.render_stroke(page_context, points, pen)
                    break
        screen_context.set_source_surface(page_surface, pan_x, pan_y)
        screen_context.paint()
        return pygame.image.fromstring(self.data_buffer.tobytes(),
            (self.width, self.height), 'BGRA')
        '''
        # blit page surface (converted for pygame) on screen surface, panning happens here
        screen_surface.blit(pygame.image.fromstring(page_buffer.tobytes(),
            (page_width_onscreen, page_height_onscreen), 'BGRA'), (max(0, pan_x), max(0, pan_y)))    
        return screen_surface
        '''

        
            