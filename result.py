# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.11

import numpy as np
from typing import List, Tuple

class MinMaxScaler:
    
    def __init__(self):
        self.minimum = None
        self.maximum = None

    
    def _check_is_array(self = None, x = None):
        """
        Try to convert x to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        pass
    # WARNING: Decompyle incomplete

    
    def fit(self = None, x = None):
        x = self._check_is_array(x)
    # WARNING: Decompyle incomplete

    
    def transform(self = None, x = None):
        '''
        MinMax Scale the given vector
        '''
        x = self._check_is_array(x)
        diff_max_min = self.maximum - self.minimum
        return (x - self.minimum) / (self.maximum - self.minimum)

    
    def fit_transform(self = None, x = None):
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)



class StandardScaler:
    
    def __init__(self):
        self.mean = None
        self.std = None

    
    def fit(self, X):
        pass
    # WARNING: Decompyle incomplete

    
    def transform(self, X):
        return (X - self.mean) / self.std

    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)