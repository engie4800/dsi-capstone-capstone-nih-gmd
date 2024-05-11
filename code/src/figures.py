import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_histogram(data, colname, fn='hist.png'):
    
    '''
    Function to create histogram of molecule fitness
    '''
    plt.figure(figsize=(6, 4))
    
    sns.histplot(data[colname], bins=25)
    plt.xlabel('Score')
    plt.title(f'{colname.capitalize()} Score Distribution')
    plt.savefig(f'./results/figures/{fn}')
    return None


def create_boxplot(data, xlabel, ylabel, fn='box.png'):
    
    '''
    Function to create boxplots of molecule fitness
    '''
    
    # Creating box plots
    plt.figure(figsize=(6, 4))
    plt.boxplot(data)

    # Setting the labels and title, if necessary
    plt.title(f'Box Plots of Fitness Score for {ylabel.capitalize()}')
    plt.xlabel(xlabel)
    plt.xticks(ticks = [1, 2, 3, 4, 5], labels=[0.1, 0.15, 0.2, 0.25, 0.3])
    plt.ylabel('Score')
    plt.savefig(f'./results/figures/{fn}')

    return None


def create_heatmap(data, fn='heatmap.png'):
    
    '''
    Function to create heatmap of molecule fitness
    '''
    
    # Create the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(data, cmap="coolwarm", annot=True)
    plt.title('Heatmap of Fitness Scores')
    plt.xlabel('Mate Probability')
    plt.ylabel('Mutate Probability')
    plt.xticks(ticks=[0.5, 1.5, 2.5, 3.5, 4.5], labels=[0.5, 0.6, 0.7, 0.8, 0.9])
    plt.yticks(ticks=[0.5, 1.5, 2.5, 3.5, 4.5], labels=[0.1, 0.15, 0.2, 0.25, 0.3])
    plt.savefig(f'./results/figures/{fn}')
    return None



def create_stackedbar(data, fn='stackedbar.png'):
    
    '''
    Function to create stacked bar chart of output population composition
    '''

    categories = ['All molecules', 'Balanced', 'Lipophilic', 'Hydrophilic']
    values1 = data.iloc[0].values
    values2 = data.iloc[1].values
    values3 = data.iloc[2].values

    x = np.arange(len(categories))

    # Plotting stacked bar chart
    plt.bar(x, values1, label='Balanced')
    plt.bar(x, values2, bottom=values1, label='Hydrophilic')
    values1_plus_values2 = np.add(values1, values2).tolist()
    plt.bar(x, values3, bottom=values1_plus_values2, label='Lipophilic')

    plt.xlabel('Initial Population')
    plt.ylabel('Proportion')
    plt.title('Stacked Bar Chart of Population Composition')
    plt.xticks(x, categories)
    plt.legend()
    plt.savefig(f'./results/figures/{fn}')

    return None

def create_piechart(data, fn='piechart.png'):
    
    '''
    Function to create pie chart of molecule population composition
    '''
    
    
    fig, ax = plt.subplots()
    ax.pie(epoch_10['LogP_label'].value_counts().values/epoch_10['LogP_label'].value_counts().values.sum(), 
           labels=list(epoch_10['LogP_label'].value_counts().index), autopct='%1.1f%%')
    plt.title('LogP score distribution for JTVAE after 10 epochs')
    plt.savefig(f'./results/figures/{fn}')
    return None