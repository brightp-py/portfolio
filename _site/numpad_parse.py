"""
numpad_parse.py.

A simple (yacc-less) compiler that converts Numpad code into Python code.
"""

import re
from collections import deque

R_WHITESPACE = re.compile(r'^\.*')
R_ASSIGN = re.compile(r'\*[0-9]+(/\*?[0-9]+)?\.[^.].*')
R_DEFINE = re.compile(r'\*[0-9]+\.$')
R_PARAM = re.compile(r'[0-9]+\.\.[0-9]+$')
R_NUMPARAM = re.compile(r'[0-9]+\.$')
R_LISTSTART = re.compile(r'[^\-]/\.')

R_COMMA = re.compile(r'(?<=[^/])\.')
OP3 = {
    '/+': '%',
    '*+': '**',
    '/-': '//',
    '*-': 'log'
}
R_MULTOP = re.compile(r'\*(?=[0-9])')   # backwards for last->first search
OP1 = [re.compile(r'-(?=[^*/])'), re.compile(r'\+(?=[^*/])')]
OP0 = {
    '..': '==',
    '.-': '<',
    '.+': '>'
}


# class Scope:

#     def __init__(self, parent = None):
#         """Create a new Scope object.
        
#         This object should only require a parent parameter, from which it will
#         infer its variables' types.
#         """
#         self.vartypes = {}


class Environment:

    def __init__(self):
        self.indentation = 0
        self.line = 0


def split_last(string: str, delim):
    """Split the given string along the last instance of the delim."""
    if isinstance(delim, re.Pattern):
        rhs, lhs = delim.split(string[::-1], maxsplit=1)
    else:
        rhs, lhs = string[::-1].split(delim[::-1], maxsplit=1)
    return lhs[::-1], rhs[::-1]


def eval_number(num: str):
    """Convert the numpad number to Python form.

    This just involves converting numbers that start with 0 to negatives.

    >>> eval_number("1")
    '1'
    >>> eval_number("0")
    '0'
    >>> eval_number("01")
    '-1'
    """
    if len(num) > 1 and num[0] == '0':
        return '-' + num[1:]
    return num


def eval_list(expr: str, use_help: bool):
    """Take a list expression (sans first bracket) and evaluate to Python.

    Only evaluates the first list given, even if multiple appear. Returns the
    rest as numpad code.

    >>> eval_list("4./.02/..1/.", False)
    ('[4, [-2], 1]', '')
    >>> eval_list("4/.+02+/.1/.", False)
    ('[4]', '+02+/.1/.')
    """
    # print('+', expr)
    if expr == '/.':
        return '[]', ''
    res = '['
    current = ''
    expr = '/.' + expr
    lists = {}
    ind = 2
    while ind < len(expr):
        char = expr[ind]
        if expr[ind:ind+2] == '/.' and current and current[-1] in '0123456789':
            res += eval_expr(current, use_help, False, lists) + ']'
            for key, val in lists.items():
                if key in res:
                    res = res.replace(key, val)
            # print('', expr, res)
            return res, expr[ind+2:]
        if char == '.' and expr[ind-1] != '/':
            res += eval_expr(current, use_help, False, lists) + ', '
            current = ''
        else:
            current += char
            # print('\t', current)
            if len(current) > 1 and current[-2:] == '/.':
                # print("INTERNAL LIST DETECTED")
                val, rem = eval_list(expr[ind+1:], use_help)
                key = 'L' + str(len(lists))
                lists['v_' + key] = val
                expr = expr[:ind-1] + '*' + key + rem
                current = current[:-2] + '*' + key
                ind += len(key) - 1
                # print('a', expr, current, ind)
        ind += 1
    assert False


