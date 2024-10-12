.global main

.text
main:
push %rbp
lea percent_d(%rip), %rdi
mov a(%rip), %rsi
call printf
lea percent_d(%rip), %rdi
mov a(%rip), %rsi
call printf
pop %rbp
ret 

.data
hello: .string "hello, world!\n"
percent_d: .string "%d\n"
a: .quad 10
b: .quad 4
