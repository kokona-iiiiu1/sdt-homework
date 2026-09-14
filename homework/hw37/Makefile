CC = gcc
CFLAGS = -Wall
TARGET = hello.exe

.PHONY: all clean

all: $(TARGET)

$(TARGET): hello.c
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(TARGET)
