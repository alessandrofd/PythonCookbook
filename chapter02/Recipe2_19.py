__author__ = 'Alessandro'

# In this problem, we're focused on the problem of parsing text according to a particular grammar. In order to do this,
# you should probably start by having a formal specification of the grammar in the form of a BNF or EBNF. For example,
# a grammar fo simple arithmetic expressions might look like this:

#   expr ::= expr + term
#       |    expr - term
#       |    term

#   term ::= term * factor
#       |    term / factor
#       |    factor

#   factor ::= ( expr )
#          |   NUM

# Or, alternatively, in EBNF form:

#   expr ::= term { (+|-) term}*
#   term ::= factor { (*|/) factor}*
#   factor ::= ( expr )
#          |   NUM

# In an EBNF, parts of a rule enclosed in { ... }* are optional. The * means zero or more repetitions (the same meaning
# as in a regular expression).

# Now, if you're not familiar with the mechanics of working with a BNF, think of it as a specification of substitution
# or replacement rules where symbols on the left side can be replaced by the symbols os the right (or vice versa). Gene-
# rally, what happens during parsing is that you try to match the input text to the grammar by making various substi-
# tutions and expansions using the BNF. To illustrate, suppose you are parsing an expression such as 3 + 4 * 5. This
# expression would first need to be broken down into a token stream, using the techniques described in Recipe 2.18. The
# result might be a sequence like this:

#   NUM + NUM * NUM

# From there, parsing involves trying to match the grammar to input tokens by making substitutions:

# expr
# expr ::= term { (+|-) term }*
# expr ::= factor { (*|/) factor }* { (+|-) term }*
# expr ::= NUM { (*|/) factor }* { (+|-) term }*
# expr ::= NUM { (+|-) term }*
# expr ::= NUM + term { (+|-) term }*
# expr ::= NUM + factor { (*|/) factor }* { (+|-) term }*
# expr ::= NUM + NUM { (*|/) factor}* { (+|-) term }*
# expr ::= NUM + NUM * factor { (*|/) factor }* { (+|-) term }*
# expr ::= NUM + NUM * NUM { (*|/) factor }* { (+|-) term }*
# expr ::= NUM + NUM * NUM { (+|-) term }*
# expr ::= NUM + NUM * NUM

# Following all of the substitutions steps takes a bit of coffee, but they're driven by looking at the input and trying
# to match it to grammar rules. The first input token is a NUM, so substitutions first focus on matching that part. Once
# matched, attention moves to the next token of + and so on. Certain parts of the righthand side (e.g., { (*/) factor }*)
# disappear when it's determined that they can't match the next token. In a successful parse, the entire righthand side
# is expanded completely to match the input token stream.

# With all the preceding background in place, here is a simple recipe that shows how to build a recursive descent
# expression evaluator:

import re
import collections

# Token specifications
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))

# Tokenizer
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

# Parser
class ExpressionEvaluator:
    '''
    Implementation of a recursive descent parser.  Each method
    implements a single grammar rule.  Use the ._accept() method
    to test and accept the current lookahead token.  Use the ._expect()
    method to exactly match and discard the next token on the input
    (or raise a SyantaxError if it doesn't match).
    '''

    def parse(self, text):
        self.tokens = generate_tokens(text)
        self.tok = None         # Last symbol consumed
        self.nexttok = None     # Nest symbol tokenized
        self._advance()         # Load first lookahead token
        return self.expr()

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self, toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)

    # Grammar rules follow

    def expr(self):
        "expression ::= term { ('+'|'-') term }*"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }*"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | ( expr )"

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')

# Here is an example of using the Expression Evaluator class interactively:

print('\n### ExpressionEvaluator ###\n')
e = ExpressionEvaluator()
print(e.parse('2'))
print(e.parse('2 + 3'))
print(e.parse('2 + 3 * 4'))
print(e.parse('2 + (3 + 4) * 5'))
#print(e.parse('2 + (3 +* 4)'))  # SyntaxError: Expected NUMBER or LPAREN


# If you want to do something other than pure evaluation, you need to change the ExpressionEvaluator class to do some-
# thing else. For example, here is an alternative implementation that constructs a simple parse tree:

class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self):
        "expression ::= ter { ('+'|'-') term }"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval

    def term(self):
        "term ::= factor { ('*'|'/') factor }"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval

    def factor(self):
        'factor ::= NUM | ( expr )'

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')

# The following example shows how it works

print('\n### ExpressionTreeBuilder ###\n')
e = ExpressionTreeBuilder()
print(e.parse('2 + 3'))
print(e.parse('2 + 3 * 4'))
print(e.parse('2 + (3 + 4) * 5'))
print(e.parse('2 + 3 + 4'))


