from balanced_brackets import BalancedBracketsPDA
from xml_tag_matching import XMLTagMatchingPDA
from roman_numerals import RomanNumeralValidation

def run_tests():
    print("--- Running Task 3 Tests ---")
    
    # Brackets PDA tests
    b_pda = BalancedBracketsPDA()
    bracket_tests = [
        ("([]){}", True),
        ("([)]", False),
        ("{", False),
        ("", True)
    ]
    for expr, expected in bracket_tests:
        assert b_pda.validate(expr) == expected, f"Failed brackets: {expr}"
    print("Balanced brackets tests passed!")

    # XML Tag Matching tests
    x_pda = XMLTagMatchingPDA()
    xml_tests = [
        ("<html><body></body></html>", True),
        ("<html><body></html></body>", False),
        ("<input />", True),
        ("<html><p></p></html>", True)
    ]
    for xml, expected in xml_tests:
        assert x_pda.validate(xml) == expected, f"Failed XML: {xml}"
    print("XML tag matching tests passed!")

    # Roman Numerals tests
    r_val = RomanNumeralValidation()
    roman_tests = [
        ("MCMLXIX", True),
        ("IIII", False),
        ("MMXXIV", True),
        ("XM", False)
    ]
    for r, expected in roman_tests:
        assert r_val.validate(r) == expected, f"Failed Roman: {r}"
    print("Roman numeral validation tests passed!")

if __name__ == '__main__':
    run_tests()
