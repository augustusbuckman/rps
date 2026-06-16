# File: rps_test.py

import unittest
import ast
import rps
import tud_test_base as tud


class TestRPS(unittest.TestCase):

    #################################################
    # Helper Methods
    #################################################

    def run_program(self, inputs):

        tud.set_keyboard_input(inputs)

        rps.main()

        return tud.get_display_output()

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
            "Olivia won 0 rounds.",
            joined
        )

        self.assertIn(
            "We played 1 round of ROCK PAPER SCISSORS.",
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
            "Isabelle won 1 round.",
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
    # Required Output Sections
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
            "1 round of ROCK PAPER SCISSORS.",
            joined
        )

    #################################################
    # Starter Functions Required
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
    # Function Count
    #################################################

    def test_multiple_functions_used(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        function_count = 0

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):
                function_count += 1

        self.assertGreaterEqual(
            function_count,
            6,
            "Expected multiple programmer-defined functions."
        )

    #################################################
    # No Global Variables
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
    # No Lists or Dictionaries
    #################################################

    def test_no_lists(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):

            self.assertFalse(
                isinstance(node, ast.List),
                "Lists are not allowed."
            )

    def test_no_dictionaries(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        for node in ast.walk(tree):

            self.assertFalse(
                isinstance(node, ast.Dict),
                "Dictionaries are not allowed."
            )

    #################################################
    # Random Module
    #################################################

    def test_random_import_present(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        found = False

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for imported in node.names:

                    if imported.name == "random":
                        found = True

        self.assertTrue(
            found,
            "Assignment requires random module."
        )

    #################################################
    # Readability
    #################################################

    def test_meaningful_variable_names(self):

        with open("rps.py") as f:
            tree = ast.parse(f.read())

        descriptive_names = 0
        bad_names = []

        allowed_short = {
            "i",
            "j"
        }

        for node in ast.walk(tree):

            if isinstance(node, ast.Assign):

                for target in node.targets:

                    if isinstance(
                        target,
                        ast.Name
                    ):

                        name = target.id

                        if (
                            len(name) <= 2
                            and name not in allowed_short
                        ):
                            bad_names.append(name)

                        if len(name) >= 5:
                            descriptive_names += 1

        self.assertLessEqual(
            len(bad_names),
            2,
            f"Use more meaningful names instead of {bad_names}"
        )

        self.assertGreaterEqual(
            descriptive_names,
            5,
            "Expected several descriptive variable names."
        )

    #################################################
    # Header and Comments
    #################################################

    def test_header_exists(self):

        with open("rps.py") as f:
            code = f.read()

        required = [

            "# File:",
            "# Description:",
            "# Assignment Number:",
            "# Name:",
            "# Email:",
            "# Grader:"
        ]

        for item in required:

            self.assertIn(
                item,
                code,
                f"Missing header item {item}"
            )

    def test_meaningful_comments(self):

        with open("rps.py") as f:
            lines = f.readlines()

        meaningful_comments = 0

        for line in lines[15:]:

            stripped = line.strip()

            if (
                stripped.startswith("#")
                and len(stripped) >= 20
            ):
                meaningful_comments += 1

        self.assertGreaterEqual(
            meaningful_comments,
            3,
            "Expected at least three meaningful comments."
        )

    #################################################
    # Function Length Requirement
    #################################################

    def test_function_length(self):

        with open("rps.py") as f:
            lines = f.readlines()

        tree = ast.parse("".join(lines))

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                start = node.lineno
                end = node.end_lineno

                function_length = (
                    end - start + 1
                )

                self.assertLessEqual(
                    function_length,
                    35,
                    f"{node.name} appears too long."
                )

    #################################################
    # Structure
    #################################################

    def test_main_exists(self):

        self.assertTrue(
            hasattr(rps, "main")
        )


if __name__ == "__main__":
    unittest.main()
