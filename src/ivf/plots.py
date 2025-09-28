import matplotlib.pyplot as plt

def plot_rv_term(time_index, rv10, rv30, rv60, path):
    plt.figure(figsize=(8, 4))
    plt.plot(time_index, rv10, label="RV 10m")
    plt.plot(time_index, rv30, label="RV 30m")
    plt.plot(time_index, rv60, label="RV 1h")
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("RV")
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()
