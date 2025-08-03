class KinematicEquations(Scene):

    # Configuration for all text elements
    
    CONFIG = {
        # Velocity-Time Graph
        "graph_title": "Velocity-Time Graph",
        "x_axis_label": "t",
        "y_axis_label": "V",

        # Labels Elements
        "final_velocity_label": "V_f",
        "initial_velocity_label": "V_i",

        # Visualized Equation
        "linear_equation_parts": ["V_f", "=", "m", "x", "+", "b"],

        "displacement_sum_parts": [
            r"\Delta{x}", "=", r"\triangle", "+", "R"
        ],

        "displacement_area_parts": [
            r"\Delta{x}", "=", "T"
        ],

        # Area of Visualized Equation
        "area_of_triangle_expression": r"\frac{1}{2}BH",
        "area_of_rectangle_expression": "BH",
        "area_of_trapezoid_expression": r"\frac{1}{2}(B_1 + B_2)H",
        
        # Concluded Equation
        "final_velocity_parts": ["V_f", "=", "V_i", "+", "a", "t"],

        "delta_x_with_acceleration_parts": [
            r"\Delta{x}", "=", "V_i", "t", "+", r"\frac{1}{2}", "a", "t^2"
        ],

        "delta_x_with_no_acceleration_parts": [
            r"\Delta{x}", "=", r"\frac{1}{2}", "(V_i+V_f)", "t"
        ],

        # Slope of Velocity (Linear)
        "slope_expression": r"\frac{\Delta{v}}{\Delta{t}}",

        # Symbols
        "acceleration_symbol": "a",
        "time_symbol": "t",
        "y_intercept_symbol": "V_i",

        # Fonts
        "font_size_small": 28,
        "font_size_medium": 36
    }
    
    # Visualization Materials

    def show_velocity_time_graph(self):
        graph = Axes(
            x_range=[0, 15],
            y_range=[0, 15],
        )
        plt = graph.plot(lambda x: x + 3, x_range=[0, 9], use_smoothing=False)

        title = Tex(self.CONFIG["graph_title"])
        title.next_to(graph, UP)

        x_label = graph.get_x_axis_label(self.CONFIG["x_axis_label"])
        y_label = graph.get_y_axis_label(self.CONFIG["y_axis_label"])

        self.play(Create(graph))
        self.play(Write(title))
        self.play(Write(x_label))
        self.play(Write(y_label))
        self.play(Create(plt))

        return graph, title, x_label, y_label

    def show_points(self, graph):
        final_velocity_point = Dot(graph.c2p(9, 12), color=YELLOW)
        final_velocity_point_1 = Dot(graph.c2p(0, 12), color=YELLOW)

        final_velocity_label = MathTex(
            self.CONFIG["final_velocity_label"], 
            font_size=self.CONFIG["font_size_small"]
        )
        final_velocity_label.next_to(final_velocity_point, UP)

        final_velocity_point_1_label = MathTex(
            self.CONFIG["final_velocity_label"], 
            font_size=self.CONFIG["font_size_small"]
        )
        final_velocity_point_1_label.next_to(final_velocity_point_1, UP + LEFT)

        final_velocity_line_x = graph.get_horizontal_line(graph.c2p(9, 12), color=RED)
        final_velocity_line_y = graph.get_vertical_line(graph.c2p(9, 12), color=RED)

        initial_velocity_point = Dot(graph.c2p(0, 3), color=YELLOW)
        initial_velocity_point_1 = Dot(graph.c2p(9, 3), color=YELLOW)

        initial_velocity_label = MathTex(
            self.CONFIG["initial_velocity_label"], 
            font_size=self.CONFIG["font_size_small"]
        )
        initial_velocity_label.next_to(initial_velocity_point, UP + LEFT)

        initial_velocity_point_1_label = MathTex(
            self.CONFIG["initial_velocity_label"], 
            font_size=self.CONFIG["font_size_small"]
        )
        initial_velocity_point_1_label.next_to(initial_velocity_point_1, UP + LEFT)

        initial_velocity_line_x = graph.get_horizontal_line(graph.c2p(9, 3), color=BLUE)

        self.play(Create(final_velocity_point))
        self.play(Create(initial_velocity_point))

        self.play(Write(final_velocity_label))
        self.play(Write(initial_velocity_label))

        self.play(Create(final_velocity_line_x))
        self.play(Create(final_velocity_line_y))

        self.play(Create(final_velocity_point_1))
        self.play(Create(initial_velocity_point_1))

        self.play(Create(initial_velocity_line_x))

        self.play(Write(initial_velocity_point_1_label))
        self.play(Write(final_velocity_point_1_label))

        return VGroup(
            final_velocity_point, final_velocity_label,
            initial_velocity_point, initial_velocity_label,
            final_velocity_point_1, final_velocity_point_1_label,
            initial_velocity_point_1, initial_velocity_point_1_label
        )

    def show_final_velocity_line(self, graph):
        plt_final_velocity = graph.plot(
            lambda x: x + 3, 
            x_range=[0, 9], 
            use_smoothing=False, 
            color=RED
        )
        self.play(Create(plt_final_velocity))
        self.wait(1)
        return plt_final_velocity

    def show_final_velocity_area(self, graph):
        final_velocity_area = Polygon(
            graph.c2p(0, 3),
            graph.c2p(9, 3),
            graph.c2p(9, 12),
            color=GREEN,
            fill_opacity=0.5
        )

        self.play(Create(final_velocity_area))
        self.wait(1)
        return final_velocity_area

    def show_initial_velocity_area(self, graph):
        initial_velocity_area = Rectangle(
            width=graph.c2p(9, 0)[0] - graph.c2p(0, 0)[0],
            height=graph.c2p(0, 3)[1] - graph.c2p(0, 0)[1],
            color=ORANGE,
            fill_opacity=0.5
        ).move_to(graph.c2p(0, 0), aligned_edge=DL)
        self.play(Create(initial_velocity_area))
        self.wait(1)
        return initial_velocity_area
    
    # Initialize an equation

    def create_equation(self, parts, position, font_size=None):
        if font_size is None:
            font_size = self.CONFIG["font_size_medium"]
        equation = VGroup(*[
            MathTex(part, font_size=font_size) for part in parts
        ]).arrange(RIGHT, buff=0.1)
        equation.move_to(position)
        return equation

    # Create an equation based on visual materials

    def show_final_velocity_linear_equation(self, plt_final_velocity):
        equation = self.create_equation(
            self.CONFIG["linear_equation_parts"],
            position=RIGHT * 4 + UP * 2
        )
        self.wait(1)
        self.play(ReplacementTransform(plt_final_velocity, equation))
        return equation

    def show_displacement_sum_equation(self, final_velocity_area, initial_velocity_area):
        equation = self.create_equation(
            self.CONFIG["displacement_sum_parts"],
            position=RIGHT * 4 + UP * 1
        )
        self.play(ReplacementTransform(
            VGroup(final_velocity_area, initial_velocity_area), 
            equation
        ))
        self.wait(1)
        return equation

    def show_displacement_area(self, graph):
        displacement_area = Polygon(
            graph.c2p(0, 0),
            graph.c2p(9, 0),
            graph.c2p(9, 12),
            graph.c2p(0, 3),
            color=BLUE,
            fill_opacity=0.5
        )
        self.wait(1)
        self.play(Create(displacement_area))
        return displacement_area

    def show_displacement_area_equation(self, displacement_area):
        equation = self.create_equation(
            self.CONFIG["displacement_area_parts"],
            position=RIGHT * 4
        )
        self.play(ReplacementTransform(displacement_area, equation))
        self.wait(1)
        return equation

    def show_final_velocity_linear_equation_slope(self, equation):
        slope = MathTex(
            self.CONFIG["slope_expression"],
            font_size=self.CONFIG["font_size_medium"]
        ).move_to(LEFT * 2 + UP)
        
        acceleration = MathTex(
            self.CONFIG["acceleration_symbol"],
            font_size=self.CONFIG["font_size_medium"]
        ).move_to(LEFT * 2 + UP)
        
        self.play(ReplacementTransform(equation[2].copy(), slope))
        self.wait(0.8)
        self.play(ReplacementTransform(slope, acceleration))
        self.wait(1)
        equation.submobjects[2] = acceleration
        return equation

    # Conclude the `final_velocity`

    def show_final_velocity_linear_equation_x(self, equation):
        time = MathTex(
            self.CONFIG["time_symbol"],
            font_size=self.CONFIG["font_size_medium"]
        ).move_to(LEFT * 2 + DOWN * 2.5)
        
        self.play(ReplacementTransform(equation[3].copy(), time))
        self.wait(1)
        equation.submobjects[3] = time
        return equation

    def show_final_velocity_linear_equation_y_intercept(self, graph, equation):
        y_intercept = MathTex(
            self.CONFIG["y_intercept_symbol"],
            font_size=self.CONFIG["font_size_medium"]
        ).move_to(LEFT * 5 + DOWN * 2.5)
        
        initial_velocity_point = Dot(graph.c2p(0, 3), color=BLUE)
        self.play(Create(initial_velocity_point))
        self.play(ReplacementTransform(initial_velocity_point, y_intercept))
        self.wait(1)
        equation.submobjects[5] = y_intercept
        return equation

    # Conclude the `displacement_with_acceleration`

    def show_area_of_triangle(self, equation):
        area_of_triangle = MathTex(
            self.CONFIG["area_of_triangle_expression"],
            font_size=self.CONFIG["font_size_small"],
        ).shift(DOWN * 0.5 + LEFT * 0.5)
        self.play(ReplacementTransform(equation[2].copy(), area_of_triangle))
        self.wait(1)
        equation.submobjects[2] = area_of_triangle
        return equation
    
    def show_area_of_rectangle(self, equation):
        area_of_rectangle = MathTex(
            self.CONFIG["area_of_rectangle_expression"],
            font_size=self.CONFIG["font_size_small"]
        ).shift(DOWN * 2.5 + LEFT * 1.5)
        self.play(ReplacementTransform(equation[4].copy(), area_of_rectangle))
        self.wait(1)
        equation.submobjects[4] = area_of_rectangle
        return equation

    # Conclude the `displacement_with_no_acceleration`
    def show_area_of_trapezoid(self, equation):
        area_of_trapezoid = MathTex(
            self.CONFIG["area_of_trapezoid_expression"],
            font_size=self.CONFIG["font_size_small"]
        ).shift(DOWN + LEFT * 2)

        self.play(ReplacementTransform(equation[2].copy(), area_of_trapezoid))
        self.wait(1)
        equation.submobjects[2] = area_of_trapezoid
        return equation

    def construct(self):
        final_velocity_equation = self.create_equation(
            self.CONFIG["final_velocity_parts"],
            position=RIGHT * 4 + UP * 2,
            font_size=self.CONFIG["font_size_medium"]
        )
        
        delta_x_with_acceleration = self.create_equation(
            self.CONFIG["delta_x_with_acceleration_parts"],
            position=RIGHT * 4 + UP * 1,
            font_size=self.CONFIG["font_size_medium"]
        )
        
        delta_x_with_no_acceleration = self.create_equation(
            self.CONFIG["delta_x_with_no_acceleration_parts"],
            position=RIGHT * 4,
            font_size=self.CONFIG["font_size_medium"]
        )

        graph, title, x_label, y_label = self.show_velocity_time_graph()
        points_group = self.show_points(graph)

        plt_final_velocity = self.show_final_velocity_line(graph)
        linear_equation = self.show_final_velocity_linear_equation(plt_final_velocity)

        final_velocity_area = self.show_final_velocity_area(graph)
        initial_velocity_area = self.show_initial_velocity_area(graph)
        displacement_sum_equation = self.show_displacement_sum_equation(
            final_velocity_area, 
            initial_velocity_area
        )

        displacement_area = self.show_displacement_area(graph)
        displacement_area_equation = self.show_displacement_area_equation(displacement_area)

        highlight_velocity_line = self.show_final_velocity_line(graph)
        
        linear_equation = self.show_final_velocity_linear_equation_slope(linear_equation)
        linear_equation = self.show_final_velocity_linear_equation_x(linear_equation)
        linear_equation = self.show_final_velocity_linear_equation_y_intercept(graph, linear_equation)

        self.play(ReplacementTransform(linear_equation, final_velocity_equation))
        self.play(Uncreate(highlight_velocity_line))

        highlight_final_velocity_area = self.show_final_velocity_area(graph)

        displacement_sum_equation = self.show_area_of_triangle(displacement_sum_equation)

        highlight_initial_velocity_area = self.show_initial_velocity_area(graph)
        displacement_sum_equation = self.show_area_of_rectangle(displacement_sum_equation)

        self.play(ReplacementTransform(displacement_sum_equation, delta_x_with_acceleration))
        self.play(Uncreate(highlight_initial_velocity_area))
        self.play(Uncreate(highlight_final_velocity_area))

        highlight_displacement_area = self.show_displacement_area(graph)
        displacement_area_equation = self.show_area_of_trapezoid(displacement_area_equation)
        self.play(ReplacementTransform(displacement_area_equation, delta_x_with_no_acceleration))
        self.play(Uncreate(highlight_displacement_area))
        self.wait(2)
        self.clear()
        github_link = Tex("https://github.com/chr-00/manim-kinematic-equations", font_size=30)
        self.play(Write(github_link))
        self.wait(5)
