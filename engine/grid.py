import pyglet


class Grid:

    LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, rows, cols, window):
        if cols > 24:
            raise ValueError("Too many columns")
        self.rows = rows
        self.cols = cols
        self.cell_length = int(window.width / self.cols)

        self.window = window

        self.size = self.cell_length
        self.offset = self.cell_length / 2

    def convert_int_to_letter(self, number):
        if number > 24:
            raise ValueError("Number outside alphabet range")
        return self.LETTERS[number]

    def convert_letter_to_int(self, letter):
        return self.LETTERS.index(letter)

    def calculate_xy_values(self, coord_x, coord_y):
        """
        coord_string is of format "{character}{number}"
        For example, c4, indicating
            x = 2
            y = 4
        Returns x, y position in pixels
        """
        pix_x = coord_x * self.size + self.offset
        pix_y = coord_y * self.size + self.offset
        return pix_x, pix_y

    def calculate_grid_position(self, pix_x, pix_y):
        coord_x = self.translate_pixel_to_cell(pix_x)
        coord_y = self.translate_pixel_to_cell(pix_y)
        return coord_x, coord_y

    def calculate_grid_position_name(self, pix_x, pix_y):
        coord_x, coord_y = self.calculate_grid_position(pix_x, pix_y)
        return self.get_grid_position_name(coord_x, coord_y)

    def get_grid_position_name(self, coord_x, coord_y):
        char_x = self.convert_int_to_letter(coord_x)
        return char_x + str(coord_y)

    def calculate_grid_position_from_name(self, name):
        # name is of format {letter}{number} eg d4
        if len(name) != 2:
            raise ValueError('Invalid position name format')
        coord_x = self.convert_letter_to_int(name[0])
        coord_y = int(name[1])
        return coord_x, coord_y

    def calculate_xy_from_name(self, name):
        coord_x, coord_y = self.calculate_grid_position_from_name(name)
        return self.calculate_xy_values(coord_x, coord_y)

    def calculate_xy_from_percentage(self, percentages):
        p_x, p_y = percentages
        coord_x = self.window.width * p_x
        coord_y = self.window.height * p_y
        return coord_x, coord_y

    def translate_pixel_to_cell(self, pixel_measure):
        cell = pixel_measure // self.cell_length
        return int(cell)

    def get_x_lines(self):
        x_lines = list()
        for i in range(1, self.cols):
            x_lines.append(self.size * i + self.offset)
        return x_lines

    def get_y_lines(self):
        y_lines = list()
        for i in range(1, self.rows):
            y_lines.append(self.size * i + self.offset)
        return y_lines
