# 0x09. Island Perimeter

`Algorithm` `Python`
![island-perimeter](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN0AAADVCAMAAADkSQVFAAAAD1BMVEWZ2eq5elf///8AAAD/8gBmU946AAAChUlEQVR4nO3dy3bDIAxFUYr9/9/crHTQ+BUkgUDY546JfHf8mJQ6Kd85aXQB16CbN2VdUqZDaXEuy2hRIcEnR27pGszdHaiDrCd3O3cU7iRGzvajYXUVudCNrtUo99alU93oUs3yPN3oTg2Dbt4cdaMbNc2jdYsuqyjKoYqUdKlGJ8M58lx14c5dKuok1/d76br8CPNaKp6qKOCpe50Uqe61tKayYulWVzEcXXddQidJfF3NcHTozAXQmYfH1KV/XdVwdOjMBdCZh6NDZy5Q0NUNR4fOXOBiKbpy0KEzF0BnHo4OnbkAOvPw4LrK4ejQmQugMw9Hh85cAJ19eMQdHamkc9pi4zJVr5PV0Bbxmcq5+9QpbqbFZWn1LfpFt8ofhD66tfrxig5dSF1Ghw4dOnToNrozHjp06NChe5Auo0OHDh06dOjQoRujy0/RnfDQoUOHDh26W+jyd93kOzpKusXtZUUeY/U6WQs1z2Us5+77tXyViDsY2+nWgLtPN7rbvaMDnSwBdRmdLOjQmQugMw9Hh85c4LA0oxMmvu5e789EJx2ODp25ADrz8HC6jE46HB06cwF05uHoBuvu9NsWt9ZldOjeQYfOXACdeTi6eXXBdnRkmW74z74potfJcDF4nLtPnc8OxiD3neJBqND1eGaiu5lux0OHDh068dKMDh06dOjQoUOHDh06dOjQoUPXWbf7BDp06NChQ4cOHbpRuml3dMh0i2o3jmKpSwq6k+9D1vjdWbE0im7Oc3f6l2XpNR4/6ObN43SjKzUMuomDbt4cdKMLNU1Rl9tkhO38f0m8M4TXTdcROU7nTNwfaITu78gunt0xOlkuj98Sc5zuUzpI0M2bXxINmpyD1K1zAAAAAElFTkSuQmCC)

# Tasks

`0. Island Perimeter`

Create a function `def island_perimeter(grid)`: that returns the perimeter of the island described in `grid`:

* 'grid` is a list of list of integers:

 * 0 represents water
 * 1 represents land
 * Each cell is square, with a side length of 1
 * Cells are connected horizontally/vertically (not diagonally).
 * `grid` is rectangular, with its width and height not exceeding 100
* The grid is completely surrounded by water
* There is only one island (or nothing).
* The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

```
mily@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

mily@ubuntu:~/0x09$ 
mily@ubuntu:~/0x09$ ./0-main.py
12
mily@ubuntu:~/0x09$ 

```
