from tree_sitter import Language, Parser

class Tokenizer():
    def __init__(self):
        Language.build_library('build/my-languages.so', ['tree-sitter-python'])
        PYTHON_LANGUAGE = Language('build/my-languages.so', 'python')
        self.parser = Parser()
        self.parser.set_language(PYTHON_LANGUAGE)

    def get_string_from_code(self, node, lines, code_list):
        line_start = node.start_point[0]
        line_end = node.end_point[0]
        char_start = node.start_point[1]
        char_end = node.end_point[1]
        if line_start != line_end:
            code_list.append(' '.join([lines[line_start][char_start:]] + lines[line_start+1:line_end] + [lines[line_end][:char_end]]))
        else:
            code_list.append(lines[line_start][char_start:char_end])

    def my_traverse(self, node, code, code_list):
        lines = code.split('\n')
        if node.child_count == 0:
            self.get_string_from_code(node, lines, code_list)
        elif node.type == 'string':
            self.get_string_from_code(node, lines, code_list)
        else:
            for n in node.children:
                self.my_traverse(n, code, code_list)
        
        return ' '.join(code_list)
    
    def tokenize(self, code):
        tree = self.parser.parse(bytes(code, "utf8"))
        code_list=[]
        tokenized_code = self.my_traverse(tree.root_node, code, code_list)
        # print("Output after tokenization: " + tokenized_code)
        return tokenized_code