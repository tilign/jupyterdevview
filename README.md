# Jupyter Dev View
Jupyter Dev View contains a style sheet that splits the jupyter output into a side by side view of code cells on the left, and output on the right.  
In addition to the stylesheet this package provides two functions to easily switch between the Dev View and the traditional notebook view.

```
    import jupyterdevview as jdv

    # Switch to dev view
    jdv.dev_view() 
    # Refresh your browser (ctrl-F5 for most browsers)
    
    # Switch back to notebook view
    jdv.notebook_view() 
    # Refresh your browser (ctrl-F5 for most browsers)
```
**NOTE: You will need to restart jupyter after the first time you run jdv.dev_view() for the changes to take effect.  Subsequently you will just need to refresh your browser**

One Paragraph of project description goes here

### Installing

Installation is through pip.  

```pip install jupyterdevview```

### Using

[first_cell.png]
[second_cell.png]
```
    import jupyterdevview as jdv

    # Switch to dev view
    jdv.dev_view() 
    # Refresh your browser (ctrl-F5 for most browsers)
    
    # Switch back to notebook view
    jdv.notebook_view() 
    # Refresh your browser (ctrl-F5 for most browsers)
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
