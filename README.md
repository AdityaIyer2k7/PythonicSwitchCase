# Switch case in python
### A pythonic way to implement switch-case
##### What is "Switch-case"?
A switch case is a way to control the flow of a program depending on the value of a variable. Example in java:

```
switch (day) {
    case 1:
        print("Monday");
        break;
    case 2:
        print("Tuesday");
        break;
    default:
        print("Other days");
        break;
}
```
A switch case is faster than an If-else since it maps the code to certain values. This means that instead of comparing 3 times you just have to get some code from a map (dictionary). Now python doesn't support switch cases, so lets build our own!
