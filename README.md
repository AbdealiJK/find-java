# Find java

Finding Java can be a big issue sometimes. Figuring out which java installations
are present and identifying which one to use is not a trivial task with the
numerous different ways you can install java.

To find java, just call:

```python
>>> import findjava
>>> findjava.find()
'/Library/Java/JavaVirtualMachines/jdk1.8.0_162.jdk/Contents/Home'
```

or directly in a shell run:

```bash
$ findjava
JAVA_HOME detected at: /Library/Java/JavaVirtualMachines/jdk1.8.0_162.jdk/Contents/Home
```
