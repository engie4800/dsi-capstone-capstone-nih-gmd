

# run.py file

#!/usr/bin/env python

import os
import sys
import json
import numpy as np
import pandas as pd

sys.path.insert(0, 'src')

# Preparing data
from etl import score
from etl import normalize_col

# Creating figures
from figures import create_histogram
from figures import create_boxplot
from figures import create_heatmap
from figures import create_stackedbar
from figures import create_piechart

def main(targets):
    
    #config = json.load(open('config/data-params.json'))
    
    # Target to run the prep code
    if 'prep' in targets:
        
        # Prepping data
        basefp  = './FNLGMD/examples'
        tab = pd.read_csv(os.path.join(basefp, 'data_all_generations.csv'))
        tab.columns['smiles']
        
        # Add the scores to the DataFrame
        logP_values, SA_scores, cycle_scores, targets = etl.score(data)
        data['logP'] = logP_values
        data['SA'] = SA_scores
        data['cycle'] = cycle_scores
        data['fitness'] = targets
        
        # Normalize the columns that contribute to fitness
        tab['Normalized logP'] = normalize_col(tab, 'logP')
        tab['Normalized SA'] = normalize_col(tab, 'SA')
        tab['Normalized Cycle'] = normalize_col(tab, 'cycle')
        
        

        
    # Target to run the figures code 
    # Prep target may take a long time to run, so only run the figures target if
    # the prep files have already been created
    if 'figures' in targets:
        
        # Create Initial population histograms and write them to results file
        hist1 = create_histogram(scored, 'fitness')
        hist2 = create_histogram(scored, 'logP')
        hist3 = create_histogram(scored, 'SA')
        hist4 = create_histogram(scored, 'cycle_score')
        
        # Create 
        
        

    return                           

        
        
if __name__ == '__main__':
    # for testing run via:
    # python run.py test
    #
    # for all data run via:
    # python run.py clean prep
    targets = sys.argv[1:]
    main(targets)
    
    print("Data prepped for plots successfully.")