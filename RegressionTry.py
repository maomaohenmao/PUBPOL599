# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:55:44 2018

@author: Qi Suo
"""
corruptLink='https://raw.githubusercontent.com/EvansDataScience/data/master/corruption.csv'
econoLink='https://raw.githubusercontent.com/EvansDataScience/data/master/economic.csv'
enviroLink='https://raw.githubusercontent.com/EvansDataScience/data/master/environment.csv'
pressLink='https://raw.githubusercontent.com/EvansDataScience/data/master/pressfreedom.csv'
#%%
import pandas as pd
corrupt=pd.read_csv(corruptLink,encoding='Latin-1')
econo=pd.read_csv(econoLink,encoding='Latin-1')
enviro=pd.read_csv(enviroLink,encoding='Latin-1')
press=pd.read_csv(pressLink,encoding='Latin-1')
#%%
indexes1=pd.merge(corrupt,econo)
indexes2=pd.merge(press,enviro)
indexes=pd.merge(indexes1,indexes2)
#%%
indexes.dtypes
#%%
indexes.describe(include='all')
#%%
def reverse(aColumn):
    return max(aColumn) - aColumn + min(aColumn)
#%%
indexes['scorepressOK']=reverse(indexes.scorepress)
#%%
from pandas.api.types import CategoricalDtype
indexes['presscat']=indexes['presscat'].astype(CategoricalDtype(categories=['Low','Medium','High'], ordered=True))
#%%
%matplotlib inline
indexes.environment.hist()
#%%
from scipy.stats import pearsonr

explanans=indexes.columns[[1,3,8]]
for x in explanans:
    p=pearsonr(indexes[x],indexes.environment)
    print('Pearson',p[0],' \t Is significative?',p[1]<0.05)
#%%
indexes[explanans].corr()
#%%
indexes.index=indexes.Country
#%%
import statsmodels.formula.api as smf

formula='environment ~ corruptionIndex + scoreEconomy + scorepressOK'
LinRegEPI = smf.ols(formula, data=indexes).fit()
#%%
LinRegEPI.summary()
#%%
#results in simple terms
pd.concat({'Coefficients':LinRegEPI.params, 
           'Significant?':LinRegEPI.pvalues<0.05},axis=1)
#%%#global measure: the closer to 1 the better
LinRegEPI.rsquared_adj
#%%
import matplotlib.pyplot as plt 
import statsmodels.api as sm

fig, ax = plt.subplots(figsize=(12,8))
#decorations
hats=LinRegEPI.get_influence().hat_diag_factor
ax.axhspan(-2,2,edgecolor='r',facecolor='g',fill=True,ls='--',alpha=0.1) #outside box residuals warning
ax.axvline(2*hats.mean(),ls='dashed',c='r')#vertical line for leverage warning

# main plot
fig = sm.graphics.influence_plot(LinRegEPI,  ax = ax, criterion="cooks")
#%%
from statsmodels.robust.robust_linear_model import RLM

formula='environment ~ corruptionIndex + scoreEconomy + scorepressOK'
LinRegEPI_R = RLM.from_formula(formula, indexes).fit()
#print(LinRegEPI_R.summary())
#%%
pd.concat({'Coefficients':LinRegEPI_R.params,
           'Significant?':LinRegEPI_R.pvalues<0.05},axis=1)
#%%
formula='environment ~ corruptionIndex + scoreEconomy + C(presscat, Treatment("High"))'
LinRegEPI_catX = smf.ols(formula, indexes).fit()
#print(LinRegEPI_catX.summary())
#%%
pd.concat({'Coefficients':LinRegEPI_catX.params,
           'Significant?':LinRegEPI_catX.pvalues<0.05},axis=1)
#%%
LinRegEPI_catX.rsquared_adj
#%%
indexes.environmentCat.value_counts().plot.bar()
#%%
from statsmodels.formula.api import logit
formula='environmentCat ~ corruptionIndex + scoreEconomy + scorepressOK'
LogitEPI_a = logit(formula,data=indexes).fit()
#print (LogitEPI_a.summary())
#%%
from scipy import stats
stats.chisqprob = lambda chisq, df: stats.chi2.sf(chisq, df)

print(LogitEPI_a.summary())
#%%
import numpy as np
pd.concat({'Coefficients':np.exp(LogitEPI_a.params),
           'Significant?':LogitEPI_a.pvalues<0.05},axis=1)
#%%
from statsmodels.formula.api import logit
formula2='environmentCat ~ corruptionIndex + scoreEconomy + C(presscat, Treatment("High"))'
LogitEPI_b = logit(formula2,data=indexes).fit()
print(LogitEPI_b.summary())
#%%#global measure: the closer to 1 the better
if LogitEPI_a.aic < LogitEPI_b.aic:
    print("model 'a' is better")
else: print("model 'b' is better")
#%%
actualValues=indexes.environmentCat
# true if > 0.5
# int() transforms true to 1, or to zero if false
threshold=0.5
predictedValues=[int (x) for x in LogitEPI_a.predict()>threshold]
#%%
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(actualValues, predictedValues)
cm
#%%
cm= pd.DataFrame(cm,
                 columns=['PredictedNegative','PredictedPositive'],
                 index=['ActualNegative','ActualPositive'])
cm
#%%
from sklearn.metrics import roc_curve, auc
#import matplotlib.pyplot as plt
#getting values:
false_positive_rate, true_positive_rate, thresholds = roc_curve(actualValues, LogitEPI_a.predict())
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate)
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate(Sensitivity)')
plt.xlabel('False Positive Rate(Specificity)')
plt.show()
#%%
roc_auc = auc(false_positive_rate, true_positive_rate)
roc_auc
#%%
TruePositive=cm.loc['ActualPositive','PredictedPositive']
TrueNegative=cm.loc['ActualNegative','PredictedNegative']
FalsePositive=cm.loc['ActualNegative','PredictedPositive']
FalseNegative=cm.loc['ActualPositive','PredictedNegative']
#%%
Sensitivity = TruePositive/(TruePositive+FalseNegative)
Sensitivity
#%%
Specificity=TrueNegative/(FalsePositive+TrueNegative)
Specificity