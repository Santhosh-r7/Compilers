out_file = open('output.s', 'w')

in_file = open('input.bob')

variables = {}

def output(*args):
    print(*args, file=out_file)

output('''.global main

.text
main:
push %rbp''')

for line in in_file:
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] == 'var':
        name = words[1]
        value = words[-1]
        variables[name] = value
    elif words[0] == 'print':
        name = words[1]
        output('lea percent_d(%rip), %rdi')
        output(f'mov {name}(%rip), %rsi')
        output('call printf')
    elif words[0] == 'printchar':
        variable = words[1]
        output('lea percent_c(%rip), %rdi')
        output(f'mov {variable}(%rip), %rsi')
        output('call printf')
    elif words[2] == '+=':
        lhs = words[0]
        rhs = words[2]
        output(f'mov {rhs}(%rip), %rdi')
        output(f'add %rdi, {lhs}(%rip)')

output('''pop %rbp
ret 

.data
hello: .string "hello, world!\\n"
percent_d: .string "%d\\n"
percent_c: .string "%c"''')

for name in variables:
    output(f'{name}: .quad {variables[name]}')
