import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        variables = self.domains.keys()
        for v in variables:
            for value in self.domains[v].copy():
                if len(value) != v.length:
                    self.domains[v].remove(value)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revision = False
        binary_constrain = self.crossword.overlaps[x, y]
        if binary_constrain:
            x_char, y_char = binary_constrain
            values_x = self.domains[x].copy()
            values_y = self.domains[y].copy()
            for value_x in values_x:
                correspondence = False
                for value_y in values_y:
                    if value_x[x_char] == value_y[y_char]:
                        correspondence = True
                        break
                if not correspondence:
                    self.domains[x].remove(value_x)
                    revision = True
        return revision


    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        variables = list(self.domains.keys())
        if not arcs:
            arcs = []
            for i in range(len(variables)):
                for j in range(i+1, len(variables)):
                    constrain = self.crossword.overlaps[variables[i], variables[j]]
                    if constrain:
                        arcs.append((variables[i], variables[j]))
        while len(arcs) != 0:
            arc = arcs[-1]
            arcs = arcs[:-1]
            v1, v2 = arc
            if self.revise(v1, v2):
                if len(self.domains[v1]) == 0:
                    return False
                for i in range(len(variables)):
                    if variables[i] != v2 and variables[i] != v1:
                        constrain = self.crossword.overlaps[v1, variables[i]]
                        if constrain:
                            arcs.append((v1, variables[i]))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for variable in list(self.domains.keys()):
            if variable not in assignment:
                return False
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        variables = list(assignment.keys())
        for v1 in range(len(variables)):
            if len(assignment[variables[v1]]) != variables[v1].length:
                return False
            for v2 in range(v1 + 1,len(variables)):
                if assignment[variables[v1]] == assignment[variables[v2]]:
                    return False
                constrain = self.crossword.overlaps[variables[v1], variables[v2]]
                if constrain:
                    char_v1, char_v2 = constrain
                    if assignment[variables[v1]][char_v1] != assignment[variables[v2]][char_v2]:
                        return False
        return True

    def number_of_mismatches(self, value, var, assignment):
        variables = list(self.domains.keys())
        variables.remove(var)
        num = 0
        for variable in variables:
            if variable not in assignment:
                constrain = self.crossword.overlaps[var, variable]
                if constrain:
                    value_char, y_char = constrain
                    for comb in self.domains[variable]:
                        if value[value_char] != comb[y_char]:
                            num += 1
        return num

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        values = list(self.domains[var])
        values.sort(key = lambda value: self.number_of_mismatches(value, var, assignment))
        return values

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        not_assigned = []
        for variable in list(self.domains.keys()):
            if variable not in assignment:
                not_assigned.append(variable)
        not_assigned.sort(key= lambda var: (len(self.domains[var]), -len(self.crossword.neighbors(var))))

        return not_assigned[0]


    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value
            if self.consistent(assignment):
                recursao = self.backtrack(assignment)
                if recursao:
                    return recursao
            del assignment[var]
        return None

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
