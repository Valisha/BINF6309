#!/usr/bin/env python3
"""
Script for analysing EEG data taken as a matlab file input. Output includes three excel files that would contain details about the most consistent features obtained from the pipeline
"""


def loading_required_libraries():
    import os, sys, re
    import scipy.io as sio
    from scipy import stats
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import scipy.io as sio
    from sklearn import metrics
    from sklearn.utils import check_random_state, resample
    from sklearn.preprocessing import normalize, LabelEncoder, scale, MinMaxScaler, PolynomialFeatures, MultiLabelBinarizer
    from sklearn.mixture import GaussianMixture
    from sklearn.linear_model import LogisticRegression, LinearRegression 
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import cross_val_score, train_test_split, KFold, StratifiedKFold, RandomizedSearchCV, GridSearchCV, StratifiedShuffleSplit
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, BaggingClassifier, RandomTreesEmbedding, AdaBoostClassifier, RandomForestRegressor
    from sklearn.feature_selection import SelectKBest, f_classif, VarianceThreshold, RFE, RFECV
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")
    import itertools
    import operator
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score,classification_report, f1_score, mean_squared_error, confusion_matrix, average_precision_score
    import multiprocessing
    import collections, functools, operator
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    idx = pd.IndexSlice
    import hdf5storage


def get_input():
    
    """
    Takes in the input from the python notebook, as 3 required matlab files, the group of interest and the accuracy threshold required for the workflow
    """

    path_mat = str(input("Path to the complete non-reshaped matlab file: "))
    path_binned = str(input("Path to binned matlab file: "))
    path_2hz = str(input("Path to 2Hz matlab file: "))
    grouping = str(input("Grouping (WT/HET): "))
    acc_thresh = float(str(input("Accuracy threshold: ")))
    return(path_mat, path_binned, path_2hz, grouping, acc_thresh)
def to_str(var):
    return(str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[2:-2])
def load_data(scipy_file_2hz, results_reshaped_pxx_2hz, results_reshaped_pxx_binned, scipy_file_binned, grouping, excluded_mice):
    
    """ To load the 2Hz bins data from reshaped matlab dataset"""

    labels_2hz = ['0.5-2', '2-4', '4-6', '6-8', '8-10', '10-12', '12-14', '14-16', '16-18', '18-20', '20-22', '22-24', '24-26', '26-28', '28-30', '30-32', '32-34', '34-36', '36-38', '38-40', '40-42', '42-44', '44-46', '46-48', '48-50', '50-52', '52-54', '54-56', '56-58', '58-60', '60-62', '62-64', '64-66', '66-68', '68-70', '70-72', '72-74', '74-76', '76-78', '78-80', '80-82', '82-84', '84-86', '86-88', '88-90', 'Broadband (0.5-90)']
    labels_binned = ['Gamma (30-90)','Low Gamma (30-45)','Med Gamma (45-60)','High Gamma (60-90)','Delta (0.5-4)','Theta (4-7.5)','Alpha (7.5-12)','Alpha1 (7.5-10)','Alpha2 (10-12)','Beta (12.5-30)','Beta1 (13-19)','Beta2 (20-30)',
          'Broadband (0.5-90)']
    doses = []
    labels_to_choose = ['Low Gamma (30-45)','Med Gamma (45-60)','High Gamma (60-90)']
    final_dict = pd.DataFrame()
    for i in range(len(results_reshaped_pxx_2hz)):
        if len(scipy_file_2hz['results_reshaped']['dose'][i][0])==1:
            dose = str(scipy_file_2hz['results_reshaped']['dose'][i][0][0]) # gets the dose 
            if len(dose) > 3:
                doses.append(dose)
    unique_doses = np.unique(np.array(doses[:-1]))
    for d in unique_doses:
        new_dict_2hz = {}
        new_dict_binned = {}
        groups = []
        for i in range(len(results_reshaped_pxx_2hz)):
            group = str(scipy_file_2hz['results_reshaped']['group'][i][0][0])
            groups.append(group)
            mouse_id = str(scipy_file_2hz['results_reshaped']['mouse'][i][0][0]) # gets the mouse_id
            if len(scipy_file_2hz['results_reshaped']['dose'][i][0])==1:
                dose = str(scipy_file_2hz['results_reshaped']['dose'][i][0][0]) 
            if group==grouping and mouse_id not in excluded_mice and d==dose:
                df_2hz = pd.DataFrame(pd.DataFrame(results_reshaped_pxx_2hz[i]).loc[0,0])
                df_2hz.columns = labels_2hz
                df_2hz = df_2hz.iloc[:, 0:15]
                new_dict_2hz.update({mouse_id:df_2hz})
        if (grouping not in groups):
            print("Please check your grouping, no group of this name found")
            sys.exit()
        d_new_2hz = pd.concat(new_dict_2hz, keys = new_dict_2hz.keys())

        for j in range(len(results_reshaped_pxx_binned)):
            group_binned = str(scipy_file_binned['results_reshaped']['group'][j][0][0])
            mouse_id_binned = str(scipy_file_binned['results_reshaped']['mouse'][j][0][0])
            if len(scipy_file_binned['results_reshaped']['dose'][j][0])==1:
                dose_binned = str(scipy_file_binned['results_reshaped']['dose'][j][0][0])
            if group_binned == grouping and mouse_id_binned not in excluded_mice and d == dose_binned:
                df_binned = pd.DataFrame(pd.DataFrame(results_reshaped_pxx_binned[j]).loc[0,0])
                df_binned = df_binned.loc[:,0:12]
                df_binned.columns = labels_binned
                df_binned = df_binned.loc[:, labels_to_choose]
                new_dict_binned.update({mouse_id_binned:df_binned})
        d_new_binned = pd.concat(new_dict_binned, keys = new_dict_binned.keys())
        d_new = pd.concat([d_new_2hz, d_new_binned], axis = 1)
        d = to_str(d)
        d_new['target'] = d
        final_dict = final_dict.append(d_new)
        print(final_dict.columns)
    return(final_dict, unique_doses)

