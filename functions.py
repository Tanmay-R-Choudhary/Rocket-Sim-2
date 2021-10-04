import matplotlib.pyplot as plt
plt.style.use("dark_background")

def plot(mode, *data):
    if mode=="new":
        for x,y in data:
            plt.figure()
            plt.plot(x, y)
    if mode=="same":
        plt.figure()
        for x,y in data:
            plt.plot(x, y)
    
    plt.show()