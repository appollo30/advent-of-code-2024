def part_1(reports):
    count = 0 # The number of safe reports
    for r in reports:
        m = len(r)
        diff = 0
        for j in range(m-1):
            if (diff > 0 and r[j] > r[j+1]) or (diff < 0 and r[j] < r[j+1]):
                break
            diff = r[j+1] - r[j]
            # If diff > 0 then r is increasing between i and i+1
            # If diff < 0 then r is decreasing between i and i+1
            if abs(diff) < 1 or abs(diff) > 3:
                break
        else:
            count += 1
    return count