def bootstrap_data(dataset, iterations):
    """saving the bootstraped data in a dictionary"""
    new_dict_X_train, new_dict_X_test, new_dict_y_train, new_dict_y_test = [], [], [], []
    sss = StratifiedShuffleSplit(n_splits = iterations, test_size = 0.5, random_state = 0)
    y = dataset.loc[:,'target']
    data = dataset.drop(labels = 'target', axis = 1, inplace = False)
    sss.get_n_splits(data,y)
    # Stratified sample split into training and testing dataset
    for train_idx, test_idx in sss.split(data,y):
        new_dict_X_train.append(data.iloc[train_idx, :])
        new_dict_X_test.append(data.iloc[test_idx, :])
        new_dict_y_train.append(y[train_idx])
        new_dict_y_test.append(y[test_idx])
    return(new_dict_X_train, new_dict_X_test, new_dict_y_train, new_dict_y_test)

def rfe_modelling(iterations):

    """modelling and feature selection with training and testing dataset just for LR, SVM and LDA"""

    X_train = new_dict_X_train[iterations]
    y_train = new_dict_y_train[iterations]
    y_test = new_dict_y_test[iterations]
    X_test = new_dict_X_test[iterations]
    rfe = RFE(estimator = models[m], n_features_to_select = num_features_to_choose, step = 5)
    rfe.fit(X_train, y_train) ## fitting the model
    feats = [X_train.columns[i] for i in range(len(X_train.columns)) if rfe.ranking_[i]==1] ## list for getting hte features selected by rfe 
    features.append(feats) ## appending these selected features into another megalist so that we can run Counter() on the lsit for stability score and feature importance
    select_X_train = X_train[feats] ## using only the selected features from RFE to train the model again for feature importance
    select_X_test = X_test[feats]
    model.fit(select_X_train, y_train)
    y_pred = models[m].predict(select_X_test)
    dict1 = models[m].coef_[0] ## feature importances 
    d = {feats[i]:dict1[i] for i in range(len(dict1))}
    fl.append(d) ## getting teh features and their feature importances as a dictionary and then appending that dictionary to a list
    acc.append(metrics.accuracy_score(y_pred, y_test))
    f1.append(metrics.f1_score(y_pred, y_test))
    return(features, fl, acc, f1)

def rfe_modelling_rf(iterations):
    """modelling and feature selection with training and testing dataset just for Random Forest"""
    X_train = new_dict_X_train[iterations]
    y_train = new_dict_y_train[iterations]
    y_test = new_dict_y_test[iterations]
    X_test = new_dict_X_test[iterations]
    rfe = RFE(estimator = models[m], n_features_to_select = num_features_to_choose, step = 5)
    rfe.fit(X_train, y_train) ## fitting the model
    feats = [X_train.columns[i] for i in range(len(X_train.columns)) if rfe.ranking_[i]==1] ## list for getting hte features selected by rfe 
    features.append(feats) ## appending these selected features into another megalist so that we can run Counter() on the lsit for stability score and feature importance
    select_X_train = X_train[feats] ## using only the selected features from RFE to train the model again for feature importance
    select_X_test = X_test[feats]
    model.fit(select_X_train, y_train)
    y_pred = models[m].predict(select_X_test)
    dict1 = model[m].feature_importances_ ## feature importances 
    d = {feats[i]:dict1[i] for i in range(len(dict1))}
    fl.append(d) ## getting teh features and their feature importances as a dictionary and then appending that dictionary to a list
    acc.append(metrics.accuracy_score(y_pred, y_test))
    f1.append(metrics.f1_score(y_pred, y_test))
    return(features, fl, acc, f1)