def eval_expr(expr: str, use_help: bool, paren=True, lists=None):
    """Evaluate the given numpad expression as Python code.

    This involves transforming lists and splitting along operators (in order
    of precedence).
    """
    # lists
    lists = lists if lists else {}
    while '/.' in expr:
        lhs, rhs = expr.split('/.', maxsplit=1)
        val, rem = eval_list(rhs, use_help)
        key = 'L' + str(len(lists))
        lists['v_' + key] = val
        expr = lhs + '*' + key + rem
    print('-', expr)

    def final_format(expr: str):
        for key, val in lists.items():
            if key in expr:
                expr = expr.replace(key, val)
        if paren and any(op in expr for op in "+-*/%"):
            return '(' + expr + ')'
        return expr

    def last_operator(ops):
        res = None
        earliest = -1
        for oper in ops:
            loc = -1
            if isinstance(oper, re.Pattern):
                if search_res := oper.search(expr[::-1]):
                    loc = len(expr) - search_res.span()[1]
            elif oper in expr:
                loc = len(expr) - expr[::-1].find(oper[::-1]) - 1
            if loc > earliest:
                res = oper
                earliest = loc
        return res

    # operators with fourth priority
    # == < >
    if oper := last_operator(OP0):
        lhs, rhs = split_last(expr, oper)
        lhs, rhs = eval_expr(lhs, use_help), eval_expr(rhs, use_help)
        if use_help:
            f_name = {'..': 'eq', '.+': 'gt', '.-': 'lt'}
            res = f"{f_name[oper]}({lhs}, {rhs})"
        else:
            res = f"{lhs} {OP0[oper]} {rhs}"
        # print(expr, res)
        return final_format(res)

    # operators with third priority
    # + -
    if oper := last_operator(OP1):
        lhs, rhs = split_last(expr, oper)
        lhs, rhs = eval_expr(lhs, use_help), eval_expr(rhs, use_help)
        oper = '-' if oper == OP1[0] else '+'
        # if op == '-':
        #     print(lhs, rhs, lists)
        if oper == '-' and rhs in lists:
            res = f"{lhs}({lists[rhs][1:-1]})"
        elif use_help:
            f_name = {'+': 'add', '-': 'sub'}
            res = f"{f_name[oper]}({lhs}, {rhs})"
        else:
            res = f"{lhs} {oper} {rhs}"
        # print(expr, res)
        return final_format(res)

    # operators with second priority
    # * /
    oper = last_operator(['/', R_MULTOP])
    if oper == '/':
        lhs, rhs = split_last(expr, '/')
        if rhs[0] not in {'.', '+', '-'}:
            lhs, rhs = eval_expr(lhs, use_help), eval_expr(rhs, use_help)
            if use_help:
                res = f"div({lhs}, {rhs})"
            else:
                res = f"_pair({lhs} / {rhs})"
            # print(expr, res)
            return final_format(res)
    elif oper is not None:
        lhs, rhs = split_last(expr, R_MULTOP)
        lhs, rhs = eval_expr(lhs, use_help), eval_expr(rhs, use_help)
        if use_help:
            res = f"mul({lhs}, {rhs})"
        else:
            res = f"{lhs} * {rhs}"
        # print(expr, res)
        return final_format(res)

    # operators with first priority
    # % // ** log
    oper = last_operator(OP3)
    if oper == '*-':
        lhs, rhs = split_last(expr, oper)
        lhs, rhs = eval_expr(lhs, use_help), eval_expr(rhs, use_help)
        res = f"_pair(log({lhs}) / log({rhs}))"
        # print(expr, res)
        return final_format(res)
    if oper is not None:
        lhs, rhs = split_last(expr, oper)
        lhs, rhs = eval_expr(lhs, use_help), eval_expr(rhs, use_help)
        if use_help and oper == '/+':
            res = f"rem({lhs}, {rhs})"
        elif use_help and oper == '/-':
            res = f"flr({lhs}, {rhs})"
        else:
            res = f"{lhs} {OP3[oper]} {rhs}"
        # print(expr, res)
        return final_format(res)

    # lone variable
    if expr[0] == '*':
        if expr[1] == 'L':
            int(expr[2:])
        else:
            int(expr[1:])
        if expr[1] == '0' and len(expr) > 2:
            return 'p_' + expr[1:]
        res = 'v_' + expr[1:]
        if res in lists:
            return lists[res]
        return res

    # number
    return eval_number(expr)


def add_helpers(np_code: str):
    """Add any extra helper functions the given code might need.

    == eq
    >  gt
    <  lt
    +  add
    -  sub
    *  mul
    /  div
    /+ rem
    /- flr
    """
    op_name = [
        '_pair', 'eq', 'gt', 'lt', 'add', 'sub', 'mul', 'div', 'rem', 'flr']
    ops = {}
    with open("numpad_helpers.py", 'r', encoding='utf-8') as file:
        text = file.read()
    for oper in op_name:
        ops[oper] = text.split(f"# {oper}")[1]

    to_add = ""
    for oper, py_code in ops.items():
        if oper in np_code or (oper == '_pair' and 'div' in np_code):
            to_add += py_code[1:] + '\n'

    return to_add + np_code


