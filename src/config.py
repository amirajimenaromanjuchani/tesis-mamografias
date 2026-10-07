"""
Configuración centralizada de la tesis.
Todas las rutas e hiperparámetros viven aquí.
"""

CONFIG = {
    'data': {
        'raw_root': '/content/tesis-mamografias/data/raw',
        'processed_root': '/content/tesis-mamografias/data/processed',
        'image_size': 224,
        'batch_size': 32,
        'num_workers': 2,
        # Mapeo BI-RADS: 1-2 = benigno, 5-6 = maligno
        # BI-RADS 0, 3, 4 se excluyen (según protocolo de tesis)
        'birads_benign': [1, 2],
        'birads_malignant': [5, 6],
    },
    'split': {
        'n_splits': 5,
        'test_size': 0.15,
        'seed': 88,  # semilla fija según protocolo
    },
    'models': ['resnet50', 'densenet121', 'efficientnet_b4'],
    'training': {
        'epochs': 100,
        'patience': 10,       # early stopping
        'lr': 1e-4,
        'weight_decay': 1e-5,
        'optimizer': 'adam',
    },
    'evaluation': {
        'bootstrap_n': 1000,  # IC 95%
        'metrics': ['accuracy', 'sensitivity', 'specificity', 'auc_roc', 'f1'],
    },
    'paths': {
        'metadata_csv': '/content/tesis-mamografias/data/processed/metadata.csv',
        'splits_csv': '/content/tesis-mamografias/splits/folds.csv',
        'checkpoints': '/content/tesis-mamografias/results/checkpoints',
        'figures': '/content/tesis-mamografias/results/figures',
        'tables': '/content/tesis-mamografias/results/tables',
    }
}