def unzipping_multiprocessing_data(l1):
    """unzips the multiprocessing output"""
    features_new = []
    fl_new = []
    acc_new = []
    f1_new = []
    for i in range(len(l1)):
        features_new.append(l1[i][0][0])
        fl_new.append(l1[i][1][0])
        acc_new.append(l1[i][2][0])
        f1_new.append(l1[i][3][0])
    a_new1 = np.mean(acc_new)
    f1_new1 = np.mean(f1_new)
    return(features_new, fl_new, a_new1, f1_new1)
def results(features_new, fl_new,iterations, a_new1, f1_new1, model_name):
    """takes the data from the modelling, calculates stability score, average accuracy, f1-score so that it can be shown in a dataframe format"""
    features_flat_list = [item for sublist in features_new for item in sublist] ## creating a flat list for counter function
    result_feats = dict(functools.reduce(operator.add, map(collections.Counter, fl_new))) ## functools.reduce function adds the values of the repeating keys
    sorted_feats = dict(sorted(result_feats.items(), key=operator.itemgetter(1), reverse=True)) ## sorting in decreasing order to get the feature = key with maximum feaure importance 
    final_feats = list(dict(itertools.islice(sorted_feats.items(), num_features_to_choose)).keys()) ## selecting only a set of top features 
    ss = {i:((features_flat_list.count(i)/iterations)*100) for i in final_feats} ## getting the stability score for top 10 features
    ## count() function calculates how many times each value is repeating in from the pool of values provided
    vals = list(ss.values()) ## storing only the percentage stability score in a different list
    cum_ss = sum(vals)/num_features_to_choose ## calculating the average of all the stability scores 
    stability_score = {features_new.count(y):y for y in features_new} # counting the number of times each list is repeating
    # 'features' is a list of lists containing all the chosen features from the above modelling - each list containing the features 
    # chosen during that iteration in a different list 
    max_key = max(stability_score) # maximum number of a list has repeated 
    max_val = stability_score[max(stability_score)] # the feauture list that has repeated the maximum number of times
    megalist = pd.DataFrame({'accuracy':np.round(a_new1,2), 'f1_score':np.round(f1_new1,2), 
                             'stability scores':[np.round(vals,2)], 'cummulative_stability_score':cum_ss,
                             'features':[final_feats], 'ss_for_the_whole_list':max_key, 
                             'most_frequent_list':[max_val],'model':model_name[m], 'timebin':t})
    return(megalist)

def calling_func_acc_threshold(pnb_df1, models, iterations, num_features_to_choose, model_name, acc_thresh, unique_doses):
    global acc, f1, fl, features,new_dict_X_train, new_dict_X_test, new_dict_y_train, new_dict_y_test, dataset,m,t, model
    d = pd.DataFrame()
    df_wo_thresh = pd.DataFrame()
    for d1 in unique_doses:
        if d1 != 'Vehicle':
            dmn = [d1, 'Vehicle']
            dff = pnb_df1[pnb_df1.target.isin(dmn)]
            dff['target'] = dff['target'].map({d1: 1, 'Vehicle': 0})
            for t in range(len(timepoint)):
                df_new1 = pd.DataFrame()
                df_new2 = pd.DataFrame()
                dataset = dff.loc[idx[:,t],:]
                for m in range(len(models)):
                    model = models[m]
                    acc, f1, fl, features,new_dict_X_train, new_dict_X_test, new_dict_y_train, new_dict_y_test  = [], [], [], [], [], [], [], []
                    new_dict_X_train, new_dict_X_test, new_dict_y_train, new_dict_y_test = bootstrap_data(dff,iterations)
                    pool = multiprocessing.Pool(iterations)
                    if models[m] == best_random:
                        model = best_random
                        l1 = pool.map(rfe_modelling_rf, range(iterations))
                    else:
                        l1 = pool.map(rfe_modelling, range(iterations))
                    pool.close()
                    pool.join()
                    features_new, fl_new, a_new, f1_new = unzipping_multiprocessing_data(l1)
                    results_new1 = results(features_new, fl_new,iterations, a_new, f1_new, model_name)
                    df_new2 = df_new2.append(results_new1)
                df_new2['target'] = d1
                df_wo_thresh = df_wo_thresh.append(df_new2)
                d_new2 = df_new2[df_new2['accuracy'] >acc_thresh]
                d = d.append(d_new2)
    return(d, df_wo_thresh)

