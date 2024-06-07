import  matplotlib.pyplot as plt

def generate_pie_chart():
    labels=['A','B','C','D']
    values = [200,40,30]

    fig, ax =plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()