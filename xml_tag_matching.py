# Pushdown Automaton for XML Tag Matching
import re

class XMLTagMatchingPDA:
    def validate(self, xml_str: str) -> bool:
        # Simple regex tokenizer for XML tags
        tokens = re.findall(r'<[^>]+>', xml_str)
        stack = []
        
        for token in tokens:
            if token.startswith('</'):
                # Closing tag
                tag_name = token[2:-1]
                if not stack or stack[-1] != tag_name:
                    return False
                stack.pop()
            elif token.startswith('<') and token.endswith('/>'):
                # Self-closing tag
                continue
            else:
                # Opening tag
                tag_name = token[1:-1]
                stack.append(tag_name)
                
        return len(stack) == 0
