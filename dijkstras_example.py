# Step 1
distances = [
    {1: None},
    {2: None},
    {3: None},
    {4: None},
    {5: None},
    {6: None},
    {7: None},
    {8: None},
]
unvisited_nodes = [1, 2, 3, 4, 5, 6, 7, 8]

# Step 2
distances = [
    {1: 0},
    {2: None},
    {3: None},
    {4: None},
    {5: None},
    {6: None},
    {7: None},
    {8: None},
]
unvisited_nodes = [2, 3, 4, 5, 6, 7, 8]

# Step 3
distances = [
    {1: 0},
    {2: 156},
    {3: 175},
    {4: 125},
    {5: None},
    {6: None},
    {7: None},
    {8: None},
]
unvisited_nodes = [2, 3, 5, 6, 7, 8]

# Step 4
distances = [
    {1: 0},
    {2: 156},
    {3: 175},
    {4: 125},
    {5: 191},
    {6: None},
    {7: None},
    {8: None},
]
unvisited_nodes = [2, 3, 6, 7, 8]

# Step 5

distances = [
    {1: 0},
    {2: 156},
    {3: 175},
    {4: 125},
    {5: 191},
    {6: None},
    {7: 360},
    {8: 305},
]
unvisited_nodes = [2, 3, 6, 7]
