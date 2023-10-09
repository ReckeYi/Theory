# Decorator is a function that expects ANOTHER function as a parameter
def my_shiny_new_decorator(a_function_to_decorate):
    # Inside the decorator, it defines a function "wrapper".
    # It will be wrapped around the decorated function,
    # allowing arbitrary code to be executed before and after it.

    def the_wrapper_around_the_original_function():
        # Place here the code that we want to run BEFORE
        # calling the original function
        print("I'm the code that runs before the function call")

        # CALL the decorated function itself
        a_function_to_decorate()

        # And here we place the code that we want to run AFTER
        # calling the original function
        print("And I'm the code that runs after")

    # At this point, the function "a_function_to_decorate" has NOT BEEN CALLED YET

    # Now, return the wrapper function that contains
    # the decorated function and the code to be executed before and after.
    # It's that simple!
    return the_wrapper_around_the_original_function


# Let's imagine now that we have a function that we don't plan to touch anymore.
def a_stand_alone_function():
    print("I'm a simple, lonely function, you wouldn't dare to change me...")


a_stand_alone_function()
# Output: I'm a simple, lonely function, you wouldn't dare to change me...

# However, to change its behavior, we can decorate it, i.e.
# simply pass it to a decorator that wraps the original function in any code
# we need and returns a new, ready-to-use function:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()


# Output:
# I'm the code that runs before the function call
# I'm a simple, lonely function, you wouldn't dare to change me...
# And I'm the code that runs after

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello habr"


print(hello())
# Output: <b><i>hello habr</i></b>
