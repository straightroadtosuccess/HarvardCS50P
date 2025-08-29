class Jar:
    def __init__(self, capacity=12):
        # If capacity is not an int or is negative
        if type(capacity) != int or capacity < 0:
            # Raise error
            raise ValueError
        # Initialize the jar's capacity and start with 0 cookies inside
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Return 🍪 amount in jar
        return "🍪" * self._size

    def deposit(self, n):
        # If amount of cookies is greater than capacity
        if self._size + n > self.capacity:
            # Raise error
            raise ValueError
        # Add cookies to jar
        self._size += n

    def withdraw(self, n):
        # If amount of cookies to withdraw is more than how many are there
        if n > self.size:
            # Raise error
            raise ValueError
        # Remove cookies
        self._size -= n

    @property
    def capacity(self):
        # Return capacity of jar
        return self._capacity

    @property
    def size(self):
        # Return amount of cookies in jar
        return self._size
