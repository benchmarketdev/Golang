### Naming Schema

- UPPERCASE
  - Constants
  
- TitleCase
  - Classes
  - Exceptions
  
- camelCase
  - GUI functions and methods
  
- lowercase and lowercase_with_underscore
  - everything else
  
- Use an uppercase letter for the first letter of custom module filenames

### Docstring
> This is simply a string that comes immediately after the def line, and before the function’s code proper begins.

```
def function_name():
    """
    text documentation goes here.<a brief one-line description>
    <a blank line>
    <full description>
    """

```


### Module and package

`.pyo` - this is an optimized byte-code compiled version of the module.
`.pyc` - this is a nonoptimized byte-code compiled version of the module. 

If Python finds an up-to-date byte-code compiled version of the module, it loads it; otherwise, Python loads the `.py` file and compiles a `byte-code` compiled version. 

When Python is installed, the standard library modules are usually `byte-code` compiled as part of the installation process.

> A package is simply a directory that contains a set of modules and a file called `__init__.py`. 

> Using leading underscores(private data) so that if the module is imported.

