import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from FNLGMD.source.scorers.SAScore import sascorer
from FNLGMD.source.scorers.base_scorer import Scorer
from rdkit.Chem import MolFromSmiles, MolToSmiles, Descriptors, rdmolops
import networkx as nx


# Scoring function, this is taken directly from the FNLGMD repo and modified slightly to return logP
def score(population):

    smiles = population['smiles']
    smiles_rdkit = []
    for s in smiles:
        mol = MolFromSmiles(s)
        smi = MolToSmiles(mol,isomericSmiles=False)
        smiles_rdkit.append(smi)

    logP_values = []
    for i in range(len(smiles_rdkit)):
        logP_values.append(Descriptors.MolLogP(MolFromSmiles(smiles_rdkit[ i ])))

    SA_scores = []
    for i in range(len(smiles_rdkit)):
        SA_scores.append(-sascorer.calculateScore(MolFromSmiles(smiles_rdkit[ i ])))

    cycle_scores = []

    for i in range(len(smiles_rdkit)):
        cycle_list = nx.cycle_basis(nx.Graph(rdmolops.GetAdjacencyMatrix(MolFromSmiles(smiles_rdkit[ i ]))))

        if len(cycle_list) == 0:
            cycle_length = 0
        else:
            cycle_length = max([ len(j) for j in cycle_list ])
        if cycle_length <= 6:
            cycle_length = 0
        else:
            cycle_length = cycle_length - 6
        cycle_scores.append(-cycle_length)

    SA_scores_normalized = (np.array(SA_scores) - np.mean(SA_scores)) / np.std(SA_scores)
    logP_values_normalized = (np.array(logP_values) - np.mean(logP_values)) / np.std(logP_values)
    cycle_scores_normalized = (np.array(cycle_scores) - np.mean(cycle_scores)) / np.std(cycle_scores)

    SA_scores_normalized[np.isnan(SA_scores_normalized)] = 0.0
    logP_values_normalized[np.isnan(logP_values_normalized)] = 0.0
    cycle_scores_normalized[np.isnan(cycle_scores_normalized)] = 0.0

    targets = SA_scores_normalized + logP_values_normalized + cycle_scores_normalized
    population['fitness'] = targets

    return logP_values, SA_scores, cycle_scores, targets


# Function to normalize the scores in a table
def normalize_col(dat, col):
    return (dat[col] - dat[col].mean()) / dat[col].std(ddof=1)
