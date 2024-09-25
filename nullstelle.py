from manim import *

class Graph(Scene):
    def construct(self):
        
        ax = Axes(
            x_range=[-7, 7, 1],
            y_range=[-2.5, 4.5, 1]    
        )

        def curve(x):
            return np.sin(x)
        
