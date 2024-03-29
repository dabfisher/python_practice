# **Python Practice**
## **Cheat Sheets**
https://docs.python.org/3/library/functions.html#round
## **Notes**
### **General Commands**
- *print(type())*: <class 'str'>
- Control Flow: order which statements, instructions or function calls are executed or evaluated`
- Boolean Expressions*:* *True* or *False*
- Indentation: Identifies lines of code to be executed together
### Loops: process of iteration
    1. *Initialization*:
    2. *Repitition*:
    3. *End condition*: 
        - For Loop: indentation signifies body "action" of for loop, end of indentation signifies end condition
        - While Loop: Fulfillment of <conditional statement> signifies end condition, indentation still signifies body "action" of for loop 
- Types of Loops:
    1. *For*: iteration for each element in collection
        {
            for <temporary variable> in <collection>: 
                <action> or <body>
        }
    2. *While*: loop performs form of indefinite iteration and 
        {
            for <conditional statement>: 
                <action> or <body>
        }
    3. *List comprehension*: clean way to .append() a list, can be expanded with a conditional statement including *if - else* statements
        {
            new_list = [<expression> for <element> in <collection> if <element> <expression>]
        }
        EXPANDED
        {
            for <element> in <collection>:
                print(<element>)
                new_list.append(<expression>)
        }
- Loop Control:
    - Break: immediately terminates a loop
        {
            <loop>
                <action> or <body>
                <conditional statement>
                    <action> or <body>
                    <break>
        }
    - Control: will skip current iteration of a loop
         {
            <loop>
                <action> or <body>
                <conditional statement>
                    <condition>
                <action> or <body>
         }
    - Nested Loops: 
        {
            <loop>
                <loop>  
                    <action> or <body>
                    <conditional statement>
                    ...
        }
#### Relational Operators: 
- *==* Equals
- *!=* Not Equals
- *>* Greater than
- *>=* Greater than or equal to
- *<* Less than
- *<=* Less than or equal to
* *bool*: Only *True* and *False* are *bool* types
#### Hot Keys & Syntax: 
- ctrl + /: comments/uncomments out whole section
- *';'*: denotes a separate line of code
- ctrl + c: cancels a infinite loop 
#### Boolean Operators:
- *and*: combines and evaluates two boolean expressions as *True*
- *or*: either component of expression true
- *not*: reverses boolean value
#### Conditional Statements: 
- *if*: [boolean expression] is true*_:_* then [execution]
- *else*: [execution] when *if* conditions aren't met
- *elif*: chains *if* statements and checks conditions from top to bottom
### Python Errors:
- *SyntaxError*: Error cause by not following the proper structure (syntax) of the language
    - *EOF*: python expected code but it end of file first
- *NameError*: Errors reported when the interpreter detects a variable that is unknown
- *TypeError*: Errors thrown when an operation is applied to an object of inappropriate type
- *IndentationError*: Error thrown when indentation is expected in a block of code
### Data Structures
- *List*: 
    - begins and ends with "[]", items separated with ",", insert space after each comma
    - code reads list in sequential order
    - can combine multiple data types in one list [str, int, bool, float]
    - can be empty
    - zero indexed
    - *list_name.method()*
        - .append(): add to end of list
        - .remove("",#): removes items with a specific/matching string or at sequential numbe (duplicated elements will only remove first instance)
    - + []: new_variable = list + [new_items], can only be used with other lists
    - (list_name[#]): accesses elements, number can only be int
    - (list_name[-#]): accesses elements reverse order, -1 results in last item on list
    - (list_name[# or -#]) = "new_element": replaces element at number position
    - 2D Lists: *2dlist_name = [[L1.1, L2.1...], [L1.2, L2.2...]...]
    - 2D Accessing: new_variable = list[L1][.1], only int's can be used
    - 2D Modifying: list[L1][.1] = "Modification"
    - Slicing: sliced_list = list[*#*:#], *1st inclusive*, 2nd <, reverse slice [-#*:
#*], upto [*#*,-#]
- *Tuples*:
    - uses ('tuple') instead of ['list']
    - data structure that allows for storage of multiple times of data inside of it
    - difference to a list is items inside are immutable/unchangable
    - accessible like a list
    - variable.1, ...varible.nc = #_tuple_elements: can be upacked
    - one_element_tuple = (element,): trailing comma is necessary for this unique case because of math operations
- *String*:
    - a string is a list
    - designated by 'string' or "string"
    - can be sliced using string[first_index:last_index], an empty side of the slice will run to end or beginning of string, back half of slice is non-inclusive, but index starts at 0
    - Concatenate by combined_string = 1st_string + 2nd_string
    - len() counts characters in a string and includes spaces in the count
    - negative indices count backwards using string[-#]
    - strings are immutable, cannot be changed
    - \ will escape special characters that python usually reads as code away from code (ex: \")
    - iteration works with strings because they are lists
    - 'in' checks if one part of a string is in another string
- *String Methods*:
    - Syntax: string_name.string_method(arguments)
    - string methods do not change strings as strings are immutable
    - ' '.upper(): formatting method
    - ' '.lower(): formatting method
    - ' '.title(): formatting method
    - ' '.split(): splits a string at 'delimiter', no delimiter splits at spaces
    - ' '.join([])
    - ' '.replace()
    - ' '.strip()
    - ' '.upper(), .title(), and .lower() adjust the casing of your string
    - ' '.split() takes a string and creates a list of substrings
    - ' '.join() takes a list of strings and creates a string
    - ' '.strip() cleans off whitespace, or other noise from the beginning and end of a string
    - ' '.replace() replaces all instances of a character/string in a string with another character/string
    - ' '.find() searches a string for a character/string and returns the index value that character/string is found at
    - ' '.format() allows you to interpolate a string with variables
    - "{} {}".format()

### Methods & Functions: Built-in functionality to manipulate data
- **Methods**: *list.method(input)* 
- **Built-in Functions**: *builtinfunction(input)* 
    - .append(): list method add element to end of list
    - .remove(): list method remove first instance of element
    - .count("") or .count([], []): list method counts occurance of element
    - .insert(#, element_to_add): list method inserts into specific index
    - .pop(#) or removed_element = _.pop(#): list method remove element from specific index or end of list *()*, returns value removed
    - .range(*0*-#) or .range(#, #) or .range(#, #, #): function to create sequence of int's, starts at *0*, creates an object *print(variable(range())*, *1st inclusive*, 2nd <, 3rd input skips
    - .temp(): can track loops
        {
            for temp_var in range(#):
                (<action> + str(temp + 1)
        }
    - .len(): function to get length of list, creates an object *print(variable(range()))*
    - .sort(): function to sort a list, will replace variable as sorted, .sort(reverse=True)
    - sorted(): before list instead of after, generates new list rather than modifying
    - zip(): combines associated data-set w/o reliance on multi-dimensional lists, zips lists together as tuples, zips are stored as a memory objects
        {
            Ex:
            list.1 = [a.elements.n]
            list.2 = [b.elements.n]
            zip_l1_l2 = zip(list.1, list.2)
            print(zip_l1_l2) **OUTPUTS** <zip object at 0x7f1631e86b48>
            convert_to_list = list(zip_l1_l2)
            print(convert_to_list) **OUTPUTS** [("a.elements.n", "b.elements.n")] *inner lists are tuples*
        }
- **Building User-Defined Functions**: group code into reusable block.
    - def function_name(parameter.1, ...parameter.n): *def* indicates beginning of function, followed by name in snake_case format, followed by *'()'* which holds parameters (input items), "':'" marks end of function header
    - body of function: indentation following heading signifies the body and what tasks the function will perform
    - call a function: function's name w/ parenthesis, no indentation, will print the outcome
    - return: will save outcomes of a function rather than print them, can return multiple values [return r.1, ...r.n]
- **Arguments of Functions**: python has 3 different types of arguments functions
    - Positional Argument: arguments can be called by their poisition in function definition
    - Keyword Argument: arguments can be called by their name
    - Default Argument: arguments are given default values

### Modules
- Files: have scope, file libraries cannot call each other

### Dictionaries
- ' '.get(, *null value*): method to search a dictionary
- ' '.pop(, *null value*): method to remove key and pairs from dictionary
- list(): function to list dictionary key values
- ' '.keys(): method to return view object of key, which can't be modified but can be used for iteration
- ' '.values(): method to return view object of values, can be made into list form using list(dict.values())
- ' '.items(): method for dictionary objects (key & value) as a tuple

### Files
- with open(' ', 'w' or 'a'): with opens a content manager, allows python to work with things that aren't necessary python, but needs to be close
- ' '.read()
- ' '.readlines()
- ' '.readline()
- ' '.write()
- ' '.close(): closes a with statement
- ' '.DictReader(' ', delimiter=' '): turns csv's into python data
- open(' ', newlinge=' '): function so that we don’t accidentally mistake a line break in one of our data fields as a new row in our csv
- ' '
