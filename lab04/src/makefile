CC := gcc
OBJ = *.c
APPNAME := app.exe
FLAGS=-lpthread -O0 -std=c99 -Wall -pg -lc
THREADS=16
TYPE=1

build:
	$(CC) -o $(APPNAME) $(OBJ) $(FLAGS)

clean:
	rm -rf *.exe *.out && cd src && rm -rf *.o *.hi *.exe *.out

run: build
	./$(APPNAME) ${THREADS} ${TYPE}
