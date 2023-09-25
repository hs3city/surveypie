# Docstrings

## Introduction

Documenting the code is a priority, and you should develop coding pattern whcih follows those steps:

1. Think what you want to achieve.
2. Write a definition of a function or a class, and create a docstring foundation. The good start is writing a sentence what the function does.
3. Write a function body.
4. Update docstring.
5. Write tests.

You may start from unit tests if you prefer this form of programming, but a docstring should be initialized before you start writing a function body. This pattern is grounding your mind on the solution that you are going to implement. Moreover, you will quickly realize that if you cannot describe function in one sentence it should be divided into two or more blocks of code.

## General rules

We use [Numpy docstrings](https://numpydoc.readthedocs.io/en/latest/format.html) to document our code.

As a rule of thumb, we document all public functions and classes, and we document private functions and classes if they perform complex computations.

## Examples

You should follow [Numpy docstrings](https://numpydoc.readthedocs.io/en/latest/format.html) definitions, but we provide some examples of docstrings that we use in this project.

Treat the examples as a reference.

### Contents

- [Function Docstring](#functions)
- [Class Docstring](#class)
- [Module Docstring](#modules)

#### Functions

Parts:

1. (Required) `Short description`,
2. (Optional) Function `summary`,
3. (Required) `Parameters` (if any is passed into a function),
4. (Required) `Returns` (if function returns any value) or `Yields` (if function is a generator),
5. (Optional) `Receives` parameters send to generator with `.send()` method.
6. (Optional) `Other Parameters`.
7. (Required) `Raises`.
8. (Required) `Warns`.
9. (Optional) `Warnings` - optional warnings.
10. (Optional) `See Also` - links to the similar or important functions, classes, etc.
11. (Optional) `Notes` - equations and explanations.
12. (Required) `References` - if code is based on a specific publication or a work of someone else then it should be cited here.
13. (Required) `Examples` - example of usage.

##### Template

```python

def do_something(a: float, b, c_opt=None) -> int:
    """Short description of the process.
    
    Here we write extended summary if needed. Bibliography links and usages in Notes part.
    
    Parameters
    -----------
    a : float
        Description of the parameter ``a``.
        
    b
        Description of the parameter ``b`` without any type.
        
    c_opt : float or None, optional, default=None
        Description of the ``c_opt`` parameter.
            
    Returns
    -------
    output : int
             Description of the output
             
    Raises
    ------
    SomeSpecificException
        Some functions performs checks and raises exceptions. Write here why and when exception is thrown.
        
    Warns
    -----
    SomeSpecificWarning
       Some functions performs checks and raises warnings. Write here why and when warning is thrown.
        
    References
    ----------
    .. [1] Numpydoc maintaners. https://numpydoc.readthedocs.io/en/latest/format.html 2019
    
    Examples
    --------
    >>> import numpy as np
    >>> a_var = 1
    >>> b_var = np.arange(0, 1000)
    >>> value = do_something(a_var, b_var)
    >>> print(value)
    0
    
    """
    ...
    
    return ...

```

##### Example

TODO: pick something from the project.

#### Class

Parts:

1. (Required) `Short description`,
2. (Optional) Class `summary`,
3. (Required) `Parameters` (if any is passed into class `__init__()`),
4. (Required) `Attributes` - only public.
5. (Required) `Methods` - only public and implemented dunder methods.
6. (Optional) `See Also` - links to the similar or important functions, classes, etc.
7. (Optional) `Notes` - equations and explanations.
8. (Required) `References` - if code is based on a publication or someone else's work then it should be cited here.
9. (Required) `Examples` - example of usage.

##### Template

```python

class MyClass:
    """
    Class stores data, and performs operations on it.
    
    Parameters
    ----------
    param_a : float
        A real number.
               
    Attributes
    ----------
    param_x : float
        A real number.
           
    param_y : int
        Value that ``param_x`` must be raised to.
                   
    Methods
    -------
    do_something()
        Transforms input data.
        
    __str__()
        Prints current state of the object.
        
    Examples
    --------
    >>> mycls = MyClass(0)
    >>> mycls.do_something()
    0
    >>> print(mycls)
    I'm the MyClass object and I did something!
    
    """
    
    def __init__(self, param_x: float):
        self.param_x = param_x
        self.param_y = 44
        self.result = self.do_something()
        
    def do_something(self):
        """
        Method raises ``param_x`` to the power of ``param_y`` and stores result in the ``result`` attribute.
        
        Returns
        -------
        : float
            ``param_x`` raised to the power of ``param_y``.
        """
        return self.param_x**self.param_y
        
    def __str__(self):
        return f'I"m the MyClass object and I did something!.'

```

##### Example

TODO: pick something from the project.

#### Modules

**Important!**

A description of modules in **ordinal-scale-stats-py** is slightly different than the `numpy` style. We include module docstring at a top of the file that groups multiple functions and classes and has own specific logic.

Parts:

1. (Required) `Short description`,
2. (Required) `Long description`,
3. (Required) `Changelog Table`: table with the major changes,
4. (Required) `Authors`: list with authors contributing to the module,
5. (Required) `References`: list of tutorials,
6. (Required) `Bibliography`: list of publications and articles related to the module.
7. (Optional) `TODO`: list of functions that should be created or debugged with links to the Github Issues.

The role of docstring in a module is to store information about changes, contributors and algorithm sources. We do not present examples - for this we have tutorials and function / class docs.

##### Template

```python
"""
Module description is placed at the top of a file.

Here we describe module in a detail. The most important questions to answer here are:
- what problem does module solve?
- what methods does module incorporate to solve this problem?
- what kind of data flows into module?
- what is the output of module?
- why this module is important?
- relation to other modules.

Changelog
---------

| Date       | Change description        | Author         |
|------------|---------------------------|----------------|
| 2022-02-16 | First release of document | @SimonMolinsky |

Authors
-------
- Szymon Molinski @SimonMolinsky
- Peter Pan @PP-GithubProfileAlias-099990

References
----------
- [Docstrings in package](url)
- [Other tutorial](url)

Bibliography
------------
- Docstrings in numpy. Numpydoc maintaners. https://numpydoc.readthedocs.io/en/latest/format.html 2019

TODO
----
- Create a docstring for the ``my_new_function()`` function.

"""
```

##### Example

TODO :)

## Resources

1. [Numpydoc maintainers and contributors. Style guide. 2019](https://numpydoc.readthedocs.io/en/latest/format.html)
2. David Goodger, Guido van Rossum [Python PEP257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)