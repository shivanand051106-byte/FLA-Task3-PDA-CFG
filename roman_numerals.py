# Roman Numeral Validation using DFA / RegEx DFA representation
import re

class RomanNumeralValidation:
    def validate(self, roman: str) -> bool:
        # DFA transition rule simplified to standard Roman numeral structure
        pattern = r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        if not roman or not isinstance(roman, str):
            return False
        return bool(re.match(pattern, roman))
