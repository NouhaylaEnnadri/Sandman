import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np


def visualise (X,labels, model):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab10', s=50)

   
    plt.title(f"Visualization of the clustering {model}", fontsize=14)
    plt.xlabel("HPC")
    plt.ylabel("PFC")
    plt.colorbar(label="clustering label")
    plt.show()


def plot_3d_clusters(data, labels, col_x='EMG', col_y='HPC', col_z='PFC', 
                     sample_n=10000, output_file=None):
    """
    Génère un graphique 3D des clusters.

    Args:
        data (pd.DataFrame): Le dataframe contenant les données brutes.
        labels (array-like): Les labels prédits par le modèle (le tableau de clusters).
        col_x (str): Nom de la colonne pour l'axe X (ex: 'EMG').
        col_y (str): Nom de la colonne pour l'axe Y (ex: 'HPC').
        col_z (str): Nom de la colonne pour l'axe Z (ex: 'PFC').
        sample_n (int): Nombre de points à afficher (pour éviter de faire ramer Matplotlib).
                        Mettre None pour tout afficher.
        output_file (str): Si fourni, sauvegarde le graphique dans ce fichier (ex: 'plot.png').
    """
    
    # 0. Vérification de sécurité : data doit être un DataFrame
    if not isinstance(data, pd.DataFrame):
        raise TypeError(f"Erreur: Le paramètre 'data' doit être un pandas.DataFrame. Type reçu : {type(data)}.\n"
                        "Si vos données sont en NumPy, convertissez-les d'abord : pd.DataFrame(data, columns=['...'])")

    # 1. Création d'une copie pour ne pas modifier le dataframe original
    df_plot = data.copy()
    
    # 2. Ajout des labels au dataframe temporaire
    # On s'assure que les labels sont bien alignés avec les données
    if len(labels) != len(df_plot):
        raise ValueError(f"Erreur: La longueur des labels ({len(labels)}) ne correspond pas à la longueur des données ({len(df_plot)}).")
        
    # On utilise np.array() pour forcer l'assignation par position et ignorer les index pandas
    # Cela évite les erreurs si 'labels' est une Series avec des index différents/mélangés
    df_plot['Cluster_Label'] = np.array(labels)

    # 3. Échantillonnage (Subsampling) pour la performance
    # Matplotlib gère mal les scatter plots 3D avec > 10k-20k points
    if sample_n and len(df_plot) > sample_n:
        print(f"--> Échantillonnage de {sample_n} points aléatoires pour la visualisation...")
        df_sampled = df_plot.sample(n=sample_n, random_state=42)
    else:
        df_sampled = df_plot

    # 4. Configuration du graphique
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Vérification que les colonnes existent
    for col in [col_x, col_y, col_z]:
        if col not in df_sampled.columns:
            raise KeyError(f"La colonne '{col}' n'existe pas dans le DataFrame. Colonnes disponibles : {list(df_sampled.columns)}")

    # 5. Création du Scatter plot
    scatter = ax.scatter(
        df_sampled[col_x], 
        df_sampled[col_y], 
        df_sampled[col_z], 
        c=df_sampled['Cluster_Label'], 
        cmap='viridis', 
        s=5,          # Taille des points
        alpha=0.6     # Transparence
    )

    # 6. Labels et Titres
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    ax.set_zlabel(col_z)
    ax.set_title(f'Visualisation 3D des Clusters\n(Axes: {col_x}, {col_y}, {col_z})')

    # 7. Barre de couleur (Légende)
    cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
    cbar.set_label('ID du Cluster')

    # 8. Sauvegarde ou Affichage
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"--> Graphique sauvegardé sous : {output_file}")
    else:
        plt.show()