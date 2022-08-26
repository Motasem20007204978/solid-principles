# solid-principles

to apply the design patterns, I need to know the following solid principles:

this article is about the OOD (Object Oriented Design):
https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/

s: Single Responsibility Principle
the module should be to solve only one problem and has a single reason to change.
eg. if a team working on a project and upload changes to github, if the team follows
    the SRP, the team will merge changes without conflict.
like facade pattern, the module should be to solve only one problem.

o: Open/Closed Principle
the module should be open for extension but closed for modification.
any one can add new features to improve the functionality, 
    but cannot modify the existing code to add new features.



l: Liskov Substitution Principle 
for inheritance process 
can substitute the base class with a subclass without modifying the code.
eg. a inherits form b, i can substitute the object b with a without any violation.
A object  new A(); or A object = new B();
like factory pattern, the object can be created by the subclass.


i: Interface Segregation Principle
avoid making interface that contains too many methods with more than one ralated logic.
segregation means to separate the interfaces to make one related logic.
cliens shoild not be forced to implement methods they don't want to use.


d: Dependency Inversion Principle 
the module should be depend on abstractions, not on concretions.
the class should not know the functionality of the method
as same as Open Closed Principle in structure.
