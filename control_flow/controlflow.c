#include <stdio.h>
#include <stdlib.h>

/*
compilation instructions:
gcc -fno-stack-protector -no-pie controlflow.c -o controlflow

decompilation instructions:
objdump -d -M intel --disassembler-color on controlflow | less
*/

void win() {
    puts("FLAG{control flow h4ck3d!}");
    fflush(stdout);
}

void vuln() {
    char name[10];
    printf("What is your name? ");
    scanf("%s", name);
    printf("Hi %s!\n", name);
}

int main(int argc, char **argv) {
    vuln();
    return EXIT_SUCCESS;
}
