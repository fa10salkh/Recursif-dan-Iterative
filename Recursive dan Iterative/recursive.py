import time

def tower_of_hanoi_recursive(n, source, destination, auxiliary):
    if n == 1:
        return
    tower_of_hanoi_recursive(n - 1, source, auxiliary, destination)
    tower_of_hanoi_recursive(n - 1, auxiliary, destination, source)

n = 20
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 21
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 22
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 23
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

def tower_of_hanoi_recursive(n, source, destination, auxiliary):
    if n == 1:
        return
    tower_of_hanoi_recursive(n - 1, source, auxiliary, destination)
    tower_of_hanoi_recursive(n - 1, auxiliary, destination, source)

n = 20
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 21
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 22
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 23
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 24
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 25
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")


print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 24
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")

n = 25
start_time = time.time()
tower_of_hanoi_recursive(n, "A", "C", "B")
end_time = time.time()

print(f"Recursive solution took {end_time - start_time:.6f} seconds for {n} disks.")