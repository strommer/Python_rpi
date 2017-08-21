import unittest

# ------------------------------------------------------
# Uncomment the following line, to get test_0... to pass
# ------------------------------------------------------
this_is_the_last_exercise = True

I_completed_the_course_evaluation = True

class MyException(Exception):
    pass

def my_function(x):
    if x == True:
        raise MyException

class MyResource:

    def __init__(self):
        self.state = 'Created'

    def getState(self):
        return self.state

    def __enter__(self):
        self.state = 'Opened'
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type == None:
            self.state = 'ClosedNoException'
        else:
            self.state = 'ClosedWithException'
        

#---------------------------------------------
# DO NOT MODIFY ANYTHING BELOW THIS LINE
#---------------------------------------------

class TestResource(unittest.TestCase):
    def ck(self,var,desc):
        if (not globals().get(var)):
            self.fail("Expected: " + var + ' = ' + desc)

    def test_0_show_example(self):
        # Define a variable, this_is_the_last_exercise, and set it to True
        self.ck('this_is_the_last_exercise', 'True')
    
    def test_1_complete_course_evaluation(self):
        # Define a variable, I_completed_the_course_evaluation,
        # and set it to True
        self.ck('I_completed_the_course_evaluation', 'True')

    def test_2_define_MyException(self):
        # Define a class, MyException, that inherits from Exception
        self.ck('MyException', 'Class that inherits from Exception')
        self.assertTrue(Exception in MyException.__bases__,
                        "MyException doesn't inherit from Exception")

    def test_3_define_my_function(self):
        self.ck('my_function', 'Function, such that my_function(x) throws ' +
                'a MyException if x is True')
        self.assertFalse(my_function(False),
                         "my_function(False) should return False")
        self.assertRaises(MyException, my_function, True)

    def test_4_define_MyResource(self):
        msg = 'Class that implements Resource Protocol'
        self.ck('MyResource', msg)
        try:
            r = MyResource()
        except:
            self.fail(msg)

    def test_5_check_if_MyResource_sets_state_to_Created(self):
        msg = ("Resource should define a method called getState")
        r = MyResource()
        self.assertTrue("getState" in dir(r), msg)
        self.assertEqual(r.getState(), "Created",
                         "Set state to 'Created' upon creation.")

    def test_6_check_if_MyResource_sets_state_to_Opened(self):
        try:
            with MyResource() as r:
                self.assertEqual(r.getState(), "Opened",
                             "Set state to 'Opened' in __enter__.")
        except:
            self.fail("Resource protocol requires definition of " +
                      "methods __enter__ and __exit__")

    def test_7_check_if_MyResource_sets_state_to_ClosedNoException(self):
        with MyResource() as r: pass
        self.assertEqual(r.getState(), "ClosedNoException",
                         "Set state to 'ClosedNoException' in __exit__.")

    def test_8_check_if_MyResource_sets_state_to_ClosedWithException(self):
        msg = ("If exception occurs, set state to 'ClosedWithException'"
               + "in __exit__.")
        try:
            with MyResource() as r: raise Exception("Throwing exception")
        except:
            pass
        self.assertEqual(r.getState(), "ClosedWithException", msg)

if __name__ == '__main__':
    unittest.main(exit=False, failfast=True)
    
