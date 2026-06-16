# File: rps_test.py

import unittest
import ast
import rps
import tud_test_base as tud


class TestRPS(unittest.TestCase):

    #################################################
    # Helpers
    #################################################

    def run_program(self, inputs):

        tud.set_keyboard_input(inputs)

        rps.main()

        return tud.get_display_output()

    #################################################
    # Required Functions
    #################################################

    def test_required_functions_exist(self):

        required = [
            "main",
            "get_input",
            "play_rounds",
            "get_computer_choice",
            "get_result",
            "print_results"
        ]

        for function_name in required:

            self.assertTrue(
                hasattr(rps, function_name),
                f"Missing function {function_name}"
            )

    #################################################
    # Assignment Examples
    #################################################

    def test_example_1(self):

        output = self.run_program([
            "Olivia",
            "1",
            "y",
            "9876",
            "P"
        ])

        joined = "\n".join(output)

        self.assertIn(
            "I pick Paper.",
            joined
        )

        self.assertIn(
            "Olivia won 0 rounds.",
            joined
        )

    def test_example_2(self):

        output = self.run_program([
            "Isabelle",
            "1",
            "y",
            "9876",
            "S"
        ])

        joined = "\n".join(output)

        self.assertIn(
            "I pick Paper.",
            joined
        )

        self.assertIn(
            "Isabelle won 1 round.",
            joined
        )

    def test_example_4(self):

        output = self.run_program([
            "D",
            "7",
            "y",
            "1234",
            "P",
            "S",
            "P",
            "P",
            "R",
            "S",
            "R"
        ])

        joined = "\n".join(output)

        self.assertIn(
            "D won 4 rounds.",
            joined
        )

    def test_example_5(self):

        output = self.run_program([
            "Noah",
            "8",
            "y",
            "77777",
            "S",
            "R",
            "S",
            "R",
            "P",
            "P",
            "S",
            "R"
        ])

        joined = "\n".join(output)

        self.assertIn(
            "Noah won 1 round.",
            joined
        )

    def test_example_7(self):

        output = self.run_program([
            "Tyler",
            "3",
            "y",
            "3",
            "P",
            "P",
            "S"
        ])

        joined = "\n".join(output)

        self.assertIn(
            "Tyler won 1 round.",
            joined
        )

    #################################################
    # Output Requirements
    #################################################

    def test_welcome_message(self):

        output = self.run_program([
            "A",
            "1",
            "y",
            "1",
            "R"
        ])

        self.assertEqual(
            output[0],
            "Welcome to ROCK PAPER SCISSORS. I, Computer, will be your opponent."
        )

    def test_initial_input_marker(self):

        output = self.run_program([
            "A",
            "1",
            "y",
            "1",
            "R"
        ])

        joined = "\n".join(output)

        self.assertIn(
            "--- INITIAL INPUT ---",
            joined
        )

    def test_round_marker(self):

        output = self.run_program([
            "A",
            "1",
            "y",
            "1",
            "R"
        ])

        joined = "\n".join(output)

        self.assertIn(
            "--- Round 1 ---",
            joined
        )

    #################################################
    # Singular / Plural
    #################################################

    def test_one_round(self):

        output = self.run_program([
            "Bob",
            "1",
            "y",
            "1",
            "R"
        ])

        joined = "\n".join(output)

        self.assertIn(
            "We played 1 round of ROCK PAPER SCISSORS.",
            joined
        )

    #################################################
    # No Globals
    #################################################

    def test_no_globals(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        globals_found = []

        for node in tree.body:

            if isinstance(node, ast.Assign):
                globals_found.append(node)

        self.assertEqual(
            len(globals_found),
            0,
            "Global variables are not allowed."
        )

    #################################################
    # No Lists
    #################################################

    def test_no_lists(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):

            self.assertFalse(
                isinstance(node, ast.List),
                "Lists are not allowed."
            )

    #################################################
    # No Dictionaries
    #################################################

    def test_no_dictionaries(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):

            self.assertFalse(
                isinstance(node, ast.Dict),
                "Dictionaries are not allowed."
            )

    #################################################
    # Random Required
    #################################################

    def test_random_import(self):

        with open("rps.py") as f:
            code = f.read()

        self.assertIn(
            "import random",
            code,
            "Assignment requires random module."
        )

    #################################################
    # Documentation
    #################################################

    def test_header_exists(self):

        with open("rps.py") as f:
            code = f.read()

        required_items = [
            "# File:",
            "# Description:",
            "# Assignment Number:",
            "# Name:",
            "# Email:",
            "# Grader:"
        ]

        for item in required_items:

            self.assertIn(
                item,
                code
            )

    def test_docstrings(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        documented_functions = 0

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                if ast.get_docstring(node):
                    documented_functions += 1

        self.assertGreaterEqual(
            documented_functions,
            5,
            "Expected function documentation."
        )

    #################################################
    # Readability
    #################################################

    def test_variable_names(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        short_names = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Assign):

                for target in node.targets:

                    if isinstance(target, ast.Name):

                        name = target.id

                        if len(name) == 1:
                            short_names.append(name)

        self.assertLessEqual(
            len(short_names),
            2,
            f"Too many single-letter variables: {short_names}"
        )

    #################################################
    # Function Length
    #################################################

    def test_function_lengths(self):

        with open("rps.py") as f:
            lines = f.readlines()

        tree = ast.parse("".join(lines))

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                executable_lines = 0

                for line in lines[
                    node.lineno - 1:
                    node.end_lineno
                ]:

                    stripped = line.strip()

                    if stripped == "":
                        continue

                    if stripped.startswith("#"):
                        continue

                    if (
                        stripped.startswith('"""')
                        or stripped.startswith("'''")
                    ):
                        continue

                    executable_lines += 1

                self.assertLessEqual(
                    executable_lines,
                    25,
                    f"{node.name} exceeds assignment limit."
                )

    #################################################
    # Structure
    #################################################

    def test_program_runs(self):

        output = self.run_program([
            "A",
            "1",
            "y",
            "1",
            "R"
        ])

        self.assertGreater(
            len(output),
            0
        )


if __name__ == "__main__":
    unittest.main()