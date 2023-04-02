import matplotlib.pyplot as plt

def grid_profit(high, low, grid_no):
    asset = 10000
    grid_asset = asset / grid_no
    profit = 0
    for x in range(1, grid_no + 1):
        grid_range = (high - low) / grid_no
        grid_low = high - grid_range * x
        grid_high = grid_low + grid_range
        profit += grid_asset * 0.999 / grid_low * grid_high * 0.999 - grid_asset
    return profit

def analyze_grid(grid_no):
    grids_arr = []
    profit_arr = []
    for x in range(1, grid_no + 1):
        profit = grid_profit(1900,1700,x)
        if profit < 0:
            print(x, profit)
            break
        grids_arr.append(x)
        profit_arr.append(profit)
    return (grids_arr, profit_arr)


def grid_profit_graph(grid_no):
    x, y = analyze_grid(grid_no)
    plt.plot(x, y, marker='o')
    plt.title('Sample Data')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

grid_profit_graph(10000)