
import pandas as pd

def eval_metrics(y_pred: pd.Series, y_test: pd.Series, clf: bool = True,c_matrix: bool = False) -> dict or tuple:
    '''
    Objetivo:
    ---
    Evaluar el modelo supervisado utilizando las métricas correspondientes.

    args.
    ---
    y_pred: La predicción del modelo.
    y_test: El resultado de prueba real.
    clf: bool; True: si es clasificación. (por defecto)
                False: si es regresión.
    c_matrix: bool; True: obtener la matriz de confusión.
                    False: no obtener la matriz. (por defecto)

    ret.
    ---
    dict; resultados de las métricas.

    * Excepto cuando c_matrix es True y clf es True:
        dict, array; resultados de las métricas, matriz de confusión.

    '''

    if clf:
        
        clf_metrics = {
            'ACC' : accuracy_score(y_test,y_pred),
            'Precision' : precision_score(y_test,y_pred),
            'Recall' : recall_score(y_test,y_pred),
            'F1' : f1_score(y_test,y_pred),
            'ROC' : roc_auc_score(y_test,y_pred),
            'Jaccard' : jaccard_score(y_test,y_pred)
        }
        
        if c_matrix:
            confusion_mtx = confusion_matrix(y_test,y_pred)
            return clf_metrics,confusion_mtx # type: ignore
        else:
            return clf_metrics

    else:

        reg_metrics = {
            'MAE' : mean_absolute_error(y_test,y_pred),
            'MAPE' : mean_absolute_percentage_error(y_test,y_pred),
            'MSE' : mean_squared_error(y_test,y_pred),
            'R2' : r2_score(y_test,y_pred)
        }   

        return reg_metrics  



def get_model(model_name):
    models = {
        'LogReg': LogisticRegression(),
        'KNNC': KNeighborsClassifier(),
        'DTC': DecisionTreeClassifier(),
        'RFC': RandomForestClassifier(),
        'BagC': BaggingClassifier(),
        'AdaBC': AdaBoostClassifier(),
        'GBC': GradientBoostingClassifier(),
        'SVC': SVC(),
        'XGBC': XGBClassifier(),
        'VC': VotingClassifier(estimators=[('RFC', RandomForestClassifier())]),
        'LDA': LinearDiscriminantAnalysis(),
        'SQL': Sequential()
    }

    if model_name in models:
        return models[model_name]
    else:
        raise ValueError(f"Model '{model_name}' not found in the list of available models.")

# Ejemplo de uso:
model_name = 'LogReg'  # Puedes cambiar el nombre del modelo aquí
model = get_model(model_name)
print(f"Modelo {model_name} creado exitosamente.")