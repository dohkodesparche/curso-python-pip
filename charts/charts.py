import  matplotlib.pyplot as plt

def generate_pie_chart():
    label=['A','B','C','D']
    value = [200,40,30]

    fig,ax =plt.subplots()
    ax.pie(value, label=label)
    plt.savefig('pie.png')
    plt.close()