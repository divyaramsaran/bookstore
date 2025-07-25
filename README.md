# Python Lists & Sets – Practice Assignment

## Problem Statement

You are tasked with creating a Python program to help a small bookstore manage its inventory and customer wishlists using lists and sets. The program should perform various operations on lists and sets such as adding, removing items, finding unique entries, and intersecting data sets to extract useful insights.

This assignment will solidify your understanding of Python lists and sets and introduce you to common data manipulation techniques.

---

## Project Name

**Bookstore Inventory & Wishlist Manager**

---

## Functional Requirements

- Maintain an **inventory list** of books available in the bookstore.
- Maintain **customer wishlists** represented as sets, indicating which books customers want.
- Allow adding and removing books from the inventory.
- Allow customers to add or remove books from their wishlists.
- Provide functionality to:
  - Find the total number of unique book titles in a wishlist.
  - Find books common between the inventory and a customer’s wishlist.
  - Find books in the wishlist that are not currently in inventory.
  - Merge multiple wishlists to see all desired books collectively.
  - Find books in inventory that no customers have wished for (unsought books).

---

## Input and Output Specifications

### Inputs

- Initial bookstore inventory list (predefined or input by user).
- Multiple customer wishlists (each as a set of book titles).
- Commands/input to add or remove books from inventory or wishlists.
- Queries to perform the required set/list operations.

### Outputs

- Confirmation messages when books are added or removed.
- Lists or sets of books resulting from queries (e.g., common books, unique books).
- Clear display formats for inventory, wishlists, and query results.

---

## Example Input/Output

### Example 1: Initial Data

Initial inventory list
inventory = ['Harry Potter', 'The Alchemist', 'Atomic Habits', 'Clean Code', 'Python Crash Course']

Customer wishlists as sets
alice_wishlist = {'Harry Potter', 'Deep Work', 'Clean Code'}
bob_wishlist = {'Atomic Habits', 'Clean Code', 'The Pragmatic Programmer'}

### Example 2: Queries and Expected Outputs

**Query:** What books does Alice want that are in the inventory?  
**Output:** `{'Harry Potter', 'Clean Code'}`

**Query:** What books does Bob want that are NOT in the inventory?  
**Output:** `{'The Pragmatic Programmer'}`

**Query:** What are all unique books wished by Alice and Bob together?  
**Output:** `{'Harry Potter', 'Deep Work', 'Clean Code', 'Atomic Habits', 'The Pragmatic Programmer'}`

**Query:** Which books in inventory are not wished by any customer?  
**Output:** `{'Python Crash Course', 'The Alchemist'}`
