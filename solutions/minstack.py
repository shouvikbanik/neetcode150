class MinStack(object):

    def __init__(self):
        self.stack_of_values = []
        self.stack_of_min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack_of_min) != 0:
            self.stack_of_min.append(min(val, self.stack_of_min[len(self.stack_of_min) - 1]))
        else:
            self.stack_of_min.append(val)
        self.stack_of_values.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack_of_min.pop()
        return self.stack_of_values.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack_of_values[len(self.stack_of_values) - 1]

    def get_min(self):
        """
        :rtype: int
        """
        return self.stack_of_min[len(self.stack_of_min) - 1]