def most_consistent_features(data):
    """
    Collecting the most consistent features based on the machine learning models run
    """
    ss = list(data['stability scores'])
    feats = list(data['features'])
    res_list = []
    keys = []
    for feat in range(len(feats)):
        res = {feats[feat][i]: ss[feat][i] for i in range(len(feats[feat]))}
        res_list.append(res)
    if len(res_list) < 2:
        print("Please reduce the accuracy threshold, no features collected")
        sys.exit()
    result = dict(functools.reduce(operator.add, map(collections.Counter, res_list)))
    sorted_result = dict(sorted(result.items(), key=operator.itemgetter(1),reverse=True))
    sorted_list_feats10 = list(dict(itertools.islice(sorted_result.items(), 10)).keys())
    sorted_list_feats5 = list(dict(itertools.islice(sorted_result.items(), 5)).keys())
    avg_accuracy = np.mean(list(data['accuracy']))
    avg_f1 = np.mean(list(data['f1_score']))
    avg_ss10 = np.round(list(dict(itertools.islice(sorted_result.items(), 10)).values()),0)
    avg_ss5 =  np.round(list(dict(itertools.islice(sorted_result.items(), 5)).values()),0)
    d_new = pd.DataFrame({'avg_accuracy_all_models_timebins_doses': np.round(avg_accuracy,2), 'avg_f1score_all_models_timebins_doses': np.round(avg_f1, 2), 'top-10': [sorted_list_feats10], 'top-5':[sorted_list_feats5]})
    return(d_new, sorted_list_feats10, sorted_list_feats5)

def run_analysis(path_mat, path_binned, path_2hz, grouping, acc_thresh):
    """
    final function for running all the machine learning algorthms together
    """
    global unique_doses, best_random, models, model_name, iterations, num_features_to_choose, pnb_df1, data_finall, sorted_list_5_thresh, sorted_list_10_thresh, binned_2hz_thresh_most_consistent_features, timepoint, exclude_animals
    a = hdf5storage.loadmat(path_mat)
    a_2hz = sio.loadmat(path_2hz)
    t_2hz = a_2hz['results_reshaped']['ratioNormalized']
    a_binned = sio.loadmat(path_binned)
    t_binned = a_binned['results_reshaped']['ratioNormalized']
    e = a['exclude']
    excluded_mice = []
    if len(e) > 1:
        for val in e[0][0][0][0]:
            str_val = str(val)
            str_val = 'Mouse'+str_val.strip('.0')
            excluded_mice.append(str_val)
    data, unique_doses = load_data(a_2hz, t_2hz, t_binned, a_binned, grouping, excluded_mice)
    best_random = RandomForestClassifier()
    models = [LogisticRegression(), LinearDiscriminantAnalysis(), SVC(kernel = "linear"), best_random]
    model_name = ['LR', 'LDA', 'SVM', 'RF']
    iterations = 40
    num_features_to_choose = 5
    pnb_df1 = data
    time = a_2hz['results_reshaped']['analysisTime']
    timepoint = time[0][0][0][:-1]
    data_finall, data_finall_wo_thresh = calling_func_acc_threshold(pnb_df1, models, iterations, num_features_to_choose, model_name, acc_thresh, unique_doses)
    binned_2hz_thresh_most_consistent_features, sorted_list_10_thresh, sorted_list_5_thresh = most_consistent_features(data_finall)
    
    print('top-5-features: ', sorted_list_5_thresh)
    for t in range(len(timepoint)):
        pnb_df1.loc[idx[:,t], 'timepoint']  = t
    for d1 in sorted_list_10_thresh:
        sns.lineplot(x = 'timepoint', y = pnb_df1[d1], hue = 'target', data = pnb_df1)
        strr = ('Line plot for frequency ' + d1 + 'Hz' + 'dose - ' + unique_doses[1][0:6] + 'group ' + grouping)
        plt.title(strr)
        plt.show()
    return(binned_2hz_thresh_most_consistent_features, data_finall, data_finall_wo_thresh)


if __name__ == "__main__":

    """
    Calling all the functions together
    """

    path_mat, path_binned, path_2hz, grouping, acc_thresh = get_input()
    binned_2hz_thresh_most_consistent_features, data_finall, data_finall_wo_thresh = run_analysis(path_mat, path_binned, path_2hz, grouping, acc_thresh)
    str2 = str(''.join(['most_consistent_features', unique_doses[1]]))
    path1 = str2 + grouping+'.csv'
    binned_2hz_thresh_most_consistent_features.to_csv(path1)
    str2 = str(''.join(['modelling_results_with_threshold', unique_doses[1]]))
    path2 = str2 +grouping+ ".csv"
    data_finall.to_csv(path2)
    str2 = str(''.join(['complete_modelling_results', unique_doses[1]]))
    path3 = str2 +grouping+ ".csv"
    data_finall_wo_thresh.to_csv(path3)    
