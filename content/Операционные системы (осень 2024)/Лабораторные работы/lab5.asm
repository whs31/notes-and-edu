section .text
    global _start

section .data

section .text

; pt. 4 
swap:
    mov rax, [rdi]
    mov rdx, [rsi]
    mov [rdi], rdx
    mov [rsi], rax
    ret

; pt. 5
min:
    cmp rdi, rsi
    jae .return_rdi
    mov rax, rsi
    ret
.return_rdi:
    mov rax, rdi
    ret

; pt. 6
pow:
    mov rax, 1
    cmp rsi, 0
    je .return
.loop:
    imul rax, rdi
    dec rsi
    jnz .loop
.return:
    ret

_start:
    xchg rsi, rdx   ;pt. 1 (swap rsi and rdx)

    add rsi, rdx    ;pt. 2 (add rdx to rsi)

    mov rax, rsi    ;pt. 3 (fahrenheit to celsius)
    sub rax, 32
    imul rax, 5
    mov rdx, 9
    idiv rdx
    mov rsi, rax

    mov ebx,0       ;process' exit code
    mov eax,1       ;system call number (sys_exit)
    int 0x80        ;call kernel - this interrupt won't return