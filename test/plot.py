import matplotlib.pyplot as plt


def test_plot():
    plt.figure(figsize=(12, 8))
    for i in range(M):
        X, Y = wiener_plot(x, h, a, b, end)
        plt.plot(X, Y)