def eval_code(np_code: str):
    """Transform the given numpad code into Python, splitting along spaces.

    >>> test = ('*1.2/3+4 '
                '*1.2*3/4*5 '
                '*337191. '
                '.1..4 '
                '.1. '
                './*01.-0 '
                '..*1.*337191-/.01**01+1/. '
                '..*00.32-*1 '
                '.- '
                '..*1.0 '
                '..*2.*01 '
                '..+/*2.+0 '
                '...*3.*2/+2 '
                '...*1.*1+*3 '
                '...*2.*2/-2 '
                '... '
                '..*00.*1 '
                '.. '
                '. '
                )
    >>> print(convert_to_python(test))
    v_1 = (2 / 3) + 4
    v_1 = ((2 * 3) / 4) * 5
    def v_337191(p_01=4):
        if p_01 < 0:
            v_1 = v_337191((-1 * p_01) + 1)
            v_00 = 32 - v_1
        else:
            v_1 = 0
            v_2 = p_01
            while v_2 > 0:
                v_3 = v_2 % 2
                v_1 = v_1 + v_3
                v_2 = v_2 // 2
            v_00 = v_1
        return v_00
    """
    res = ""
    indentation = 0
    has_lists = False
    for line in np_code.split():
        if line.count('-/.') * 2 < line.count('/.'):
            has_lists = True
            break

    current_func = None
    current_param = {}
    scope_stack = deque()

    for line in np_code.split():
        line = R_WHITESPACE.sub('', line)

        # blank line, indicating the end of a scope
        if line == '':
            assert current_func is None
            if scope_stack.pop():
                res += '    ' * indentation + "return v_00\n\n"
            indentation -= 1

        # assignment line, with a variable, a dot, and an expression
        elif R_ASSIGN.match(line):
            assert current_func is None
            v_name, expr = line.split('.', maxsplit=1)
            if indentation == 0 and v_name == "*00":
                res += f"print({eval_expr(expr, has_lists, False)})"
            else:
                if '/' in v_name:
                    lhs, rhs = v_name.split('/')
                    v_name = f"v_{lhs[1:]}[{eval_expr(rhs, has_lists, False)}]"
                else:
                    v_name = 'v_' + v_name[1:]
                expr = eval_expr(expr, has_lists, False)
                res += '    ' * indentation + f"{v_name} = {expr}\n"

        # function definition, with a variable and a dot
        elif R_DEFINE.match(line):
            assert current_func is None
            current_func = 'v_' + line[1:-1]

        # default parameter
        elif R_PARAM.match(line):
            assert current_func is not None
            p_name, value = line.split('..')
            p_name = 'p_0' + p_name
            current_param[p_name] = eval_number(value)

        # number of parameters
        elif R_NUMPARAM.match(line):
            assert current_func is not None
            res += '    ' * indentation + f"def {current_func}("

            param_texts = []
            num_params = int(line[:-1])
            for p_name in range(1, num_params + 1):
                p_name = 'p_0' + str(p_name)
                if p_name not in current_param:
                    param_texts.append(p_name)
            for p_name in sorted(current_param):
                param_texts.append(f"{p_name}={current_param[p_name]}")
            res += f"{', '.join(param_texts)}):\n"

            current_func = None
            current_param = {}
            scope_stack.append(True)
            indentation += 1

        # while statement
        elif line[:2] == '+/':
            assert current_func is None
            expr = eval_expr(line[2:], has_lists, False)
            res += '    ' * indentation + f"while {expr}:\n"
            scope_stack.append(False)
            indentation += 1

        # elif statement
        elif line[:2] == '-/':
            assert current_func is None
            expr = eval_expr(line[2:], has_lists, False)
            res += '    ' * (indentation - 1) + f"elif {expr}:\n"

        # if statement
        elif line[0] == '/':
            assert current_func is None
            expr = eval_expr(line[1:], has_lists, False)
            res += '    ' * indentation + f"if {expr}:\n"
            scope_stack.append(False)
            indentation += 1

        # else statement
        elif line == '-':
            assert current_func is None
            res += '    ' * (indentation - 1) + "else:\n"

        else:
            # print(line)
            assert False

    if 'log' in res:
        res = "from math import log\n\n" + res

    return add_helpers(res), res


def convert_to_python(np_code: str):
    """Transform the given numpad code into Python, splitting along spaces.

    If the code fails to compile, returns 'Could not compile.'
    """
    try:
        return eval_code(np_code)
    except Exception as err:
        return "Could not compile: " + str(err), "Could not compile"


if __name__ == "__main__":
    print("Testing...")
    TEST = """\
    *2160.
    .1.
    .*1.*01/+10
    .*2.*01/+100/-10
    .*3.*01/+1000/-100
    .*4.*01/-1000
    ./*1.+*4
    ..*5.*1
    ..*1.*4
    ..*4.*5
    ..
    ./*2.+*3
    ..*5.*2
    ..*2.*3
    ..*3.*5
    ..
    ./*1.+*3
    ..*5.*1
    ..*1.*3
    ..*3.*5
    .-/*2.+*4
    ..*5.*2
    ..*2.*4
    ..*4.*5
    ..
    .*5.*3+*4
    .*00.*5*10+*1+*2
    .
    """
    _, code = eval_code(TEST)
    print(code)
