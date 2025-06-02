
# PEP 8 Advanced Style Guide Summary

## 🔧 Advanced Code Layout
- Continuation lines should align wrapped elements vertically (recommended) or use a hanging indent.
- Use implicit line continuation inside parentheses, brackets, and braces whenever possible.
- Avoid backslashes (`\`) for line continuation except when necessary.

## 🧼 Whitespace in Expressions and Statements
- **Don't** use spaces around the `=` sign for keyword arguments or default parameters.
  ```python
  def function(arg=default)  # ✅
  def function(arg = default)  # ❌
  ```
- **Don't** use spaces around the `:` in dictionary declarations.
  ```python
  d = {'key': 'value'}  # ✅
  d = {'key' : 'value'}  # ❌
  ```

## 🧠 Programming Recommendations
- Use `is not` rather than `not ... is`.
- Use `is None` instead of `== None`.
- Don't compare boolean values to `True` or `False` using `==`.

## 🏷 Naming Conventions (More)

| Type                      | Convention                 |
|---------------------------|----------------------------|
| Module names              | `lowercase_with_underscores` |
| Package names             | `lowercase`                   |
| Class names               | `CapWords` (PascalCase)       |
| Global constants          | `ALL_CAPS_WITH_UNDERSCORES`   |
| Exception names           | `CapWords` + `Error` (e.g., `MyCustomError`) |
| Private class attributes  | `_single_leading_underscore`  |
| Magic methods             | `__double_underscore__` (e.g., `__init__`, `__str__`) |

## 🚫 Don'ts (Common Mistakes to Avoid)
- Don't use mutable default arguments like lists or dicts in functions:
  ```python
  def bad_function(data=[])  # ❌
  def good_function(data=None):  # ✅
      if data is None:
          data = []
  ```
- Avoid mixing tabs and spaces for indentation.
- Don't write overly complex one-liners.

## 📜 Imports (More Details)
- Always put imports at the **top of the file**.
- Group imports in three sections (with blank lines between them):
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library imports
- Alphabetize imports within each section.

## 🧪 Testing and Logging Style
- Use `unittest` or `pytest` with descriptive test function names.
- Use `logging` instead of `print()` for status messages in production code.
