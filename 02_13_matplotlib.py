import matplotlib.pyplot as plt

def generate_bar_chart(label, values):
    fig, ax = plt.subplot()
    ax.bar(label, values)
    plt.show

if __name__ == '__main__':
    labels = ['a', 'b', 'c', 'd']
    values = [10, 20, 30, 40]
    generate_bar_chart(labels, values)