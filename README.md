# Pythonic Switch Case
### A pythonic way to implement switch-case
##### What is "Switch-case"?
A switch case is a way to control the flow of a program depending on the value of a variable. Example in java:

```java
switch (day) {
    case 1:
        System.out.print("Monday");
        break;
    case 2:
        System.out.print("Tuesday");
        break;
    case 3:
        System.out.print("Wednesday")
        break;
    default:
        System.out.print("Other days");
        break;
}
```
A switch case is faster than an If-else since it maps the code to certain values. This means that instead of comparing 3 times you just have to get some code from a map (dictionary). Now python doesn't support switch cases, so here is how I made one!

##### How to use
Being a pythoneer, I have used a class to implement the switch case

```python
# First import the class (Yes, it is just one class)
from pySwitch import Switch

# Now you can make a switch object
# Pass in the value
sw = Switch(day)

# You can add cases easily
sw.case(1, print, "Monday")
sw.case(2, print, "Tuesday")
sw.case(3, print, "Wednesday")

# And you can add a default
sw.default(print, "Other days")
```

Now for the smart people out there, you can use lambda functions to put args and kwargs together.
```py
sw.case(1, lambda: print("Monday"))
```

And you can put multiline code snippets by defining them and deleting them after
When you want to delete the switch, call the kill function first and then you can safely delete the object
