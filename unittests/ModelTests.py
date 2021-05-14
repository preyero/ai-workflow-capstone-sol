#!/usr/bin/env python
"""
model tests
"""


import unittest

## import model specific functions and variables
from scripts.model import *

MODEL_DIR = "models"
MODEL_VERSION = 0.1

class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """

        ## train the model
        tag = 'all'
        model_name = re.sub("\.", "_", str(MODEL_VERSION))
        model_train()
        SAVED_MODEL = os.path.join(MODEL_DIR,
                                   "sl-{}-{}.joblib".format(tag,model_name))
        self.assertTrue(os.path.exists(SAVED_MODEL))

    def test_02_load(self):
        """
        test the train functionality
        """
        tag = 'all'
        ## train the model
        data, model = model_load()
        
        self.assertTrue('predict' in dir(model[tag]))
        self.assertTrue('fit' in dir(model[tag]))

    def test_03_predict(self):
        """
        test the predict function input
        """

        ## ensure that a list can be passed
        test=False
        query = {'country': 'all',
                 'year': '2018',
                 'month': '01',
                 'day': '05'
        }

        result = model_predict(query['country'],
                            query['year'], query['month'], query['day'],
                            test=test)
        y_pred = list(result['y_pred'])
        self.assertTrue(np.round(y_pred,3) in [184414.794])

          
### Run the tests
if __name__ == '__main__':
    unittest.main()
