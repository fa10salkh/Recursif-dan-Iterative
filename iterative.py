import time

def tower_of_hanoi_iterative(n, source, destination, auxiliary):
    total_moves = 2 ** n - 1
    rods = {source: list(range(n, 0, -1)), destination: [], auxiliary: []}

    if n % 2 == 0:
        destination, auxiliary = auxiliary, destination

    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            move_disk(source, destination, rods)
        elif i % 3 == 2:
            move_disk(source, auxiliary, rods)
        elif i % 3 == 0:
            move_disk(auxiliary, destination, rods)

def move_disk(from_rod, to_rod, rods):
    if rods[from_rod] and (not rods[to_rod] or rods[from_rod][-1] < rods[to_rod][-1]):
        disk = rods[from_rod].pop()
        rods[to_rod].append(disk)
        print(f"Move disk {disk} from {from_rod} to {to_rod}")
    else:
        disk = rods[to_rod].pop()
        rods[from_rod].append(disk)
        print(f"Move disk {disk} from {to_rod} to {from_rod}")

n = int(input("Jumlah n (minimal 3) : "))
if n < 3 : n = 3
start_time = time.time()
tower_of_hanoi_iterative(n, "A", "C", "B")
end_time = time.time()

print(f"Iterative solution took {end_time - start_time:.6f} seconds for {n} disks.")