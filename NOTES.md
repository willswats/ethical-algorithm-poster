# Notes

- The distance values were rounded down for the sake of the graphs, however, in the algorithm the full value could be used.
- It's assumed that more buildings will result in more pedestrians, which would be an increase in risk.
- Both sides of the edge were taken into account when calculating the risk values, because it's assumed that dangers could appear from either side of the road.
- Flow chart doesn't include a part about what the current node is.
- The algorithm aims to find the safest route unless the safest route is an extremely long distance, however, currently there could be cases where a dangerous route is chosen over a medium distance green route (not extremely long), this could be remedied by increasing the colours risk for each zone.
