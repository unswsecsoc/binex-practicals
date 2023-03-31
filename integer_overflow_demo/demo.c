#include <stdio.h>
#include <stdlib.h>

void* alloctMemory (unsigned int fileSize, unsigned int nameSize) {
	unsigned int total = fileSize + nameSize;
	void* buffer = malloc(total);
	printf("Allocating space: %d\n", total);
}

int main () {
	int size = 4294967295; // Maximal 32-bits integer (4294967295)!
	int name = 10;
	alloctMemory(size, name);
}