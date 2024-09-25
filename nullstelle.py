from manim import *

class Graph(Scene):
    def construct(self):
        
        ax = Axes(
            x_range=[-7, 7, 1],
            y_range=[-2.5, 4.5, 1]    
        )

        def curve(x):
            return np.sin(x)
        
        ax_curve = ax.plot(curve, color = RED)
        
        nullstelle1 = Dot(radius=0.1, color=DARK_BLUE)
        nullstelle2 = nullstelle1.copy()
        nullstelle3 = nullstelle1.copy()
        nullstelle4 = nullstelle1.copy()
        nullstelle5 = nullstelle1.copy()


        nullstelle1.shift(ax.coords_to_point(np.pi * 2, 0))
        nullstelle2.shift(ax.coords_to_point(np.pi, 0))
        nullstelle3.shift(ax.coords_to_point(0, 0))
        nullstelle4.shift(ax.coords_to_point(-np.pi, 0))
        nullstelle5.shift(ax.coords_to_point(-np.pi * 2, 0))

        

        self.add(ax, ax_curve, nullstelle1, nullstelle2, nullstelle3, nullstelle4, nullstelle5)