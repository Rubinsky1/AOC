# Gebruik meerdere cores voor het compileren
MAKEFLAGS += -j

# Zoek naar alle .cc en .h bestanden in het project
cc := $(shell find . -iname "*.cc")
hs := $(shell find . -iname "*.h")

# Combineer de bestanden in een enkele lijst
src := $(cc) $(hs)

# De naam van de uitvoerbare file
out := main


# Compileer de uitvoerbare file
$(out): $(src)
	g++ -Wall -Wextra -Wunused-parameter -std=c++11 -Og -g -o $(out) $(cc)

# Automatisch hercompileren van .cc-bestanden naar .o-bestanden
%.o: %.cc
	g++ -c -Wall -Wextra -Wunused-parameter -std=c++11 -Og -g -o $@ $<


# Run het programma onder Valgrind
.PHONY: valgrind
valgrind: $(out)
	valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./$(out)

# Schoon het project (verwijder .o bestanden en de uitvoerbare file)
.PHONY: clean
clean:
	rm -f $(out) *.o
